# Scenariusz pokazu — Prześwit (DRAFT, ok. 105 s)

Podstawa: `docs/spec.md` §7.3 (ścieżka pokazu), §7.2 (ekrany). Nagrywa człowiek. Link do makiety: [link po wdrożeniu].

**Czas:** 105 s łącznie, czyli 15 s zapasu do limitu 120 s (na kliknięcia i ładowanie). Lektor czyta najwyżej ok. 2 słowa na sekundę; liczba słów w kolumnie „słowa” jest limitem dla wiersza.

**Dane na ekranie (sztuczne, §7.2):** (a) czysta naczepa — 0 zaznaczeń; (b) podwójna podłoga — 2 zaznaczenia; (c) towar w ładunku i ściana przy kabinie — 4 zaznaczenia; (d) naczepa, której typ system dobiera źle: system wybiera „plandeka”, poprawny typ to „chłodnia” (nazwy przykładowe — Programista wpisuje je w makiecie tak samo). Pasek stanu zawsze pokazuje liczbę zaznaczeń z danego obrazu. Bez zdań obiecujących skuteczność (P15–P17, P25 B).

**Zależność od P29 (teraz A):** „Zatwierdź” = sprawdzone, podejrzane — do kontroli; „Odrzuć” = pomyłka systemu, z powodem z krótkiej listy. Gdyby Artur zmienił na B (zamieniają się znaczenia przycisków), zmieniają się wiersze 4–5 (ekran i lektor) oraz okno raportu w wierszu 8.

| # | sekunda | słowa | co widać na ekranie | co mówi lektor |
|---|---|---|---|---|
| 1 | 0–10 | ≤20 | Ekran startowy: nazwa Prześwit i hasło „Zaznacza na obrazie RTG miejsca różne od wzorca.” | Operator RTG ma kilka minut na naczepę. Obecne narzędzie KAS słabo wykrywa małe ilości ukryte w konstrukcji. |
| 2 | 10–19 | ≤18 | Wczytanie obrazu (b) „naczepa_017.bmp”; pojawiają się 2 ramki i podpis „porównano z: typ chłodnia”; pasek „Przejrzano 0 z 2 miejsc” | System sam dobiera wzorzec z biblioteki i zaznacza miejsca różne od wzorca. |
| 3 | 19–26 | ≤14 | Dwa okna obok siebie: wzorzec i obraz badany, lista miejsc z boku | Wzorzec i obraz obok siebie — widać, gdzie naczepa się różni. |
| 4 | 26–38 | ≤24 | Prawa kolumna: klik w pierwsze miejsce (strefa podwójnej podłogi) → obraz przewija się → „Zatwierdź”; pasek „Przejrzano 1 z 2” | Lista idzie od wysokiego stopnia różnicy. Klikam pierwsze miejsce, w strefie podwójnej podłogi, i zatwierdzam: do kontroli. |
| 5 | 38–46 | ≤16 | Drugie miejsce → „Odrzuć” → powód z listy („cień”); pasek „Przejrzano 2 z 2” | Drugie odrzucam jako pomyłkę i wybieram powód. Decyzję o kontroli fizycznej podejmuje operator. |
| 6 | 46–58 | ≤24 | Obraz (c): 4 zaznaczenia, na liście dwie strefy: ściana przy kabinie i towar w ładunku; pasek „Przejrzano 0 z 4” | Tu są dwie różne strefy: ściana przy kabinie i towar w ładunku. Przeróbki konstrukcji i dodatki pokazujemy tak samo. |
| 7 | 58–72 | ≤28 | Obraz (d): podpis „porównano z: typ plandeka” (zły) → lista typów u góry → klik „chłodnia” → wzorzec i zaznaczenia się odświeżają | Gdy system dobierze zły wzorzec, operator zna typ z dokumentów i wybiera go z listy jednym kliknięciem. Lista jest zawsze pod ręką. |
| 8 | 72–82 | ≤20 | „Zapisz raport” → okno raportu: obraz z zaznaczeniami, decyzje, pola „miejsce kontroli” i „przedmiot kontroli” | Raport zapisuje miejsce i przedmiot kontroli, żeby kontrola fizyczna wiedziała, gdzie patrzeć. |
| 9 | 82–88 | ≤12 | Obraz (a): czysta naczepa, w tym pokazie bez zaznaczeń; pasek „0 miejsc” | Na tej czystej naczepie w pokazie nie ma zaznaczeń. |
| 10 | 88–105 | ≤34 | **SLAJD** (nie ekran makiety): wyniki pomiaru — wariant z liczbami: czyste obrazy z zaznaczeniem 7 z 20; pominięte dodatki 0 z 45, w tym podwójna podłoga 0 z 10; czas 1,1 s na obraz (cel < 1 min) | Wyniki na sztucznym zbiorze: czyste obrazy z zaznaczeniem 7 z 20, pominięte dodatki 0 z 45, czas 1,1 s na obraz. Obrazów KAS nie mamy, więc na prawdziwych danych wyniki mogą być inne. |

Łącznie: 105 s (0–105).

**Slajd 10, wariant bez liczb** (gdy pomiaru nie ma; kończy się w ok. 100 s, wiersze 1–9 bez zmian): slajd „Wyniki — po pomiarze”: cel < 1 min na obraz, liczby z pomiaru w opisie projektu. Lektor (≤ 22 słów, 88–100 s): „Wyniki liczymy na sztucznym zbiorze; podamy je z pomiaru. Obrazów KAS nie mamy, więc na prawdziwych danych wyniki mogą być inne.”

**Wersja awaryjna:** gdy makieta lub usługa nie działa, pokazujemy te same kroki na zrzutach ekranu (obrazy (a)–(d), okno raportu) i slajd 10 (w wariancie z liczbami albo bez nich, zależnie od tego, czy pomiar jest gotowy); lektor czyta ten sam tekst.
