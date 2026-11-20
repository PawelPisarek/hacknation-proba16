# Uruchomienie (Programista)

Kod: `rtg/` (Python 3.12, `requirements.txt`). Metody liczą wyłącznie na karcie (CUDA); bez karty kończą się komunikatem.

```sh
pip install -r requirements.txt
# 1. dane sztuczne (deterministyczne, ziarno 16)
python -m rtg.generator --wyjscie ~/dane/proba16/male                       # 5 typów × (3 wzorce + 4 czyste + 4 z dodatkami), 2000×1000
python -m rtg.generator --wyjscie ~/dane/proba16/pelne --typy 2 --biblioteka 2 --czyste 1 --z-dodatkami 1 --wysokosc 5000   # 10000×5000 = 50 MB
# 2. porównanie z biblioteką + ocena (kilka hipotez w jednym przebiegu)
python -m rtg.uruchom --dane ~/dane/proba16/male --metody H1,H1t,H2,H2n,H2k --wyjscie wyniki/male --podglad 4
# 3. sama ocena gotowych przewidywań
python -m rtg.ocena --prawda ~/dane/proba16/male/prawda.json --pred wyniki/male/H2.json
```

Format przewidywań i zasady liczenia FP/FN: nagłówek `rtg/ocena.py`. Ramki prawdy: `prawda.json` (`[x0, y0, x1, y1]` w pikselach,
`miejsce`: `konstrukcja` = przeróbka/skrytka, `ladunek`; `maly`).

Na zespołowej flocie: przez orkiestrator (`--klasa gpu-tlo` dla `rtg.uruchom`, `--maszyna dowolna` dla generatora).

## Rdzeń MVP: .bmp → PNG z ramkami + JSON (spec §7.6)

```sh
# jeden obraz, typ dobierany automatycznie (albo --typ chłodnia = wybór operatora, P26 B)
python -m rtg.analiza --biblioteka ~/dane/proba16/male/biblioteka --obraz ~/dane/proba16/male/testy/T031.bmp --wyjscie wynik/
# 4 gotowe obrazy (a)–(d) ze spec §7.2
python -m rtg.analiza --biblioteka ~/dane/proba16/male/biblioteka --gotowe ~/dane/proba16/male --wyjscie wynik/
# test akceptacji (23 sprawdzenia; --caly dodaje przegląd stref i stopni na 40 obrazach)
python -m rtg.test_akceptacja --dane ~/dane/proba16/male --wyjscie wyniki/mvp
```
JSON: `obraz`, `porownano_z`, `typ_wybrany_przez_operatora`, `wzorce`, `metoda`, `czas_s`, `miejsce_kontroli`, `przedmiot_kontroli`,
`miejsca[]` (`nr`, `ramka` [x0,y0,x1,y1] px, `strefa` „podwójna podłoga” / „ściana przy kabinie” / null, `stopien` niski/średni/wysoki,
`decyzja`, `powod`), `png`. Lista od wysokiego stopnia. Gotowe: (a) T000, (b) T031, (c) T006, (d) T014 — `rtg/analiza.py` `GOTOWE`.
Na flocie: `--klasa gpu-tlo` (karta). Wyniki z karty: `wyniki/mvp/` (zgl-4693).
