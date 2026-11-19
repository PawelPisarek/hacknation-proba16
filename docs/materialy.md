# Materiały zadania (krok 0)

Źródło: `docs/zadanie.md` (numery „§” = rozdziały zadania), ustalenia: `docs/decyzje.md`.

## 1. Wymagania wprost
| # | Wymaganie | § |
|---|---|---|
| W1 | Aplikacja/model autonomicznie (bez człowieka) porównuje obrazy RTG środków przewozowych, pary/grupy obrazów | 2, 3 |
| W2 | Porównanie pod kątem podobieństw i różnic (detekcja anomalii, segmentacja, porównanie pikselowe) | 3 |
| W3 | Wykrycie odstępstwa od „reguły”: wzorzec (pusty środek) vs obraz z dodatkowymi elementami | 3 |
| W4 | Raport z wykrytymi anomaliami, np. zaznaczone obszary na obrazie | 3 |
| W5 | Obsługa wejścia `*.bmp` | 3 |
| W6 | Duże pliki (~50 MB): kompresja, przetwarzanie partiami | 3, 7 |
| W7 | Skalowalność na większe zbiory w przyszłości | 3 |
| W8 | Uczenie wyłącznie na obrazach wzorcowych (prawidłowych, bez anomalii) | 5 |
| W9 | Czyste obrazy → zero zaznaczeń; alarm = false positive | 6 |
| W10 | Obrazy z „dodatkami” (nie elementy konstrukcji) → wskazać miejsce graficznie; brak = false negative | 6 |
| W11 | Czas analizy jednego obrazu < 1 min | 7 |
| W12 | Docelowo bez internetu/chmury/zewn. silnika AI (AI wolno do tworzenia kodu) | 9 |
| W13 | Dane KAS chronione: bez udostępniania/kopiowania poza hackathonem | 7 |
| W14 | Oddanie: tytuł + szczegółowy opis, repozytorium, PDF ≤ 10 slajdów | 4 |
| W15 | Wynik analizy ma mieć przypisanie do miejsca i przedmiotu kontroli (integracja z repozytorium) | 9 |
| W16 | Kontekst: istniejące narzędzie wykrywa papierosy; słabe przy małych ilościach w konstrukcji — tropy: detale, przeróbki, skrytki | 1 |

## 2. Dane wejściowe / wyjściowe
- **Wejście:** `.bmp` RTG, ~50 MB/szt.; ~200 obrazów, ~10 GB, w parach/grupach „przed/po” (§7). Źródła skanerów: Nuctech, Multicontrol (§1, §9). Wzorce do nauki dostarcza organizator (§5).
- **Wyjście:** raport z zaznaczonymi obszarami na obrazie (§3); decyzja per obraz: czysty / anomalia + lokalizacja (wynika z §6).
- **Dostęp do danych KAS:** pendrive na stoisku KAS (§7). **Nie mamy ich teraz** → własny sztuczny zbiór (decyzje 11:59).

## 3. Sprawdzanie (§6) w liczbach, które mierzymy
Zadanie nie podaje progów ani metryki lokalizacji (kryteria §8 zna Szef).
- **FP-obraz** = odsetek obrazów czystych z ≥ 1 zaznaczeniem (cel: 0 %, bo „nie zaznaczała jakichkolwiek miejsc”). Dodatkowo FP-obszary na czysty obraz.
- **FN-obraz** = odsetek obrazów z dodatkami bez żadnego zaznaczenia. Dodatkowo FN-obiekt: odsetek dodatków bez zaznaczenia w ich miejscu.
- Trafienie = zaznaczenie pokrywa dodatek (proponowane IoU ≥ 0,1 lub środek ramki w masce dodatku — do decyzji, §6 milczy).
- Czas/obraz (s), szczytowa pamięć (MB) przy 50 MB.

## 4. Ograniczenia
- < 1 min/obraz (§7); plik ~50 MB (§3, §7); działanie offline docelowo (§9); dane chronione — nie wrzucać do repo/chmury/zewn. API (§7); skalowanie partiami (§3).
- Nasze: karta GTX 1050 4 GB, liczenie tylko przez orkiestrator (SOUL).

## 5. Luki i ryzyka (z propozycją)
1. **Brak obrazów KAS (decyzje 11:59)** — sztuczny zbiór może nie oddawać szumu/artefaktów RTG. *Propozycja:* generator z szumem, gradientem, różną pozycją naczepy; przy próbie z prawdziwymi obrazami próg kalibrować na czystych.
2. **§6 bez progów i metryki trafienia** (§8 nieznane). *Propozycja:* raportować FP/FN obrazowe i obiektowe, IoU zdefiniowane w decyzjach.
3. **Wzorzec vs badany: rejestracja** — przesunięcia/skala naczepy dają fałszywe różnice (ryzyko FP). *Propozycja:* wyrównanie obrazów przed różnicą (korelacja fazowa) + tolerancja.
4. **Uczenie tylko na czystych (§5)** — brak przykładów anomalii do strojenia progu. *Propozycja:* próg z rozkładu błędu na czystych (kwantyl), dodatki tylko do walidacji.
5. **50 MB × czas < 1 min na GPU 4 GB** — pełna rozdzielczość się nie zmieści. *Propozycja:* kafelki/przetwarzanie partiami, pomiar czasu przy 50 MB.
6. **Zero FP vs wykrycie małych skrytek (§1, §6)** — sprzeczność celów; małe dodatki ginąć będą w progu. *Propozycja:* zgłosić kompromis; raportować czułość wg rozmiaru dodatku.
7. **Offline (§9) vs ewentualne modele z sieci** — pobrane wagi/zależności. *Propozycja:* wagi lokalne, brak wywołań sieciowych w czasie analizy; demo = usługa na OMENie w sieci lokalnej.
8. **Dane chronione (§7)** — przykłady w README/slajdach nie mogą zawierać obrazów KAS. *Propozycja:* pokazywać wyłącznie obrazy syntetyczne.

Nie wynika z zadania: format raportu (maska/ramki/JSON), przypisanie „miejsce i przedmiot kontroli” (W15) — metadane nieznane; *propozycja:* pole `kontrola_id` opcjonalne w raporcie.
