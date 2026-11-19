"""Skrypt oceny według rozdz. 6 zadania.

FP (obrazowy) = czysty obraz z co najmniej jednym zaznaczeniem.
FN = dodatek (także przeróbka konstrukcji), którego żadne zaznaczenie nie trafiło.
Trafienie — miara główna P9 A (Artur): zaznaczenie choć częściowo nachodzi na ramkę dodatku
albo jego środek leży w ramce. Obok miara pomocnicza: IoU >= 0,1.
FN wypisywany razem i osobno: przeróbki konstrukcji (miejsce=konstrukcja) / dodatki w ładunku;
fałszywe ramki = zaznaczenia na obrazach z dodatkami, które nie trafiają żadnego dodatku.

Przewidywania (JSON): {"metoda": "...", "obrazy": {"testy/T000.bmp": {"ramki": [[x0,y0,x1,y1,wynik], ...],
                        "czas_s": 0.4}}}
Użycie: python -m rtg.ocena --prawda DANE/prawda.json --pred wyniki/H1.json
"""
import argparse
import json


def _inter(a, b):
    return max(0.0, min(a[2], b[2]) - max(a[0], b[0])) * max(0.0, min(a[3], b[3]) - max(a[1], b[1]))


def iou(a, b):
    i = _inter(a, b)
    u = (a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - i
    return i / u if u > 0 else 0.0


def p9a(p, r):
    cx, cy = (p[0] + p[2]) / 2, (p[1] + p[3]) / 2
    return _inter(p, r) > 0 or (r[0] <= cx <= r[2] and r[1] <= cy <= r[3])


TRAFIENIE = {"P9A": p9a, "IoU": lambda p, r: iou(p, r) >= 0.1}


def ocen(prawda, pred):
    obrazy = pred["obrazy"]
    czyste = [o for o in prawda["obrazy"] if o["rodzaj"] == "czysty"]
    z_dod = [o for o in prawda["obrazy"] if o["rodzaj"] == "dodatki"]
    w = {"czyste": len(czyste), "brak_pred": sum(o["plik"] not in obrazy for o in prawda["obrazy"]),
         "FP": sum(1 for o in czyste if obrazy.get(o["plik"], {}).get("ramki")),
         "dodatki": sum(len(o["dodatki"]) for o in z_dod),
         "przer": sum(d["miejsce"] == "konstrukcja" for o in z_dod for d in o["dodatki"]),
         "lad": sum(d["miejsce"] == "ladunek" for o in z_dod for d in o["dodatki"]),
         "male": sum(bool(d.get("maly")) for o in z_dod for d in o["dodatki"])}
    for nazwa, traf in TRAFIENIE.items():
        fn = {"all": 0, "przer": 0, "lad": 0, "male": 0}
        falszywe = 0
        for o in z_dod:
            ramki = [r[:4] for r in obrazy.get(o["plik"], {}).get("ramki", [])]
            for d in o["dodatki"]:
                if not any(traf(p, d["ramka"]) for p in ramki):
                    fn["all"] += 1
                    fn["przer" if d["miejsce"] == "konstrukcja" else "lad"] += 1
                    fn["male"] += bool(d.get("maly"))
            falszywe += sum(1 for p in ramki if not any(traf(p, d["ramka"]) for d in o["dodatki"]))
        w[nazwa] = dict(fn, falszywe=falszywe)
    czasy = [v.get("czas_s", 0.0) for v in obrazy.values()]
    w["czas_sr"] = sum(czasy) / len(czasy) if czasy else 0.0
    w["czas_max"] = max(czasy) if czasy else 0.0
    return w


def linia(metoda, w):
    pc = lambda a, b: f"{100.0 * a / b:.0f}%" if b else "-"
    cz = [f"OCENA {metoda}: FP={w['FP']}/{w['czyste']} ({pc(w['FP'], w['czyste'])})"]
    for n in TRAFIENIE:
        m = w[n]
        cz.append(f"FN[{n}]={m['all']}/{w['dodatki']} ({pc(m['all'], w['dodatki'])}) przeróbki {m['przer']}/{w['przer']}"
                  f" ładunek {m['lad']}/{w['lad']} małe {m['male']}/{w['male']} fałszywe_ramki {m['falszywe']}")
    cz.append(f"czas/obraz śr {w['czas_sr']:.2f}s max {w['czas_max']:.2f}s")
    if w["brak_pred"]:
        cz.append(f"BRAK predykcji: {w['brak_pred']}")
    return " | ".join(cz)


def przeglad_progow(prawda, pred, progi=(6, 10, 15, 20, 30, 40, 60)):
    """Krótkie linie FP/FN (miara P9A) przy odcięciu ramek o wyniku z poniżej progu."""
    out = []
    for p in progi:
        pr = {"obrazy": {k: dict(v, ramki=[r for r in v["ramki"] if r[4] >= p]) for k, v in pred["obrazy"].items()}}
        w = ocen(prawda, pr)
        out.append(f"  z>={p}: FP={w['FP']}/{w['czyste']} FN[P9A]={w['P9A']['all']}/{w['dodatki']} "
                   f"(przeróbki {w['P9A']['przer']}/{w['przer']}, ładunek {w['P9A']['lad']}/{w['lad']}) "
                   f"FN[IoU]={w['IoU']['all']} fałszywe {w['P9A']['falszywe']}")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--prawda", required=True)
    ap.add_argument("--pred", required=True)
    a = ap.parse_args()
    prawda, pred = json.load(open(a.prawda)), json.load(open(a.pred))
    print(linia(pred.get("metoda", a.pred), ocen(prawda, pred)))


if __name__ == "__main__":
    main()
