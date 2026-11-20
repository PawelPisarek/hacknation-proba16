# Odbiór MVP — wynik (16:43, produkcja https://hacknation.ksefbot.pl/)

Metoda: kod produkcyjny `app.js` ma sumę md5 identyczną z `app/public/app.js` w repo (66426c54; `r.css` też; `index.html` różni się tylko skryptem wstrzykniętym przez Cloudflare); `node app/test.mjs` → **TEST EKRANU: 14/14 OK**; `curl` na `dane/*.json` z produkcji; zrzuty z `docs/zrzuty/` (oglądałem `mvp-ksefbot.png` i `mvp-p38-ostrzezenie.png`, resztę tylko po istnieniu pliku). Przeglądarki nie mam — pobrań plików z ekranu nie wykonałem. Karty OMENa nie uruchamiałem.

**Wynik: 26 przechodzi / 0 nie przechodzi / 3 nie da się sprawdzić / 1 w toku.** HTTP: `curl` → 200 (strona, `dane/spis.json`).

| # | wynik | dowód |
|---|---|---|
| 1, 2 | przechodzi | test: samo „Odrzuć” nie zapisuje, bez powodu nie odrzuca; zrzuty `mvp-p29-*.png` (istnieją); w `mvp-ksefbot.png` miejsce 1 „✓ Zatwierdzone”, pasek 1 z 2 |
| 3 | przechodzi | test P30 (9 obrazów × 6 wyników: stopień słownie, od wysokiego, opisy bez liczb); JSON z produkcji: T015 wysoki/wysoki |
| 4 | przechodzi | `mvp-ksefbot.png`: wzorzec lewo, badany prawo z ramkami, lista z boku. Wspólnego przewijania nie widać na zrzucie (obrazy mieszczą się w oknie) |
| 5 | przechodzi | test: lista powodów = A7 (4 pozycje); `mvp-p32-po.png` istnieje |
| 6 | przechodzi | `mvp-ksefbot.png`: w oknie wzorca przerywana ramka miejsca wybranego |
| 7 | przechodzi | test P34/A6; JSON: T015 → „chłodnia”, T014 → „plandeka” |
| 8 | **nie da się sprawdzić (PNG)** | JSON: test `zestawienie()` ma miejsce, przedmiot, „dane sztuczne”, ramkę, decyzję, powód; okno raportu na `mvp-p38-ostrzezenie.png` ma „(dane sztuczne)”; pobrany PNG i plik JSON nieotwarte |
| 9 | przechodzi | `mvp-ksefbot.png`: numer + opis przy każdym miejscu (ramka wzorca i badanego) |
| 10 | przechodzi | `grep -rniE "WZORZEC:|skuteczn|żadn" app/public/app.js index.html` → 0 trafień (nagłówek „WZORZEC —” bez dwukropka); na pasku tylko „Przejrzano 1 z 2”. Zrzutu `mvp-p37-ekran.png` brak |
| 11 | przechodzi | `mvp-p38-ostrzezenie.png`: „Nieprzejrzane: 1 miejsce. Zapisać mimo to?”, „Zapisz mimo to”, „Wróć”; test odmiany OK |
| 12 | przechodzi (kod+test, nie pobrany plik) | test: miejsce bez decyzji → `decyzja: "nieprzejrzane"`, `powod: null`; ten sam kod na produkcji (md5). Pobranego pliku nie otwierałem |
| 13 | przechodzi | test: po decyzjach przy wszystkich `nieprzejrzane()`=0 → `zapisz()` idzie wprost do `pobierz()` |
| 14, 15 | przechodzi | `wyniki/0P/README.md`: H2ko FN 0/45 (P9A); osobno wg rodzaju: podłoga 0/10, ściana 0/15, ładunek 0/9 |
| 16 | **nie da się sprawdzić** | dobór trafny 37/40 (README), progu trafności nie znalazłem w `decyzje.md` |
| 17 | przechodzi dla (a)–(d) | czas karty z JSON: T015 1,63 s, T006 1,11 s, T014 1,11 s, T000 1,1 s (< 60 s); gotowe obrazy są wczytywane z plików. Wgrany .bmp — patrz 26 |
| 18, 19 | przechodzi | kod: Zatwierdź = 1 klik, Odrzuć + powód = 2; `zmienTyp` = 1 wybór, test A6 OK; zrzuty `mvp-a6-przed/po.png` istnieją; zrzutu `mvp-a5-*` brak |
| 20 | przechodzi | test P35/A7 (patrz 8, JSON) |
| 21 | nie da się sprawdzić | wymaga Artura (A8), nie na noc |
| 22 | przechodzi | grep jak w 10 |
| 23 | przechodzi | README: H2ko FP 7/20, FN 0/45; próg „FN=0, FP ≤ 7/20” wg wpisu Szefa 16:01 |
| 24 | przechodzi | JSON T000: 0 miejsc; `mvp-a-czysta.png` istnieje |
| 25 | przechodzi wg aktualnego specu | JSON T006: **3** miejsca (towar, ściana przy kabinie, „poza skrzynią”), nie 4; spec poprawiony w 8ed053b (§7.2 (c) 3 miejsca) |
| 26 | **w toku** | na produkcji `/api/stan` → `{"wgrywanie":true}` (pole wgrywania widoczne), ale `POST /api/analiza` → **503** (kod: „karta OMENa nie odpowiada”); P41 czeka na Pawła |
| 27 | przechodzi | `mvp-ksefbot.png`: „podwójna podłoga” w kolorze strefy, ściana przy kabinie też w kolorze (ma strefę); JSON T015: strefa „podwójna podłoga”. Zrzutu `mvp-b-strefa.png` brak |
| 28, 29 | przechodzi | `curl` strona 200, `dane/spis.json` 200; dane: 9 obrazów sztucznych, wgrywanie z produkcji tylko przez kartę (P41) |
| 30 | przechodzi (JSON) | JSON z produkcji: (b) 2, (c) 3, (a) 0 miejsc; PNG z rdzenia niesprawdzony; test rdzenia 24/24 wg Programisty (nie powtarzałem — karta) |

## Braki (bez pochwał)

1. **technika** — wiersz 26: pole „wgraj .bmp” jest widoczne na produkcji, a `POST /api/analiza` daje 503; operator zobaczy błąd. Do rozstrzygnięcia z P41 (ukryć pole albo otworzyć drogę do OMENa).
2. **technika** — brak pobranego przez przeglądarkę raportu (JSON + PNG) z produkcji: wiersze 8, 12 oparte na kodzie i teście w node, nie na pliku. Ktoś z przeglądarką (Programista) powinien pobrać jedną parę i wkleić `grep nieprzejrzane`.
3. **technika** — zrzutów `mvp-p37-ekran`, `mvp-a5-*`, `mvp-b-strefa` z listy dowodów nie ma; dowody zastępcze (grep, kod, `mvp-ksefbot.png`).
4. **technika** — brak progu trafności doboru (A3, 37/40) w `decyzje.md` (wiersz 16).
5. **produkt** — FP 7/20 czystych obrazów dostaje zaznaczenie (A10); próg „≤ 7/20” to pomiar, nie cel — decyzja Artura po MVP razem z A8.

<!-- skill: brak -->
