"""Rdzeń MVP Prześwit (spec §7.6): obraz .bmp (+ opcjonalnie typ naczepy) -> PNG z ramkami + JSON.

python -m rtg.analiza --biblioteka ~/dane/proba16/male/biblioteka --obraz X.bmp [Y.bmp ...] [--typ chłodnia] --wyjscie wynik/
python -m rtg.analiza --biblioteka ~/dane/proba16/male/biblioteka --gotowe ~/dane/proba16/male --wyjscie wynik/   # 4 gotowe obrazy (a)–(d)

Metoda H2ko (krok 0P: FP 7/20, FN 0/45), liczy tylko na karcie. Biblioteka wzorców = katalog .bmp;
typ wzorca z nazwy pliku (część przed „_”), nazwy typów: NAZWY.
Strefy ryzyka (§7.6 pkt 3) z geometrii wzorca: dach, podłoga i ściana przy kabinie wykryte z profili tłumienia
wzorca; „podwójna podłoga” = pas nad podłogą, „ściana przy kabinie” = pas przy przedniej ścianie skrzyni.
Ramka należy do strefy, gdy jej środek (przeniesiony siatką wyrównania do układu wzorca) leży w strefie.
Stopień różnicy słownie (P30 A): niski / średni / wysoki z najwyższej wartości różnicy w ramce (w jednostkach szumu);
lista miejsc ułożona od wysokiego. Liczby w JSON-ie tylko jako współrzędne ramek.
"""
import argparse
import glob
import json
import os
import time

import torch
from PIL import Image, ImageDraw, ImageFont

from rtg.metody import Porownywacz

# typy generatora -> nazwy z §7.6 pkt 1 (dobór tak, by (d) dawał „plandeka” zamiast „chłodnia”, jak w demo)
NAZWY = {"N00": "kontener na podwoziu", "N01": "chłodnia", "N02": "cysterna", "N03": "skrzyniowa", "N04": "plandeka"}
KODY = {v: k for k, v in NAZWY.items()}
# progi stopnia (z ramki, jednostki szumu) z rozkładu w 0P H2ko: trafienia zwykle > 40, fałszywe ramki < 35
PROG_SREDNI, PROG_WYSOKI = 25.0, 60.0
RANGA = {"wysoki": 0, "średni": 1, "niski": 2}
STREFA_PODLOGA, STREFA_SCIANA = "podwójna podłoga", "ściana przy kabinie"
# 4 gotowe obrazy (spec §7.2) ze zbioru `male` (ziarno 16)
GOTOWE = {
    "a": ("testy/T000.bmp", "czysta naczepa"),
    "b": ("testy/T015.bmp", "podwójna podłoga (chłodnia, typ dobrany dobrze — P34)"),
    "c": ("testy/T006.bmp", "ściana przy kabinie i towar w ładunku (+ belka)"),
    "d": ("testy/T014.bmp", "zły dobór typu: system wybiera plandeka, poprawny chłodnia"),
}


def nazwa(kod):
    return NAZWY.get(kod, kod)


def stopien(z):
    return "wysoki" if z >= PROG_WYSOKI else "średni" if z >= PROG_SREDNI else "niski"


def geometria(ref):
    """Skrzynia ładunkowa wzorca (rozdz. robocza): dach y0, góra podłogi yF, ściana przy kabinie x0, drzwi x1."""
    h, w = ref.shape
    srodek = ref[:, int(0.3 * w):int(0.7 * w)].median(1).values
    wiersze = torch.nonzero(srodek > 0.15).flatten()
    y0 = int(wiersze[0]) if len(wiersze) else int(0.15 * h)
    pod = torch.nonzero(srodek[y0 + 20:] > 0.55).flatten()
    yF = y0 + 20 + int(pod[0]) if len(pod) else int(0.68 * h)
    pas = ref[max(0, y0 - 8):y0 + 9].max(0).values
    kol = torch.nonzero(pas > 0.15).flatten()
    x0, x1 = (int(kol[0]), int(kol[-1])) if len(kol) else (int(0.12 * w), int(0.95 * w))
    return dict(y0=y0, yF=yF, x0=x0, x1=x1)


def strefy(geo):
    """Strefy ryzyka w układzie wzorca [x0, y0, x1, y1] (rozdz. robocza)."""
    hb, wb = geo["yF"] - geo["y0"], geo["x1"] - geo["x0"]
    dol = geo["yF"] + 0.012 * hb
    return {STREFA_PODLOGA: [geo["x0"], geo["yF"] - 0.08 * hb, geo["x1"], dol],
            STREFA_SCIANA: [geo["x0"] - 0.005 * wb, geo["y0"], geo["x0"] + 0.06 * wb, dol]}


def do_wzorca(g, x, y):
    """Punkt obrazu (rozdz. robocza) -> punkt wzorca, przez siatkę wyrównania."""
    _, h, w, _ = g.shape
    gx, gy = g[0, min(h - 1, max(0, int(y))), min(w - 1, max(0, int(x)))].tolist()
    return (gx + 1) / 2 * w - 0.5, (gy + 1) / 2 * h - 0.5


def w_strefie(st, x, y):
    for n in (STREFA_PODLOGA, STREFA_SCIANA):
        r = st[n]
        if r[0] <= x <= r[2] and r[1] <= y <= r[3]:
            return n
    return None


class Analiza:
    def __init__(self, katalog_biblioteki, metoda="H2ko", k=6.0):
        pliki = sorted(glob.glob(os.path.join(os.path.expanduser(katalog_biblioteki), "*.bmp")))
        if not pliki:
            raise SystemExit(f"brak wzorców .bmp w {katalog_biblioteki}")
        self.por = Porownywacz(metoda, k=k)
        self.por.naucz([(p, os.path.basename(p).split("_")[0]) for p in pliki])
        self.metoda = metoda

    def typy(self):
        return sorted({nazwa(t) for t in self.por.typy})

    def analizuj(self, obraz, wyjscie, typ=None):
        """Zwraca słownik raportu; zapisuje <nazwa>.png i <nazwa>.json w katalogu wyjscie."""
        kod = None if typ is None else KODY.get(typ, typ)
        torch.cuda.synchronize()
        t = time.time()
        ramki, a, wz = self.por.porownaj(obraz, kod)
        self.ostatni_obraz = a
        j, g, ref = self.por.ostatnie
        st = strefy(geometria(ref))
        torch.cuda.synchronize()
        czas = time.time() - t
        f = self.por.f
        miejsca = []
        for r in ramki:
            cx, cy = (r[0] + r[2]) / 2 / f, (r[1] + r[3]) / 2 / f
            miejsca.append(dict(ramka=r[:4], strefa=w_strefie(st, *do_wzorca(g, cx, cy)), stopien=stopien(r[4]), _z=r[4]))
        miejsca.sort(key=lambda m: -m["_z"])  # od wysokiego; wartości z nie zapisujemy (P30 A: bez liczb)
        for i, m in enumerate(miejsca, 1):
            del m["_z"]
            m.update(nr=i, decyzja=None, powod=None)
        baza = os.path.splitext(os.path.basename(obraz))[0]
        os.makedirs(wyjscie, exist_ok=True)
        raport = {
            "obraz": os.path.basename(obraz),
            "porownano_z": nazwa(self.por.typy[j]),
            "typ_wybrany_przez_operatora": typ,
            "wzorce": [nazwa(x) for x in wz],
            "metoda": self.metoda,
            "czas_s": round(czas, 2),
            "miejsce_kontroli": None,
            "przedmiot_kontroli": None,
            "miejsca": [{k: m[k] for k in ("nr", "ramka", "strefa", "stopien", "decyzja", "powod")} for m in miejsca],
            "png": baza + ".png",
        }
        self._png(a, f, miejsca, os.path.join(wyjscie, raport["png"]))
        with open(os.path.join(wyjscie, baza + ".json"), "w") as fh:
            json.dump(raport, fh, ensure_ascii=False, indent=1)
        return raport

    @staticmethod
    def _png(a, f, miejsca, sciezka):
        """Obraz w rozdz. roboczej; ramki w strefie ryzyka czerwone z etykietą, pozostałe szare (kolor tylko dla stref, P22)."""
        I = (255 * torch.exp(-a)).clamp(0, 255).byte().cpu().numpy()
        im = Image.fromarray(I, "L").convert("RGB")
        dr = ImageDraw.Draw(im)
        try:
            fn = ImageFont.truetype("DejaVuSans-Bold.ttf", 18)
        except OSError:
            fn = ImageFont.load_default(size=18)  # Pillow >= 10.1: czcionka z polskimi znakami
        for m in miejsca:
            x0, y0, x1, y1 = [v / f for v in m["ramka"]]
            kol = (210, 0, 30) if m["strefa"] else (60, 60, 60)
            dr.rectangle([x0 - 3, y0 - 3, x1 + 3, y1 + 3], outline=kol, width=3)
            et = f"{m['nr']}" + (f" {m['strefa']}" if m["strefa"] else "")
            tw = dr.textlength(et, font=fn)
            lx, ly = min(x0 - 3, im.width - tw - 8), (y0 - 27 if y0 > 30 else y1 + 4)
            dr.rectangle([lx, ly, lx + tw + 6, ly + 23], fill=kol)
            dr.text((lx + 3, ly + 1), et, fill=(255, 255, 255), font=fn)
        im.save(sciezka)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--biblioteka", required=True, help="katalog wzorców .bmp (typ = część nazwy przed _)")
    ap.add_argument("--obraz", nargs="*", default=[])
    ap.add_argument("--gotowe", help="katalog zbioru `male`: analizuje 4 gotowe obrazy (a)–(d)")
    ap.add_argument("--typ", help="typ naczepy wybrany przez operatora (np. chłodnia); bez tego dobór automatyczny")
    ap.add_argument("--wyjscie", default="wynik")
    a = ap.parse_args()
    an = Analiza(a.biblioteka)
    obrazy = list(a.obraz)
    if a.gotowe:
        obrazy += [os.path.join(os.path.expanduser(a.gotowe), p) for p, _ in GOTOWE.values()]
    for o in obrazy:
        r = an.analizuj(o, a.wyjscie, a.typ)
        print(f"{r['obraz']}: porównano z {r['porownano_z']}; miejsc {len(r['miejsca'])}: "
              + ", ".join(f"{m['nr']} {m['strefa'] or '-'} {m['stopien']}" for m in r["miejsca"])
              + f" | {r['czas_s']} s", flush=True)


if __name__ == "__main__":
    main()
