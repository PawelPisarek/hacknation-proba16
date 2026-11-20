"""Test akceptacji rdzenia MVP na 4 gotowych obrazach (a)–(d) + przegląd hipotez na całym zbiorze `male`.

python -m rtg.test_akceptacja --dane ~/dane/proba16/male --wyjscie wyniki/mvp [--caly]

Sprawdza (spec §7.2, §7.4 A4, A6, §7.6):
  wspólne: PNG i JSON zapisane, pola raportu, stopień ∈ {niski, średni, wysoki}, lista od wysokiego, czas < 60 s (A4)
  (a) czysta naczepa: 0 miejsc
  (b) ramka w strefie „podwójna podłoga” trafia podwójną podłogę (P9 A)
  (c) ramka w strefie „ściana przy kabinie” trafia ścianę; towar w ładunku trafiony ramką spoza stref
  (d) automatycznie: porównano z „plandeka”; operator wybiera „chłodnia” -> porównano z „chłodnia”, wszystkie wzorce
      chłodnia, wynik się odświeża (A6)
--caly — hipotezy na wszystkich 40 obrazach (jeden przebieg na karcie):
  HS: ramki trafiające podwójną podłogę / ścianę przy kabinie dostają właściwą strefę, inne dodatki — żadnej
  HT: progi stopnia rozdzielają trafienia (wysoki/średni) od fałszywych ramek (niski)
Wynik: linia „TEST AKCEPTACJI: n/N OK”.
"""
import argparse
import json
import os
from collections import Counter

from rtg.analiza import GOTOWE, RANGA, STREFA_PODLOGA, STREFA_SCIANA, Analiza
from rtg.ocena import p9a

POLA = {"obraz", "porownano_z", "typ_wybrany_przez_operatora", "wzorce", "metoda", "czas_s", "miejsce_kontroli",
        "przedmiot_kontroli", "miejsca", "png"}
POLA_M = {"nr", "ramka", "strefa", "stopien", "decyzja", "powod"}


def dodatki(prawda, plik, typ):
    o = next(o for o in prawda["obrazy"] if o["plik"] == plik)
    return [d["ramka"] for d in o["dodatki"] if d["typ"] == typ]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dane", required=True)
    ap.add_argument("--wyjscie", default="wyniki/mvp")
    ap.add_argument("--caly", action="store_true")
    a = ap.parse_args()
    dane = os.path.expanduser(a.dane)
    prawda = json.load(open(os.path.join(dane, "prawda.json")))
    an = Analiza(os.path.join(dane, "biblioteka"))
    an.analizuj(os.path.join(dane, GOTOWE["a"][0]), "/tmp/rozgrzewka")  # rozgrzewka karty poza pomiarem
    wyniki = []

    def sprawdz(nazwa, warunek):
        wyniki.append((nazwa, bool(warunek)))
        print(f"  {'OK ' if warunek else 'BŁĄD'} {nazwa}", flush=True)

    rap = {}
    for k, (plik, opis) in GOTOWE.items():
        r = an.analizuj(os.path.join(dane, plik), a.wyjscie)
        rap[k] = r
        print(f"({k}) {plik} — {opis}: porównano z {r['porownano_z']}; miejsc {len(r['miejsca'])}: "
              + ", ".join(f"{m['nr']} {m['strefa'] or '-'} {m['stopien']}" for m in r["miejsca"]) + f" | {r['czas_s']} s")
        baza = os.path.splitext(os.path.basename(plik))[0]
        sprawdz(f"({k}) PNG i JSON zapisane", os.path.exists(os.path.join(a.wyjscie, baza + ".png"))
                and json.load(open(os.path.join(a.wyjscie, baza + ".json")))["obraz"] == r["obraz"])
        sprawdz(f"({k}) pola raportu", set(r) == POLA and all(set(m) == POLA_M for m in r["miejsca"]))
        st = [RANGA.get(m["stopien"], -1) for m in r["miejsca"]]
        sprawdz(f"({k}) stopień słownie, lista od wysokiego", min(st, default=0) >= 0 and st == sorted(st))
        sprawdz(f"({k}) czas < 60 s (A4)", r["czas_s"] < 60)

    sprawdz("(a) 0 miejsc", len(rap["a"]["miejsca"]) == 0)
    pp = dodatki(prawda, GOTOWE["b"][0], "podwojna_podloga")
    sprawdz("(b) podwójna podłoga trafiona ramką w strefie „podwójna podłoga”",
            pp and all(any(m["strefa"] == STREFA_PODLOGA and p9a(m["ramka"], d) for m in rap["b"]["miejsca"]) for d in pp))
    sprawdz("(b) automatycznie porównano z „chłodnia” (P34)", rap["b"]["porownano_z"] == "chłodnia")
    sc = dodatki(prawda, GOTOWE["c"][0], "sciana_przy_kabinie")
    sprawdz("(c) ściana przy kabinie trafiona ramką w strefie „ściana przy kabinie”",
            sc and all(any(m["strefa"] == STREFA_SCIANA and p9a(m["ramka"], d) for m in rap["c"]["miejsca"]) for d in sc))
    ld = dodatki(prawda, GOTOWE["c"][0], "ladunek")
    sprawdz("(c) towar w ładunku trafiony ramką spoza stref ryzyka",
            ld and all(any(m["strefa"] is None and p9a(m["ramka"], d) for m in rap["c"]["miejsca"]) for d in ld))
    sprawdz("(d) automatycznie porównano z „plandeka”", rap["d"]["porownano_z"] == "plandeka")
    r2 = an.analizuj(os.path.join(dane, GOTOWE["d"][0]), os.path.join(a.wyjscie, "d_chlodnia"), typ="chłodnia")
    print(f"(d) po wyborze „chłodnia”: porównano z {r2['porownano_z']}, wzorce {r2['wzorce']}; miejsc {len(r2['miejsca'])}: "
          + ", ".join(f"{m['nr']} {m['strefa'] or '-'} {m['stopien']}" for m in r2["miejsca"]))
    sprawdz("(d) operator wybiera „chłodnia” -> porównano z „chłodnia”, wszystkie wzorce chłodnia (A6)",
            r2["porownano_z"] == "chłodnia" and set(r2["wzorce"]) == {"chłodnia"}
            and r2["typ_wybrany_przez_operatora"] == "chłodnia")
    pp = dodatki(prawda, GOTOWE["d"][0], "podwojna_podloga")
    sprawdz("(d) po zmianie typu podwójna podłoga w strefie „podwójna podłoga”",
            all(any(m["strefa"] == STREFA_PODLOGA and p9a(m["ramka"], d) for m in r2["miejsca"]) for d in pp))

    if a.caly:
        strefa_ok, strefa_n = Counter(), Counter()
        st_traf, st_fals = Counter(), Counter()
        for o in prawda["obrazy"]:
            r = an.analizuj(os.path.join(dane, o["plik"]), os.path.join(a.wyjscie, "caly"))
            for m in r["miejsca"]:
                traf = [d for d in o["dodatki"] if p9a(m["ramka"], d["ramka"])]
                (st_traf if traf else st_fals)[m["stopien"]] += 1
                for d in traf[:1]:
                    oczek = {"podwojna_podloga": STREFA_PODLOGA, "sciana_przy_kabinie": STREFA_SCIANA}.get(d["typ"])
                    strefa_n[d["typ"]] += 1
                    strefa_ok[d["typ"]] += m["strefa"] == oczek
        print("HS strefy (ramki trafiające dodatek: właściwa strefa / wszystkie): "
              + ", ".join(f"{t} {strefa_ok[t]}/{strefa_n[t]}" for t in sorted(strefa_n)))
        print("HT stopień: trafienia " + ", ".join(f"{s} {st_traf[s]}" for s in RANGA)
              + " | fałszywe ramki " + ", ".join(f"{s} {st_fals[s]}" for s in RANGA))

    ok = sum(w for _, w in wyniki)
    print(f"TEST AKCEPTACJI: {ok}/{len(wyniki)} OK", flush=True)
    raise SystemExit(0 if ok == len(wyniki) else 1)


if __name__ == "__main__":
    main()
