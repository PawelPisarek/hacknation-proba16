## Product Requirements Document: Prześwit

**Author**: Projektant (zespół „próba 16”)
**Date**: 2026-11-19
**Status**: Draft (do makiety)

Źródła: `docs/zadanie.md`, `docs/pm/01-competitive-analysis.md`, `docs/pm/02-discover.md`, `docs/decyzje.md` (P4–P28). Dane są sztuczne (decyzje 11:59); obrazy w formacie .bmp; praca bez internetu (zadanie §9).

## 1. Podsumowanie
Prześwit to narzędzie dla operatora RTG KAS. Pokazuje miejsca na obrazie naczepy ciężarowej, które różnią się od wzorca, żeby operator wiedział, gdzie spojrzeć jeszcze raz. Nie rozstrzyga za operatora i nie obiecuje skuteczności (P15–P17).

## 2. Kontakty
Artur — kształt produktu; Paweł — technika, wygląd, użyteczność.

## 3. Tło
Obecne narzędzie KAS wykrywa papierosy, ale przy małych ilościach ukrytych w konstrukcji pojazdu jest za słabe (P10). Operator ma kilka minut na auto i sięga po narzędzie w trakcie oglądania obrazu (P6). Czyste zdjęcie tej samej naczepy zwykle nie istnieje (P8).

## 4. Cel
- Nie przeoczyć skrytki; ważniejsze niż uniknięcie kilku fałszywych alarmów (P4, P13). Zaznaczeń na auto ma być kilka, nie kilkadziesiąt (P13).
- Podwójna podłoga i ściana przy kabinie to najczęstsze kryjówki (P7, P12) — bez nich narzędzie nie ma sensu.
- Cel dla podwójnej podłogi: nie przeoczyć (P25 B). W tekstach bez obietnicy „żadnej” (P15); w opisie liczba z pomiaru.
- Wynik dla obrazu w mniej niż 1 min (zadanie §7).

## 5. Segment
Operator RTG KAS na granicy zewnętrznej UE. Pierwsza wersja: tylko naczepy ciężarowe (P19 A); kontenery, autokary i wagony jako dalszy krok.

## 6. Propozycja wartości
| Kto | Dlaczego | Co przed | Jak | Co po | Alternatywy |
|---|---|---|---|---|---|
| operator RTG | ma kilka minut na auto i szuka małych przeróbek | ogląda obraz bez wskazówki; narzędzie do papierosów słabe przy małych ilościach w konstrukcji | zaznaczone miejsca różne od wzorca, lista miejsc, podgląd obok siebie | wie, gdzie spojrzeć jeszcze raz, i zostawia ślad decyzji w raporcie | ręczne oglądanie; obecne narzędzie KAS do papierosów |

## 7. Rozwiązanie

### 7.1 Funkcje pierwszej wersji (P18–P22, P25, P26)
1. **Zaznaczenia różnic na obrazie** — ramki w miejscach różnych od wzorca.
2. **Dobór wzorca i wybór typu naczepy** — system dobiera wzorzec z biblioteki, podpis „porównano z: typ X”. Operator zawsze może zmienić typ naczepy z listy jednym kliknięciem (P26 B; zna typ z dokumentów przewozowych). Po zmianie wzorzec i porównanie odświeżają się.
3. **Podgląd obok siebie z suwakiem** — wzorzec i obraz w jednym oknie.
4. **Lista miejsc od najbardziej różnych** — klik skacze w miejsce.
6. **Strefy ryzyka** — oznaczone podwójna podłoga i ściana przy kabinie; kolor ramki tylko dla stref ryzyka (5 w części, P22).
7. **Zatwierdź / odrzuć** zaznaczenie jednym kliknięciem (P20 A).
8. **Raport z kontroli** — obraz z zaznaczeniami, miejsce i przedmiot kontroli, do zapisania (zadanie §3).

### 7.2 Ekrany (propozycja do makiety)
Ekran główny jest jeden, trzy strefy; dane sztuczne.
- **Góra:** nazwa Prześwit, nazwa wczytanego obrazu (np. „naczepa_017.bmp”), podpis „porównano z: typ ___”, lista wyboru typu naczepy (zmiana = 1 kliknięcie), przycisk „Zapisz raport”.
- **Środek:** obraz badany z ramkami; ramki w strefie ryzyka mają kolor wyróżniony i etykietę („podwójna podłoga”, „ściana przy kabinie”); suwak dzieli okno na wzorzec i obraz badany (przesuwany pionowy podział).
- **Prawa kolumna:** lista miejsc od najbardziej różnych (numer, strefa, stopień różnicy); każde miejsce ma przyciski „Zatwierdź” (= sprawdzone, podejrzane — do kontroli) i „Odrzuć” (= pomyłka systemu) (P29 A); „Odrzuć” wymaga powodu z krótkiej listy (np. element konstrukcji, ładunek zgodny, cień); klik w wiersz przewija obraz do miejsca.
- **Dół:** pasek stanu „Przejrzano 2 z 4 miejsc”, ostrożna informacja „Narzędzie pokazuje, gdzie obraz różni się od wzorca — tam warto spojrzeć jeszcze raz.” (P17).
- **Okno raportu:** obraz z zaznaczeniami, lista miejsc z decyzją, pola „miejsce kontroli” i „przedmiot kontroli”, przycisk zapisu (plik do pobrania).
- **Udawane dane:** 4 gotowe obrazy: (a) czysta naczepa — brak zaznaczeń; (b) naczepa z podwójną podłogą — 2 zaznaczenia, jedno w strefie ryzyka; (c) naczepa z towarem w ładunku i ścianą przy kabinie — 4 zaznaczenia; (d) naczepa, której typ system dobiera źle — pokaz wyboru typu z listy.

### 7.3 Ścieżka pokazu (nasze ograniczenie: do 2 min)
1. Wczytanie obrazu (b) → w kilka sekund zaznaczenia i podpis „porównano z”. 2. Suwak: wzorzec ↔ obraz. 3. Klik w pierwsze miejsce z listy (strefa podwójnej podłogi) → „Zatwierdź” (sprawdzone, podejrzane — do kontroli). 4. Inne miejsce → „Odrzuć” (pomyłka systemu) + powód z listy. 5. Obraz (c): ściana przy kabinie i towar w ładunku — dwie strefy na liście. 6. Obraz (d): zmiana typu naczepy z listy. 7. „Zapisz raport”. 8. Obraz (a): brak zaznaczeń.

### 7.4 Kryteria akceptacji
Definicje (P9 A): skrytka „zaznaczona”, gdy zaznaczenie choć częściowo nachodzi na skrytkę albo jego środek leży w skrytce. FP = czysty obraz z co najmniej jednym zaznaczeniem. Liczby progów nie są wpisane: wynik „n z N” podaje pomiar Programisty (krok 0P), progi po pomiarze (P11, P16).
- A1 (Z2): podwójna podłoga — kryterium przechodzi przy 0 przeoczeń w pomiarze 0P (zbiór z generatora, wg P9 A: zaznaczenie choć częściowo nachodzi na skrytkę albo środek leży w skrytce), chyba że Programista po pomiarze zapisze inny próg w `docs/decyzje.md`. Nie trzyma (więcej przeoczeń niż próg): wynik „n z N” w opisie, a na ekranie zostają strefy ryzyka bez twierdzenia o różnicy (02 §8, Z2). Cel z P25 B: nie przeoczyć, bez obietnicy „żadnej” w tekstach (P15).
- A2 (Z2b, Z2c): ściana przy kabinie i towar w ładunku — w tym samym przebiegu co A1, FN liczone osobno od konstrukcji. Próg dla każdego ustala Programista po pomiarze 0P. Nie trzyma: ściana → strefa ryzyka bez twierdzenia o różnicy; towar → ograniczenie w tekstach, FN osobno w opisie (02 §8, Z2b, Z2c).
- A3 (Z1): trafność doboru wzorca — wynik „n z N” z pomiaru; próg ustala Programista po pomiarze 0P. Nie trzyma: wybór typu naczepy z listy (A6) i tak jest dostępny zawsze; poprawiamy dobór (02 §8, Z1).
- A4 (czas): wynik dla obrazu w mniej niż 1 min. Nie trzyma: upraszczamy porównanie albo zawężamy zbiór (02 §8).
- A5 (Z5): „Zatwierdź” = 1 kliknięcie; „Odrzuć” = 2 kliknięcia (przycisk + powód z listy).
- A6 (P26 B): zmiana typu naczepy — najwyżej 1 kliknięcie; wzorzec zmienia się, porównanie odświeża się; test akceptacji MVP.
- A7 (Z6): raport zawiera miejsce i przedmiot kontroli oraz decyzję przy każdym miejscu; test akceptacji MVP.
- A8 (Z3): zaufanie — po MVP, przegląd z Arturem w roli operatora. Miary: (1) zaznaczenia zatwierdzone („sprawdzone, podejrzane — do kontroli”, P29 A), wynik „n z N”, bez procentów (02 §6); (2) liczba zaznaczeń na obraz na czystych obrazach (A10). „Kilka, nie kilkadziesiąt” (P13): do MVP robocza wartość z pomiaru 0P (Programista, A10); ostateczną liczbę ustala Artur przy przeglądzie MVP. Próg zatwierdzonych też ustala Artur. Nie trzyma: pokazujemy tylko najbardziej różne miejsca, reszta zwinięta pod listą (02 §8, Z3).
- A9 (Z4): w tekstach i na ekranie brak zdań obiecujących skuteczność (P15–P17).
- A10 (fałszywy alarm): FP = czysty obraz z co najmniej jednym zaznaczeniem; liczony na czystych obrazach i raportowany razem z FN (P4, P13). Wynik „n z N” z pomiaru Programisty (0P); próg FP po pomiarze ustala Programista (P16). Liczba zaznaczeń na auto „kilka, nie kilkadziesiąt” (P13): do MVP wartość robocza z pomiaru 0P; ostateczną ustala Artur przy przeglądzie MVP (A8).

### 7.5 Założenia i otwarte pytania
Założenia Z1–Z6 i drzewo decyzji: `docs/pm/02-discover.md`. P8 B koliduje z zadaniem §7 (01 §7 pkt 3) — założenie do pomiaru; P26 B daje wybór typu jako zapas.

## 8. Wydanie
**Pierwsza wersja:** funkcje 1–4, 6–8 z punktu 7.1, tylko naczepy.
**Poza pierwszą wersją:**
UPROSZCZENIE: kolejka wielu obrazów (9) — jeden obraz naraz — dorobienie: średnie
UPROSZCZENIE: tablica wyników jako funkcja (10) — liczby tylko w opisie i na slajdzie — dorobienie: małe
UPROSZCZENIE: kontenery, autokary, wagony — tylko naczepy — dorobienie: duże (nowy zbiór)
UPROSZCZENIE: badania z operatorami — sztuczne dane i Artur przy przeglądzie MVP — dorobienie: duże

## 9. Ryzyka
- Znaczenie „Zatwierdź” / „Odrzuć” rozstrzygnięte (P29 A); powody odrzucenia trafiają do raportu.
- **Ekran i ścieżka nie były potwierdzone przez Artura:** moment (c) (trzy warianty ekranu i wybór) pominięty na zlecenie Szefa po P28; układ z 7.2 to propozycja Projektanta. Do potwierdzenia przy przeglądzie makiety.
- Z1: dobór wzorca może zawieść; zapas — wybór typu z listy (P26 B).
- Z2 / Z2b / Z2c: przeoczenia podwójnej podłogi, ściany przy kabinie i towaru — progi po pomiarze 0P; zapas — strefy ryzyka.
- Z3: zaufanie operatora do kilku zaznaczeń; mierzone dopiero po MVP.
- Czas poniżej 1 min na obraz nie sprawdzony przed pomiarem 0P.
- Recenzja 1b zakończona po 3 rundach (P28): braki rundy 3 poprawione, bez rundy 4.
- Liczba przeoczonych podwójnych podłóg w opisie projektu czeka na pomiar.

<!-- skill: przeplywy-pm -->
<!-- skill: create-prd -->
