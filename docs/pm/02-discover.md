# 02 — Odkrywanie (`/discover`) — kompletny (po wyborze Artura P18–P23)

Źródła: `docs/zadanie.md`, `docs/pm/01-competitive-analysis.md`, `docs/decyzje.md` (P4–P23). Produkt nowy (nie ma użytkowników ani danych z użycia), nazwa robocza: **Prześwit** (P14).

## 1. Kontekst odkrywania (z zadania i ustaleń, bez pytań)
- **Co badamy:** narzędzie, które pokazuje operatorowi RTG miejsca różne od wzorca (zadanie §2–3).
- **Co już wiemy:** użytkownik to operator RTG KAS; ma kilka minut na auto (P6); wzorzec dobiera system (P8, P16); boli i skrytka w konstrukcji, i towar w ładunku — najczęściej podwójna podłoga albo ściana przy kabinie (P7, P12); ważniejsze nie przeoczyć niż uniknąć kilku fałszywych alarmów (P4, P13); trafienie wg P9; obecne narzędzie KAS słabe przy małych ilościach w konstrukcji (P10); wydajność i partie dopiero po pomiarze (P11); teksty ostrożnie (P15–P17).
- **Jaką decyzję ustawia odkrywanie:** co wchodzi do pierwszej działającej wersji i do pokazu. „Pokaz do 2 min” to nasze ograniczenie (cel zespołu), nie odpowiedź Artura ani wymóg zadania.
- UPROSZCZENIE: brak badań z operatorami — rozmowy z użytkownikami zastępuje wiedza Artura i opis zadania — dorobienie: rozmowy po hackathonie.

## 2. Pomysły (rozbieżna faza; produkt nowy — perspektywy: PM, projektant, inżynier)
| # | Pomysł | Perspektywa | Co daje operatorowi | Wpływ | Wysiłek |
|---|---|---|---|---|---|
| 1 | **Zaznaczenia różnic na obrazie** — ramki na obrazie badanym w miejscach różnych od wzorca | PM | od razu widać, gdzie spojrzeć jeszcze raz (rdzeń zadania §3) | W | M |
| 2 | **Dobór wzorca z zapasu wzorców i podpis „porównano z: typ X”** | PM | operator nie szuka zdjęcia czystej naczepy (P8); wie, z czym porównano | W | M |
| 3 | **Podgląd obok siebie z suwakiem** — wzorzec i obraz w jednym oknie, przesuwana granica | projektant | sprawdza zaznaczenie okiem w ułamku sekundy | W | N |
| 4 | **Lista miejsc od najbardziej różnych** — klik skacze w to miejsce | projektant | kilka minut na auto (P6): przegląd miejsc po kolei, bez błądzenia po obrazie | W | N |
| 5 | **Siła zaznaczenia** — kolor ramki zależny od tego, jak bardzo miejsce różni się od wzorca | projektant | łatwiej zdecydować, które sprawdzić najpierw | Ś | N |
| 6 | **Strefy ryzyka** — oznaczone na obrazie podwójna podłoga i ściana przy kabinie (P7) | PM | przegląd najczęstszych kryjówek najpierw | Ś | Ś |
| 7 | **„Sprawdzone / pomyłka” przy zaznaczeniu** — operator odznacza miejsca | PM | porządek pracy, ślad decyzji | Ś | Ś |
| 8 | **Raport z kontroli** — obraz z zaznaczeniami, miejsce i przedmiot kontroli, do zapisania (zadanie §9) | PM | wynik trafia do ewidencji | Ś | Ś |
| 9 | **Kolejka obrazów** — wiele naczep czeka, wynik pojawia się, gdy gotowy (zadanie §3: partie) | inżynier | skalowalność | Ś | W |
| 10 | **Tablica wyników na zbiorze testowym** — ile skrytek znaleziono, ile fałszywych alarmów na czystych, osobno konstrukcja i ładunek | inżynier | dowód skuteczności, uzasadnienie wyróżnienia (P5) | W | N |

Skróty: W = wysoki, Ś = średni, N = niski.

**Rekomendacja wyboru (3–5):** 1, 2, 3, 4, 10 — razem dają ścieżkę pokazu w 2 min: obraz → zaznaczenia → porównanie obok siebie → lista → liczby.

## 3. Wybór Artura (P18–P23)
- **P18:** pomysły 1, 2, 3, 4, 6. Strefy ryzyka (6) zamiast tablicy wyników (10); liczby z 10 trafiają do opisu, nie jako funkcja.
- **P19 A:** tylko naczepy ciężarowe; kontenery, autokary i wagony jako dalszy krok.
- **P20 A:** operator zatwierdza albo odrzuca zaznaczenie jednym kliknięciem; raport zapisuje miejsce i przedmiot kontroli. Pomysły 7 i 8 wchodzą do pierwszej wersji.
- **P21:** nic nie zmieniamy w pomysłach 1, 2, 3, 4, 6, 7.
- **P22:** pomysł 5 w części (kolor ramki tylko dla stref ryzyka); 9 odpada.
- **P23:** najryzykowniejsze założenia Z1, Z2, Z3 w tej kolejności; Z1 i Z2 sprawdzamy jednym przebiegiem.

Zakres pierwszej wersji: 1, 2, 3, 4, 6, 7, 8 + kolor ramki ze strefy ryzyka (5 w części). Poza zakresem: 9, 10 (jako funkcja).

UPROSZCZENIE: kolejka wielu obrazów (9) — jeden obraz naraz — dorobienie: średnie
UPROSZCZENIE: tablica wyników jako funkcja (10) — liczby tylko w opisie i na slajdzie — dorobienie: małe
UPROSZCZENIE: kontenery, autokary, wagony — tylko naczepy — dorobienie: duże (nowy zbiór)

## 4. Założenia (wartość, użyteczność, wykonalność, opłacalność)
Definicje (P9 A): skrytka jest „zaznaczona”, gdy zaznaczenie choć częściowo nachodzi na skrytkę albo jego środek leży w skrytce. Fałszywy alarm (FP) = czysty obraz z co najmniej jednym zaznaczeniem. Przeoczenie (FN) = skrytka bez zaznaczenia. FN liczymy razem i osobno: konstrukcja (podwójna podłoga, ściana przy kabinie, przeróbki) oraz towar w ładunku (P7, 01 §5, §7).

| # | Rodzaj | Założenie | Ryzyko | Wpływ |
|---|---|---|---|---|
| Z1 | wykonalność | system trafnie dobiera wzorzec z biblioteki (P8 B). Uwaga z 01 §7 pkt 3: P8 B koliduje z zadaniem §7 — traktujemy jako założenie do pomiaru | W | W |
| Z2 | wykonalność | podwójną podłogę widać jako różnicę od wzorca (P7) | W | W |
| Z2b | wykonalność | ścianę przy kabinie widać jako różnicę od wzorca (P7) | W | W |
| Z2c | wykonalność | towar w ładunku (dodatki) widać jako różnicę od wzorca (P7, P12) | Ś | W |
| Z3 | użyteczność | przy kilku zaznaczeniach na auto operator im ufa i zdąży je obejrzeć (P13) | W | W |
| Z4 | wartość | zaznaczenia pomagają spojrzeć jeszcze raz — nie obiecujemy skuteczności (P16, P17) | Ś | W |
| Z5 | użyteczność | zatwierdź/odrzuć jednym kliknięciem mieści się w kilku minutach na auto (P6) | Ś | Ś |
| Z6 | opłacalność | raport z miejscem i przedmiotem kontroli wystarcza do ewidencji | N | Ś |

## 5. Priorytety
Macierz wpływ × ryzyko: Z1, Z2, Z2b, Z3 w prawym górnym rogu — „skok wiary”. Kolejność wg P23: Z1 i Z2 jednym przebiegiem (Z2b i Z2c w tym samym przebiegu, bo to te same obrazy), potem Z3. Z4–Z6 po nich.

## 6. Eksperymenty
Próba (założenie robocze, do potwierdzenia z Programistą): co najmniej 30 obrazów z daną skrytką na każdy mierzony rodzaj i 30 czystych. Przy 10 obrazach ułamki typu 9/10 nie mają sensu. Wyniki podajemy jako „n z N” (np. 27 z 30), nie jako procent.

| Założenie | Eksperyment | Kryterium sukcesu (kandydat na kryterium akceptacji) |
|---|---|---|
| Z1 | dla każdego obrazu system dobiera wzorzec z biblioteki | trafny typ naczepy — próg po pomiarze (założenie) |
| Z2 | zaznaczenia na obrazach z podwójną podłogą, FN osobno | przeoczenia podwójnej podłogi — próg czeka na odpowiedź Artura (P25); do tego czasu bez liczby w specu |
| Z2b | zaznaczenia na obrazach ze ścianą przy kabinie, FN osobno | próg po pomiarze (założenie); raportowane osobno od Z2 |
| Z2c | zaznaczenia na obrazach z towarem w ładunku, FN osobno | próg po pomiarze (założenie); raportowane osobno od konstrukcji |
| czas | czas od wczytania obrazu do wyniku | poniżej 1 minuty na obraz (zadanie §7, 01 §9) |
| Z3 | czyste obrazy: liczba zaznaczeń na obraz (rozkład) + próba: operator ocenia na obrazach z kilkoma zaznaczeniami, czy zaznaczenia uznaje za pomocne i czy obejrzy wszystkie na liście | miara zaufania: odsetek zaznaczeń zatwierdzonych jako trafne lub sensowne do sprawdzenia (P20 A: kliknięcia zatwierdź/odrzuć); liczba zaznaczeń „kilka, nie kilkadziesiąt” (P13) — próg po pomiarze |
| Z4 | przegląd tekstów ekranu i README | brak zdań obiecujących skuteczność (P16, P17) |
| Z5 | przejście ścieżki pokazu ze stoperem | nasze ograniczenie: pokaz do 2 min |

Fałszywe alarmy liczymy wg P9 (czysty obraz z ≥ 1 zaznaczeniem) i raportujemy razem z FN. Żadnej liczby z tej tabeli nie przenosimy do `docs/spec.md` jako kryterium akceptacji, dopóki nie jest zmierzona albo potwierdzona przez Artura.

## 7. Plan odkrywania
1. Dobór wzorca + konstrukcja i ładunek (Z1, Z2, Z2b, Z2c) — jeden przebieg na zbiorze naczep, plus czas na obraz.
2. Czyste naczepy i kilka zaznaczeń (Z3).
3. Teksty ekranu (Z4) i stoper ścieżki (Z5) — po makiecie.

Brak badań z operatorami (UPROSZCZENIE z punktu 1): zastępują je sztuczne dane i ustalenia Artura.

## 8. Drzewo decyzji
- Z1 nie trzyma → dopracowujemy dobór wzorca (więcej wzorców w bibliotece). Ręczny wybór typu naczepy przez operatora zmieniłby P8 B — tylko za zgodą Artura (P26); do czasu odpowiedzi nie wchodzi do zakresu.
- Z2 nie trzyma → strefy ryzyka (6) wskazują miejsce do ręcznego sprawdzenia bez twierdzenia o różnicy.
- Z3 nie trzyma → pokazujemy tylko najbardziej różne miejsca, reszta zwinięta pod listą.
- Wszystko trzyma → zakres bez zmian; następny krok: kontenery (P19).

## 9. Otwarte pytania do Artura
- **P25** — dopuszczalne przeoczenia podwójnej podłogi (próg).
- **P26** — ręczny wybór typu naczepy jako zapas, gdy dobór wzorca zawiedzie.

## 10. Dalej
Wybór ekranu i ścieżki (moment c) przed `/write-prd`; eksperymenty i ryzyka wracają w `docs/spec.md` jako kryteria akceptacji (tylko zmierzone lub potwierdzone).

<!-- skill: przeplywy-pm -->
<!-- skill: brainstorm-ideas-new -->
