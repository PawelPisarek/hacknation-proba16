"""Generator sztucznego zbioru RTG naczep (.bmp, 8 bit, odcienie szarości).

Model obrazu: transmisja I = 255 * exp(-A), gdzie A to mapa tłumienia (gęstość x grubość).
Jasne = powietrze, ciemne = materiał gęsty. Każdy typ naczepy ma stałą budowę (ziarno typu),
każdy egzemplarz drobne różnice wymiarów i gęstości, każdy skan nowe przesunięcie, rozciągnięcie
wzdłuż osi jazdy, lekki obrót, wzmocnienie i szum. Deterministyczny: te same argumenty -> te same pliki.

Układ wyjścia (katalog --wyjscie):
  biblioteka/N00_0.bmp ...  czyste egzemplarze każdego typu (biblioteka wzorców; system dobiera wzorzec sam, P8 B)
  testy/T000.bmp ...        inne egzemplarze tych typów: czyste albo z dodatkami
  prawda.json               typ, rodzaj obrazu i ramki dodatków [x0, y0, x1, y1] w pikselach

Dodatki: przeróbki konstrukcji — podwójna podłoga, ściana przy kabinie (najczęstsze, P7/P12), skrytki
w belce, zbiorniku, dachu, drzwiach — oraz obce paczki w przestrzeni ładunkowej; ~40% małych.

Użycie:
  python -m rtg.generator --wyjscie ~/dane/proba16/male  --typy 5 --biblioteka 3 --czyste 4 --z-dodatkami 4
  python -m rtg.generator --wyjscie ~/dane/proba16/pelne --typy 2 --biblioteka 2 --czyste 1 --z-dodatkami 1 --wysokosc 5000
"""
import argparse
import json
import math
import os
import time

import numpy as np
from PIL import Image
from scipy import ndimage

W0, H0 = 2000, 1000  # jednostki bazowe; obraz ma rozmiar (H0*s, W0*s)


def szum_gladki(rng, h, w, ziarno_px):
    """Gładki szum 0..1 o rozmiarze (h, w) i ziarnie ~ziarno_px pikseli."""
    sh, sw = max(2, int(h / ziarno_px) + 2), max(2, int(w / ziarno_px) + 2)
    male = rng.random((sh, sw)).astype(np.float32)
    return np.asarray(Image.fromarray(male, "F").resize((max(1, w), max(1, h)), Image.BILINEAR))


class Plotno:
    """Mapa tłumienia A rysowana w jednostkach bazowych (W0 x H0), skalowana o s."""

    def __init__(self, s):
        self.s = s
        self.A = np.zeros((int(H0 * s), int(W0 * s)), np.float32)

    def _wyc(self, x0, y0, x1, y1):
        s = self.s
        H, W = self.A.shape
        c0, c1 = max(0, int(round(x0 * s))), min(W, int(round(x1 * s)))
        r0, r1 = max(0, int(round(y0 * s))), min(H, int(round(y1 * s)))
        return r0, r1, c0, c1

    def prost(self, x0, y0, x1, y1, mu, rng=None, faktura=0.0, ziarno=8.0, ksztalt="prost", paski=0.0):
        r0, r1, c0, c1 = self._wyc(x0, y0, x1, y1)
        if r1 <= r0 or c1 <= c0:
            return
        h, w = r1 - r0, c1 - c0
        m = np.full((h, w), mu, np.float32)
        if faktura and rng is not None:
            m *= 1.0 + faktura * (szum_gladki(rng, h, w, ziarno * self.s) - 0.5)
        if paski and rng is not None:
            # regularne pasy (np. kartony papierosów)
            okres = max(2.0, rng.uniform(3, 6) * self.s)
            xx = np.arange(w, dtype=np.float32)
            m *= (1.0 + paski * np.sign(np.sin(2 * math.pi * xx / okres)))[None, :]
        if ksztalt == "elipsa":
            yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
            maska = ((xx + 0.5 - w / 2) / (w / 2)) ** 2 + ((yy + 0.5 - h / 2) / (h / 2)) ** 2 <= 1.0
            m *= maska
        self.A[r0:r1, c0:c1] += m

    def kolo(self, cx, cy, r, mu, r_wew=0.0):
        r0, r1, c0, c1 = self._wyc(cx - r, cy - r, cx + r, cy + r)
        if r1 <= r0 or c1 <= c0:
            return
        s = self.s
        yy, xx = np.mgrid[r0:r1, c0:c1].astype(np.float32)
        d = np.hypot(xx / s - cx, yy / s - cy)
        self.A[r0:r1, c0:c1] += mu * ((d <= r) & (d >= r_wew))


def budowa_typu(rng):
    """Parametry typu naczepy (wspólne dla egzemplarzy), jednostki bazowe."""
    b = {}
    b["x0"], b["x1"] = rng.uniform(235, 265), rng.uniform(1870, 1930)
    b["y0"], b["y1"] = rng.uniform(130, 170), rng.uniform(680, 710)
    b["mu_sciana"] = rng.uniform(0.35, 0.5)
    b["mu_podloga"] = rng.uniform(0.7, 0.9)
    b["slupki"] = int(rng.integers(8, 15))
    b["mu_slupek"] = rng.uniform(0.18, 0.3)
    b["mu_belka"] = rng.uniform(0.9, 1.2)
    b["osie"] = int(rng.integers(2, 4))
    b["rozstaw_osi"] = rng.uniform(105, 125)
    b["zbiornik_x"] = rng.uniform(300, 360)
    b["kabina_h"] = rng.uniform(230, 280)
    return b


def egzemplarz(typ, rng):
    """Inny egzemplarz tego samego typu: drobne różnice wymiarów i gęstości (produkcja, zużycie)."""
    b = dict(typ)
    for k, d in (("x0", 2), ("x1", 3), ("y0", 2), ("y1", 2), ("zbiornik_x", 3), ("rozstaw_osi", 1.5),
                 ("kabina_h", 3)):
        b[k] = typ[k] + rng.uniform(-d, d)
    for k in ("mu_sciana", "mu_podloga", "mu_slupek", "mu_belka"):
        b[k] = typ[k] * rng.uniform(0.96, 1.04)
    return b


def rysuj_pojazd(p, b):
    x0, x1, y0, y1 = b["x0"], b["x1"], b["y0"], b["y1"]
    rng_f = np.random.default_rng(12345)  # faktury konstrukcji stałe
    # ciągnik
    p.prost(20, b["kabina_h"], 220, y1, 0.45, rng_f, 0.4, 20)
    p.prost(45, 520, 165, y1, 2.0, rng_f, 0.5, 6)
    for cx in (70, 190):
        p.kolo(cx, y1 + 95, 58, 1.1, 44)
        p.kolo(cx, y1 + 95, 24, 1.8)
    # skrzynia naczepy
    p.prost(x0, y0, x1, y0 + 4, b["mu_sciana"])          # dach
    p.prost(x0, y1 - 10, x1, y1, b["mu_podloga"])        # podłoga
    p.prost(x0, y0, x0 + 5, y1, b["mu_sciana"] * 1.5)    # ściana przy kabinie
    p.prost(x1 - 5, y0, x1, y1, b["mu_sciana"] * 1.5)    # drzwi
    for i in range(1, b["slupki"]):
        x = x0 + (x1 - x0) * i / b["slupki"]
        p.prost(x - 3, y0, x + 3, y1, b["mu_slupek"])
    # podwozie: belka, poprzeczki, zbiornik, podpora, osie
    p.prost(x0 + 20, y1, x1 - 10, y1 + 40, b["mu_belka"], rng_f, 0.15, 30)
    xx = x0 + 60
    while xx < x1 - 40:
        p.prost(xx, y1, xx + 10, y1 + 40, 0.5)
        xx += 120
    zx = b["zbiornik_x"]
    p.prost(zx, y1 + 45, zx + 120, y1 + 105, 0.7, ksztalt="elipsa")
    p.prost(460, y1 + 40, 470, y1 + 150, 1.5)
    for k in range(b["osie"]):
        cx = x1 - 140 - k * b["rozstaw_osi"]
        p.kolo(cx, y1 + 95, 58, 1.1, 44)
        p.kolo(cx, y1 + 95, 24, 1.8)


# Rodzaje dodatków i ich udział. Przeróbki konstrukcji (P7, P12 — najczęstsze): podwójna podłoga,
# ściana przy kabinie; rzadziej skrytki w belce, zbiorniku, dachu, drzwiach. W ładunku: obce paczki.
RODZAJE = (("podwojna_podloga", 0.25), ("sciana_przy_kabinie", 0.25), ("belka", 0.08), ("zbiornik", 0.05),
           ("dach", 0.04), ("drzwi", 0.03), ("ladunek", 0.30))


def rysuj_dodatek(p, rng, b):
    """Rysuje dodatek na płótnie, zwraca opis z ramką w jednostkach bazowych."""
    x0, x1, y0, y1 = b["x0"], b["x1"], b["y0"], b["y1"]
    nazwy, wagi = zip(*RODZAJE)
    typ = nazwy[int(rng.choice(len(nazwy), p=np.array(wagi) / sum(wagi)))]
    maly = bool(rng.random() < 0.4)
    tex = dict(rng=rng, faktura=0.3, ziarno=4)
    if typ == "podwojna_podloga":
        # druga blacha nad podłogą, wsporniki i zawartość w szczelinie
        dl = rng.uniform(30, 120) if maly else rng.uniform(120, 900)
        szcz = rng.uniform(6, 12) if maly else rng.uniform(10, 30)
        ax = rng.uniform(x0 + 10, x1 - 10 - dl)
        ay1 = y1 - 10
        ay0 = ay1 - szcz
        p.prost(ax, ay0 - 3, ax + dl, ay0, rng.uniform(0.25, 0.5))
        p.prost(ax, ay0, ax + dl, ay1, rng.uniform(0.1, 0.5), paski=rng.uniform(0, 0.3), **tex)
        p.prost(ax, ay0 - 3, ax + 3, ay1, 0.3)
        p.prost(ax + dl - 3, ay0 - 3, ax + dl, ay1, 0.3)
        r, miejsce = [ax, ay0 - 3, ax + dl, ay1], "konstrukcja"
    elif typ == "sciana_przy_kabinie":
        # fałszywa ściana w odstępie od prawdziwej, przestrzeń między nimi wypełniona
        odst = rng.uniform(6, 15) if maly else rng.uniform(15, 70)
        wys = rng.uniform(40, 150) if maly else rng.uniform(150, y1 - y0 - 30)
        ay0 = rng.uniform(y0 + 5, y1 - 10 - wys)
        ax = x0 + 5
        p.prost(ax + odst, ay0, ax + odst + 4, ay0 + wys, rng.uniform(0.3, 0.6))
        p.prost(ax, ay0, ax + odst, ay0 + wys, rng.uniform(0.1, 0.5), paski=rng.uniform(0, 0.3), **tex)
        r, miejsce = [ax, ay0, ax + odst + 4, ay0 + wys], "konstrukcja"
    elif typ in ("belka", "zbiornik", "dach", "drzwi"):
        if typ == "belka":
            w, h = rng.uniform(15, 140), rng.uniform(12, 32)
            ax, ay = rng.uniform(x0 + 30, x1 - 30 - w), y1 + rng.uniform(3, 38 - h)
        elif typ == "zbiornik":
            zx = b["zbiornik_x"]
            w, h = rng.uniform(15, 50), rng.uniform(12, 35)
            ax, ay = rng.uniform(zx + 20, zx + 100 - w), y1 + rng.uniform(55, 95 - h)
        elif typ == "dach":
            w, h = rng.uniform(15, 160), rng.uniform(6, 14)
            ax, ay = rng.uniform(x0 + 10, x1 - 10 - w), y0 + 2
        else:
            w, h = rng.uniform(6, 14), rng.uniform(15, 160)
            ax, ay = x1 - w - 1, rng.uniform(y0 + 10, y1 - 20 - h)
        p.prost(ax, ay, ax + w, ay + h, rng.uniform(0.25, 1.0), paski=rng.uniform(0, 0.3), **tex)
        r, miejsce = [ax, ay, ax + w, ay + h], "konstrukcja"
    else:
        lo, hi = (8, 20) if maly else ((20, 60) if rng.random() < 0.65 else (60, 150))
        w, h = rng.uniform(lo, hi), rng.uniform(lo, hi)
        ax, ay = rng.uniform(x0 + 15, x1 - 15 - w), rng.uniform(y0 + 15, y1 - 15 - h)
        mu = rng.uniform(0.2, 1.0) if rng.random() < 0.85 else rng.uniform(1.5, 3.0)
        p.prost(ax, ay, ax + w, ay + h, mu, ksztalt="elipsa" if rng.random() < 0.3 else "prost",
                paski=rng.uniform(0, 0.4), **tex)
        r, miejsce = [ax, ay, ax + w, ay + h], "ladunek"
    return dict(ramka=r, typ=typ, miejsce=miejsce, maly=maly)


def skanuj(A, rng, s, sigma_szumu=3.0):
    """Symuluje przejazd przez skaner: przekształcenie afiniczne, wzmocnienie, szum.
    Zwraca (obraz uint8, funkcja mapująca punkty (x, y) płótna -> obraz)."""
    H, W = A.shape
    sx = rng.uniform(0.97, 1.03)      # prędkość przejazdu
    sy = rng.uniform(0.995, 1.005)
    th = math.radians(rng.uniform(-0.25, 0.25))
    tx = rng.uniform(-0.03, 0.03) * W
    ty = rng.uniform(-0.02, 0.02) * H
    c, si = math.cos(th), math.sin(th)
    # wyjście (y, x) = F @ (y, x)_płótna + t, środek obrotu w środku obrazu
    F = np.array([[sy * c, sy * si], [-sx * si, sx * c]])
    ctr = np.array([H / 2, W / 2])
    t = ctr - F @ ctr + np.array([ty, tx])
    Finv = np.linalg.inv(F)
    A2 = ndimage.affine_transform(A, Finv, offset=-Finv @ t, order=1, mode="constant", cval=0.0,
                                  output=np.float32)
    A2 = ndimage.gaussian_filter(A2, 0.6 * s)  # rozmycie detektora
    A2 *= rng.uniform(0.93, 1.07)              # energia źródła
    I = 255.0 * np.exp(-A2)
    I *= (1 + 0.012 * (rng.random(W, dtype=np.float32) - 0.5))[None, :]  # migotanie impulsów
    I *= (1 + 0.010 * (rng.random(H, dtype=np.float32) - 0.5))[:, None]  # czułość wierszy detektora
    I += rng.normal(0, sigma_szumu, size=I.shape).astype(np.float32)
    I = np.clip(I, 0, 255).astype(np.uint8)

    def mapuj(x, y):
        yy, xx = F @ np.array([y, x]) + t
        return float(xx), float(yy)

    return I, mapuj


def ramka_po_skanie(ramka_baz, s, mapuj, W, H):
    x0, y0, x1, y1 = [v * s for v in ramka_baz]
    pts = [mapuj(x, y) for x, y in ((x0, y0), (x1, y0), (x0, y1), (x1, y1))]
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    return [max(0, int(math.floor(min(xs)))), max(0, int(math.floor(min(ys)))),
            min(W, int(math.ceil(max(xs)))), min(H, int(math.ceil(max(ys))))]


def generuj(wyj, typy, biblioteka, czyste, z_dodatkami, wysokosc, ziarno):
    s = wysokosc / H0
    for d in ("biblioteka", "testy"):
        os.makedirs(os.path.join(wyj, d), exist_ok=True)
    prawda = {"ziarno": ziarno, "wysokosc": wysokosc, "szerokosc": int(W0 * s), "biblioteka": [], "obrazy": []}
    nr = 0
    for ti in range(typy):
        typ = budowa_typu(np.random.default_rng([ziarno, ti]))
        tid = f"N{ti:02d}"
        plan = [("biblioteka", i) for i in range(biblioteka)] + [("czysty", i) for i in range(czyste)] \
            + [("dodatki", i) for i in range(z_dodatkami)]
        for k, (rodzaj, i) in enumerate(plan):
            rng = np.random.default_rng([ziarno, ti, k])
            b = egzemplarz(typ, rng)
            p = Plotno(s)
            rysuj_pojazd(p, b)
            n_dod = int(rng.integers(1, 4)) if rodzaj == "dodatki" else 0
            dodatki = [rysuj_dodatek(p, rng, b) for _ in range(n_dod)]
            I, mapuj = skanuj(p.A, rng, s)
            H, W = I.shape
            if rodzaj == "biblioteka":
                sciezka = f"biblioteka/{tid}_{i}.bmp"
                prawda["biblioteka"].append({"plik": sciezka, "typ": tid})
            else:
                sciezka = f"testy/T{nr:03d}.bmp"
                nr += 1
                prawda["obrazy"].append({"plik": sciezka, "typ": tid, "rodzaj": rodzaj, "dodatki": [
                    dict(d, ramka=ramka_po_skanie(d["ramka"], s, mapuj, W, H)) for d in dodatki]})
            Image.fromarray(I, "L").save(os.path.join(wyj, sciezka))
    with open(os.path.join(wyj, "prawda.json"), "w") as f:
        json.dump(prawda, f, indent=1, ensure_ascii=False)
    return prawda


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--wyjscie", required=True)
    ap.add_argument("--typy", type=int, default=5, help="typów naczep")
    ap.add_argument("--biblioteka", type=int, default=3, help="czystych egzemplarzy wzorcowych na typ")
    ap.add_argument("--czyste", type=int, default=4, help="czystych testów na typ")
    ap.add_argument("--z-dodatkami", type=int, default=4, help="testów z dodatkami na typ")
    ap.add_argument("--wysokosc", type=int, default=1000, help="5000 -> 10000x5000 px = ~50 MB")
    ap.add_argument("--ziarno", type=int, default=16)
    a = ap.parse_args()
    t = time.time()
    pr = generuj(os.path.expanduser(a.wyjscie), a.typy, a.biblioteka, a.czyste, a.z_dodatkami, a.wysokosc, a.ziarno)
    dod = [d for o in pr["obrazy"] for d in o["dodatki"]]
    print(f"GENERATOR {a.wyjscie}: typy={a.typy} biblioteka={len(pr['biblioteka'])} testy={len(pr['obrazy'])} "
          f"dodatki={len(dod)} (konstrukcja {sum(d['miejsce'] == 'konstrukcja' for d in dod)}, "
          f"małe {sum(d['maly'] for d in dod)}) rozmiar={pr['szerokosc']}x{pr['wysokosc']} czas={time.time() - t:.1f}s")


if __name__ == "__main__":
    main()
