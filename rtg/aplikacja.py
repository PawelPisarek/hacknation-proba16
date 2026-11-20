"""Dane dla ekranu aplikacji (zadanie 01): wynik rdzenia (rtg.analiza) + obrazy do pokazania, liczone na karcie.

Przygotowanie gotowych obrazów (a)–(d) — każdy dla doboru automatycznego i dla każdego typu (A6: zmiana typu
odświeża porównanie), plus kilka innych obrazów sztucznych:
  python -m rtg.aplikacja przygotuj --dane ~/dane/proba16/male --wyjscie app/public/dane
Usługa na karcie dla wgranego .bmp (§7.6 pkt 1), na czas pokazu (POST /analiza?typ=chłodnia, ciało = plik .bmp):
  python -m rtg.aplikacja usluga --biblioteka ~/dane/proba16/male/biblioteka --port 8716

Na ekranie wzorzec jest pokazany wyrównany do badanego obrazu (ta sama siatka co w porównaniu), więc to samo
miejsce ma w obu oknach te same współrzędne (P33). Stopień i strefy bez zmian względem rdzenia (P40 A: progi 60/25).
"""
import argparse
import base64
import io
import json
import os
import tempfile
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, unquote, urlparse

import torch
from PIL import Image

from rtg.analiza import GOTOWE, NAZWY, STREFA_PODLOGA, STREFA_SCIANA, Analiza, geometria, do_wzorca
from rtg.metody import przenies

SZER = 1200  # szerokość obrazów na ekranie (px)
# dodatkowe obrazy sztuczne do wyboru w aplikacji (poza (a)–(d)); dobrane po rodzaju dodatku
INNE = ["testy/T031.bmp", "testy/T005.bmp", "testy/T020.bmp", "testy/T033.bmp", "testy/T038.bmp"]


def opis_miejsca(geo, xt, yt, strefa):
    """Krótki opis położenia (P36) z geometrii wzorca; strefa ryzyka ma pierwszeństwo."""
    if strefa:
        return strefa
    hb, wb = geo["yF"] - geo["y0"], geo["x1"] - geo["x0"]
    if xt < geo["x0"] - 0.01 * wb or xt > geo["x1"] + 0.01 * wb or yt < geo["y0"] - 0.03 * hb or yt > geo["yF"] + 0.05 * hb:
        return "poza skrzynią"
    if yt < geo["y0"] + 0.12 * hb:
        return "pod dachem"
    if xt > geo["x1"] - 0.06 * wb:
        return "przy drzwiach"
    if xt < geo["x0"] + 0.12 * wb:
        return "przy przedniej ścianie"
    return "w ładunku"


def _jpg(t, plik=None):
    """Tłumienie (rozdz. robocza) -> JPEG szerokości SZER; zwraca (bajty, skala)."""
    I = (255 * torch.exp(-t)).clamp(0, 255).byte().cpu().numpy()
    im = Image.fromarray(I, "L")
    s = min(1.0, SZER / im.width)
    if s < 1:
        im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, "JPEG", quality=82)
    if plik:
        with open(plik, "wb") as fh:
            fh.write(b.getvalue())
    return b.getvalue(), s, im.width, im.height


def wynik_ekranu(an, obraz, typ, katalog_tmp, pliki=None):
    """Raport rdzenia + miejsca w układzie ekranu + obrazy. pliki=(badany.jpg, wzorzec.jpg) zapisuje na dysk,
    inaczej obrazy jako data: URL."""
    r = an.analizuj(obraz, katalog_tmp, typ)
    j, g, ref = an.por.ostatnie
    geo = geometria(ref)
    f = an.por.f
    a = an.ostatni_obraz
    wz = przenies(ref, g)
    jb, s, w, h = _jpg(a, pliki and pliki[0])
    jw, _, _, _ = _jpg(wz, pliki and pliki[1])
    miejsca = []
    for m in r["miejsca"]:
        x0, y0, x1, y1 = [v / f for v in m["ramka"]]
        xt, yt = do_wzorca(g, (x0 + x1) / 2, (y0 + y1) / 2)
        miejsca.append(dict(m, opis=opis_miejsca(geo, xt, yt, m["strefa"]),
                            ekran=[round(x0 * s), round(y0 * s), round(x1 * s), round(y1 * s)]))
    d = {k: r[k] for k in ("obraz", "porownano_z", "typ_wybrany_przez_operatora", "wzorce", "metoda", "czas_s")}
    d.update(miejsca=miejsca, szer=w, wys=h)
    if pliki:
        d.update(badany=os.path.basename(pliki[0]), wzorzec=os.path.basename(pliki[1]))
    else:
        d.update(badany="data:image/jpeg;base64," + base64.b64encode(jb).decode(),
                 wzorzec="data:image/jpeg;base64," + base64.b64encode(jw).decode())
    return d


def przygotuj(a):
    dane = os.path.expanduser(a.dane)
    an = Analiza(os.path.join(dane, "biblioteka"))
    os.makedirs(a.wyjscie, exist_ok=True)
    tmp = tempfile.mkdtemp()
    lista = [(k, p, o) for k, (p, o) in GOTOWE.items()]
    lista.sort(key=lambda x: "bcda".index(x[0]))       # kolejność ścieżki pokazu §7.3
    lista += [(os.path.splitext(os.path.basename(p))[0], p, "obraz sztuczny z generatora") for p in INNE]
    spis = []
    for k, p, opis in lista:
        sc = os.path.join(dane, p)
        baza = os.path.splitext(os.path.basename(p))[0]
        wyniki = {}
        auto = wynik_ekranu(an, sc, None, tmp, (os.path.join(a.wyjscie, baza + "_badany.jpg"),
                                                 os.path.join(a.wyjscie, baza + "_auto.jpg")))
        wyniki["auto"] = auto
        for kod, typ in NAZWY.items():
            wyniki[typ] = wynik_ekranu(an, sc, typ, tmp, (os.path.join(a.wyjscie, baza + "_badany.jpg"),
                                                          os.path.join(a.wyjscie, f"{baza}_{kod}.jpg")))
        with open(os.path.join(a.wyjscie, baza + ".json"), "w") as fh:
            json.dump(wyniki, fh, ensure_ascii=False)
        spis.append(dict(id=k, plik=os.path.basename(p), opis=opis, json=baza + ".json"))
        print(f"{k} {p}: auto {auto['porownano_z']}, miejsc {len(auto['miejsca'])}: "
              + ", ".join(f"{m['nr']} {m['opis']} {m['stopien']}" for m in auto["miejsca"])
              + " | " + ", ".join(f"{t} {len(w['miejsca'])}" for t, w in wyniki.items() if t != "auto"), flush=True)
    with open(os.path.join(a.wyjscie, "spis.json"), "w") as fh:
        json.dump(dict(typy=list(NAZWY.values()), obrazy=spis, metoda=an.metoda,
                       policzono=time.strftime("%Y-%m-%d %H:%M"), gdzie="karta OMENa (GTX 1050)"), fh, ensure_ascii=False)


def usluga(a):
    an = Analiza(a.biblioteka)
    tmp = tempfile.mkdtemp()

    class H(BaseHTTPRequestHandler):
        def _odp(self, kod, obj):
            b = json.dumps(obj, ensure_ascii=False).encode()
            self.send_response(kod)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)

        def do_GET(self):
            self._odp(200, {"ok": True, "typy": list(NAZWY.values())})

        def do_POST(self):
            q = parse_qs(urlparse(self.path).query)
            typ = unquote(q["typ"][0]) if q.get("typ") and q["typ"][0] else None
            n = int(self.headers.get("Content-Length", 0))
            if not 0 < n < 200_000_000:
                return self._odp(400, {"blad": "pusty albo za duży plik"})
            dane = self.rfile.read(n)
            if dane[:2] != b"BM":
                return self._odp(400, {"blad": "to nie jest plik .bmp"})
            plik = os.path.join(tmp, "wgrany.bmp")
            with open(plik, "wb") as fh:
                fh.write(dane)
            try:
                self._odp(200, wynik_ekranu(an, plik, typ, tmp))
            except SystemExit as e:
                self._odp(400, {"blad": str(e)})

    print(f"usługa na karcie: port {a.port}", flush=True)
    HTTPServer(("0.0.0.0", a.port), H).serve_forever()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    p = sp.add_parser("przygotuj")
    p.add_argument("--dane", required=True)
    p.add_argument("--wyjscie", default="app/public/dane")
    u = sp.add_parser("usluga")
    u.add_argument("--biblioteka", required=True)
    u.add_argument("--port", type=int, default=8716)
    a = ap.parse_args()
    {"przygotuj": przygotuj, "usluga": usluga}[a.cmd](a)


if __name__ == "__main__":
    main()
