"""Metody porównania obrazu RTG z wzorcem. Liczą wyłącznie na karcie (CUDA).

Wspólny tor: obraz -> tłumienie a = -ln(I/255) -> zmniejszenie do ~1000 px wysokości ->
wyrównanie wzorca do obrazu -> dodatnia różnica tłumienia (dodatek = więcej materiału) ->
normalizacja szumem zależnym od jasności -> próg -> spójne obszary -> ramki w pikselach oryginału.

Warianty (hipotezy):
  H1   przesunięcie globalne (korelacja fazowa), różnica piksel w piksel
  H1t  jak H1 + tolerancja krawędzi (różnica do maksimum wzorca w oknie 5x5)
  H2   skala wzdłuż osi jazdy + lokalne pole przesunięć (kafle 128 px) + tolerancja 3x3
  H2n  jak H2 + mapa zmienności „normalnej” wyuczona z innych egzemplarzy typu w bibliotece (rozdz. 5)
  H2k  jak H2, ale różnica do 3 najpodobniejszych wzorców naraz (minimum) — mniej fałszywych alarmów
Wzorzec dobierany automatycznie z biblioteki (P8 B): najwyższa korelacja miniatury po wyrównaniu.
"""
import math

import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image
from scipy import ndimage

WARIANTY = {
    "H1": dict(skale=False, lokalnie=False, tol=1, nauka=False, top=1),
    "H1t": dict(skale=False, lokalnie=False, tol=5, nauka=False, top=1),
    "H2": dict(skale=True, lokalnie=True, tol=3, nauka=False, top=1),
    "H2n": dict(skale=True, lokalnie=True, tol=3, nauka=True, top=1),
    "H2k": dict(skale=True, lokalnie=True, tol=3, nauka=False, top=3),
}


def karta():
    if not torch.cuda.is_available():
        raise SystemExit("BRAK KARTY: metody liczą tylko na GPU (zasada zespołu) — przerwano")
    return torch.device("cuda")


def wczytaj(sciezka, dev, f=None):
    """Zwraca (tłumienie na karcie w rozdzielczości roboczej, współczynnik f, (H, W) oryginału)."""
    im = Image.open(sciezka)
    if im.mode != "L":
        im = im.convert("L")
    x = torch.from_numpy(np.asarray(im)).to(dev, non_blocking=True)
    H, W = x.shape
    if f is None:
        f = max(1, round(H / 1000))
    a = -torch.log((x.float() + 0.5) / 255.5)
    if f > 1:
        a = F.avg_pool2d(a[None, None], f)[0, 0]
    return a, f, (H, W)


def _okno(h, w, dev):
    return torch.hann_window(h, device=dev)[:, None] * torch.hann_window(w, device=dev)[None, :]


def _podpiksel(r, i, n):
    """Paraboliczne dopasowanie wzdłuż ostatniego wymiaru; r: (N, n), i: (N,)."""
    ar = torch.arange(r.shape[0], device=r.device)
    a, b, c = r[ar, (i - 1) % n], r[ar, i], r[ar, (i + 1) % n]
    den = a - 2 * b + c
    return torch.where(den.abs() > 1e-9, 0.5 * (a - c) / den, torch.zeros_like(den))


def korelacja_fazowa(stale, ruchome):
    """stale, ruchome: (N, h, w). Zwraca (dy, dx, szczyt), gdzie stale(x) ≈ ruchome(x - d)."""
    N, h, w = stale.shape
    okn = _okno(h, w, stale.device)
    s = (stale - stale.mean((1, 2), keepdim=True)) * okn
    m = (ruchome - ruchome.mean((1, 2), keepdim=True)) * okn
    R = torch.fft.rfft2(s) * torch.conj(torch.fft.rfft2(m))
    r = torch.fft.irfft2(R / (R.abs() + 1e-6), s=(h, w))
    flat = r.reshape(N, -1)
    szczyt, idx = flat.max(1)
    iy, ix = idx // w, idx % w
    ary = torch.arange(N, device=r.device)
    fy = _podpiksel(r[ary, :, ix], iy, h)
    fx = _podpiksel(r[ary, iy, :], ix, w)
    dy = torch.where(iy > h // 2, iy - h, iy).float() + fy
    dx = torch.where(ix > w // 2, ix - w, ix).float() + fx
    return dy, dx, szczyt


def siatka(h, w, dev, sx=1.0, dx=0.0, dy=0.0, pole=None):
    """Siatka grid_sample: piksel obrazu stałego -> współrzędne obrazu ruchomego."""
    yy = torch.arange(h, device=dev, dtype=torch.float32)[:, None].expand(h, w)
    xx = torch.arange(w, device=dev, dtype=torch.float32)[None, :].expand(h, w)
    if pole is not None:
        xx, yy = xx - pole[1], yy - pole[0]
    cx = w / 2
    xm = ((xx - dx) - cx) / sx + cx
    ym = yy - dy
    return torch.stack([(xm + 0.5) / w * 2 - 1, (ym + 0.5) / h * 2 - 1], -1)[None]


def przenies(m, g):
    return F.grid_sample(m[None, None], g, mode="bilinear", padding_mode="zeros", align_corners=False)[0, 0]


def wyrownaj(stale, ruchome, skale, lokalnie):
    """Zwraca siatkę przenoszącą 'ruchome' na układ 'stale'."""
    h, w = stale.shape
    dev = stale.device
    kandydaci = torch.arange(0.94, 1.0601, 0.005).tolist() if skale else [1.0]
    najl = None
    for i in range(0, len(kandydaci), 6):
        partia = kandydaci[i:i + 6]
        rs = torch.stack([przenies(ruchome, siatka(h, w, dev, sx)) for sx in partia])
        dy, dx, sz = korelacja_fazowa(stale[None].expand(len(partia), h, w), rs)
        j = int(sz.argmax())
        if najl is None or float(sz[j]) > najl[0]:
            najl = (float(sz[j]), partia[j], float(dx[j]), float(dy[j]))
    _, sx, dx, dy = najl
    g = siatka(h, w, dev, sx, dx, dy)
    if not lokalnie:
        return g
    # lokalne pole przesunięć na kaflach
    T, S = 128, 64
    rg = przenies(ruchome, g)
    ps = F.unfold(stale[None, None], T, stride=S)[0].T.reshape(-1, T, T)
    pr = F.unfold(rg[None, None], T, stride=S)[0].T.reshape(-1, T, T)
    ny, nx = (h - T) // S + 1, (w - T) // S + 1
    ky, kx, sz = korelacja_fazowa(ps, pr)
    dobre = (sz > 0.08) & (ps.std((1, 2)) > 0.02)
    ky = torch.where(dobre, ky, torch.zeros_like(ky)).reshape(1, 1, ny, nx)
    kx = torch.where(dobre, kx, torch.zeros_like(kx)).reshape(1, 1, ny, nx)
    pole = []
    for k in (ky, kx):
        k = F.pad(k, (1, 1, 1, 1), mode="replicate")
        k = F.unfold(k, 3).median(1).values.reshape(1, 1, ny, nx).clamp(-6, 6)
        pole.append(F.interpolate(k, size=(h, w), mode="bilinear", align_corners=False)[0, 0])
    return siatka(h, w, dev, sx, dx, dy, pole=pole)


def _rozmyj(x, sigma=1.5):
    r = int(math.ceil(3 * sigma))
    t = torch.arange(-r, r + 1, device=x.device, dtype=torch.float32)
    k = torch.exp(-t ** 2 / (2 * sigma ** 2))
    k = k / k.sum()
    x = F.conv2d(x[None, None], k.view(1, 1, 1, -1), padding=(0, r))
    return F.conv2d(x, k.view(1, 1, -1, 1), padding=(r, 0))[0, 0]


def mapa_z(obraz, wzorzec_w, waznosc, tol):
    """Znormalizowana dodatnia różnica tłumienia (w jednostkach szumu)."""
    m = (wzorzec_w > 0.15) & (waznosc > 0.99)
    g = (obraz[m] / wzorzec_w[m]).median() if m.sum() > 100 else torch.tensor(1.0, device=obraz.device)
    ref = wzorzec_w * g
    jasn = torch.exp(ref.clamp(max=4.0))          # szum tłumienia rośnie ~ 1/I
    e = _rozmyj(obraz - ref) / jasn
    c = 1.4826 * (e - e.median()).abs().median() + 1e-6
    reft = F.max_pool2d(ref[None, None], tol, 1, tol // 2)[0, 0] if tol > 1 else ref
    d = _rozmyj(torch.relu(obraz - reft))
    z = d / (c * jasn)
    z = torch.where(waznosc > 0.99, z, torch.zeros_like(z))
    return z, d


def _ncc(a, b, m):
    a, b = a[m], b[m]
    a, b = a - a.mean(), b - b.mean()
    return float((a * b).sum() / (a.norm() * b.norm() + 1e-9))


class Porownywacz:
    """Biblioteka wzorców w pamięci karty; wzorzec dobierany automatycznie (P8 B)."""

    def __init__(self, wariant, k=6.0, d_min=0.03, pole_min=12):
        self.p = WARIANTY[wariant]
        self.nazwa, self.k, self.d_min, self.pole_min = wariant, k, d_min, pole_min
        self.dev = karta()
        self.wz, self.miniatury, self.typy, self.tol = [], [], [], []
        self.f = None

    def naucz(self, biblioteka):
        """biblioteka: lista (ścieżka, typ). Wczytuje wzorce; dla H2n uczy mapę zmienności normalnej
        każdego wzorca z pozostałych egzemplarzy tego samego typu."""
        for sciezka, typ in biblioteka:
            a, self.f, _ = wczytaj(sciezka, self.dev, self.f)
            if self.wz:
                a = _dopasuj_rozmiar(a, self.wz[0].shape)
            self.wz.append(a)
            self.miniatury.append(F.avg_pool2d(a[None, None], 4)[0, 0])
            self.typy.append(typ)
        if self.p["nauka"]:
            for j, ref in enumerate(self.wz):
                tol = torch.zeros_like(ref)
                for i, a in enumerate(self.wz):
                    if i == j or self.typy[i] != self.typy[j]:
                        continue
                    g = wyrownaj(ref, a, self.p["skale"], self.p["lokalnie"])
                    z, _ = mapa_z(przenies(a, g), ref, przenies(torch.ones_like(a), g), self.p["tol"])
                    tol = torch.maximum(tol, z)
                self.tol.append(F.max_pool2d(tol[None, None], 5, 1, 2)[0, 0])

    def dobierz(self, a, ile):
        """Indeksy `ile` najpodobniejszych wzorców (miniatury, skala + przesunięcie, korelacja)."""
        m = F.avg_pool2d(a[None, None], 4)[0, 0]
        oceny = []
        for w in self.miniatury:
            w = _dopasuj_rozmiar(w, m.shape)
            g = wyrownaj(m, w, True, False)
            waz = przenies(torch.ones_like(w), g) > 0.99
            oceny.append(_ncc(m, przenies(w, g), waz))
        return sorted(range(len(oceny)), key=lambda i: -oceny[i])[:ile]

    def porownaj(self, obraz):
        a, f, (H, W) = wczytaj(obraz, self.dev, self.f)
        wybrane = self.dobierz(a, self.p.get("top", 1))
        z_min = d_min = None
        for j in wybrane:
            ref = _dopasuj_rozmiar(self.wz[j], a.shape)
            g = wyrownaj(a, ref, self.p["skale"], self.p["lokalnie"])
            z, d = mapa_z(a, przenies(ref, g), przenies(torch.ones_like(ref), g), self.p["tol"])
            if self.p["nauka"]:
                tol = przenies(_dopasuj_rozmiar(self.tol[j], a.shape), g)
                z = torch.where(z > 1.3 * tol, z, torch.zeros_like(z))
            z_min = z if z_min is None else torch.minimum(z_min, z)
            d_min = d if d_min is None else torch.minimum(d_min, d)
        maska = (z_min > self.k) & (d_min > self.d_min)
        maska_np = maska.cpu().numpy()  # mała maska (~2 Mpx) — tylko etykietowanie obszarów
        z_np = z_min.cpu().numpy()
        etyk, n = ndimage.label(maska_np)
        ramki = []
        if n:
            pola = np.bincount(etyk.ravel())
            for i, sl in enumerate(ndimage.find_objects(etyk), start=1):
                if sl is None or pola[i] < self.pole_min:
                    continue
                y0, y1, x0, x1 = sl[0].start, sl[0].stop, sl[1].start, sl[1].stop
                ramki.append([int(x0 * f), int(y0 * f), int(min(W, x1 * f)), int(min(H, y1 * f)),
                              round(float(z_np[sl][etyk[sl] == i].max()), 2)])
        return ramki, a, [self.typy[j] for j in wybrane]


def _dopasuj_rozmiar(x, ksztalt):
    if tuple(x.shape) == tuple(ksztalt):
        return x
    return F.interpolate(x[None, None], size=tuple(ksztalt), mode="bilinear", align_corners=False)[0, 0]
