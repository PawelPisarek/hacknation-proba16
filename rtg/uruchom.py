"""Uruchamia kilka wariantów (hipotez) na zbiorze w jednym przebiegu i drukuje linie oceny.

python -m rtg.uruchom --dane ~/dane/proba16/male --metody H1,H1t,H2,H2n,H2k --wyjscie wyniki/male [--podglad 4]
Czas na obraz: wczytanie .bmp + dobór wzorca + porównanie (biblioteka wczytana raz, poza pomiarem — usługa).
"""
import argparse
import json
import os
import time

import torch
from PIL import Image, ImageDraw

from rtg.metody import Porownywacz
from rtg.ocena import linia, ocen, przeglad_progow


def podglad(a, ramki, prawda_ramki, f, sciezka):
    I = (255 * torch.exp(-a)).clamp(0, 255).byte().cpu().numpy()
    im = Image.fromarray(I, "L").convert("RGB")
    dr = ImageDraw.Draw(im)
    for r in prawda_ramki:
        dr.rectangle([r[0] / f - 3, r[1] / f - 3, r[2] / f + 3, r[3] / f + 3], outline=(0, 160, 0), width=2)
    for r in ramki:
        dr.rectangle([r[0] / f, r[1] / f, r[2] / f, r[3] / f], outline=(230, 0, 0), width=2)
    im.save(sciezka)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dane", required=True)
    ap.add_argument("--metody", default="H1,H1t,H2,H2n,H2k")
    ap.add_argument("--wyjscie", default="wyniki")
    ap.add_argument("--podglad", type=int, default=0, help="ile obrazów zapisać jako PNG z ramkami")
    ap.add_argument("--k", type=float, default=6.0, help="próg w jednostkach szumu")
    a = ap.parse_args()
    dane = os.path.expanduser(a.dane)
    prawda = json.load(open(os.path.join(dane, "prawda.json")))
    os.makedirs(a.wyjscie, exist_ok=True)
    print(f"karta: {torch.cuda.get_device_name(0)}; obrazy {len(prawda['obrazy'])}, biblioteka {len(prawda['biblioteka'])}",
          flush=True)
    linie = []
    for m in a.metody.split(","):
        torch.cuda.reset_peak_memory_stats()
        por = Porownywacz(m, k=a.k)
        t_n = time.time()
        por.naucz([(os.path.join(dane, b["plik"]), b["typ"]) for b in prawda["biblioteka"]])
        torch.cuda.synchronize()
        t_n = time.time() - t_n
        por.porownaj(os.path.join(dane, prawda["obrazy"][0]["plik"]))  # rozgrzewka poza pomiarem
        wyn = {"metoda": m, "obrazy": {}}
        dobor = 0
        for i, o in enumerate(prawda["obrazy"]):
            torch.cuda.synchronize()
            t = time.time()
            ramki, am, typy = por.porownaj(os.path.join(dane, o["plik"]))
            torch.cuda.synchronize()
            wyn["obrazy"][o["plik"]] = {"ramki": ramki, "czas_s": round(time.time() - t, 3), "wzorce": typy}
            dobor += typy[0] == o["typ"]
            if i < a.podglad or (a.podglad and o["rodzaj"] == "dodatki" and i < 3 * a.podglad):
                f = max(1, prawda["wysokosc"] // am.shape[0])
                podglad(am, ramki, [d["ramka"] for d in o["dodatki"]], f,
                        os.path.join(a.wyjscie, f"{m}_{os.path.basename(o['plik'])[:-4]}.png"))
        json.dump(wyn, open(os.path.join(a.wyjscie, f"{m}.json"), "w"))
        l = (linia(m, ocen(prawda, wyn)) + f" | dobór wzorca trafny {dobor}/{len(prawda['obrazy'])}"
             f" | nauka {t_n:.1f}s | karta max {torch.cuda.max_memory_allocated() / 2**20:.0f} MB")
        print(l, flush=True)
        linie.append(l)
        for p in przeglad_progow(prawda, wyn):
            print(m + p, flush=True)
            linie.append(m + p)
    open(os.path.join(a.wyjscie, "oceny.txt"), "w").write("\n".join(linie) + "\n")


if __name__ == "__main__":
    main()
