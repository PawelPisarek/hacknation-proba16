# 02 — Odkrywanie (`/discover`) — kompletny (po wyborze Artura P18–P23)

Źródła: `docs/zadanie.md`, `docs/pm/01-competitive-analysis.md`, `docs/decyzje.md` (P4–P17). Produkt nowy (nie ma użytkowników ani danych z użycia), nazwa robocza: **Prześwit** (P14).

## 1. Kontekst odkrywania (z zadania i ustaleń, bez pytań)
- **Co badamy:** narzędzie, które pokazuje operatorowi RTG miejsca różne od wzorca (zadanie §2–3).
- **Co już wiemy:** użytkownik to operator RTG KAS; ma kilka minut na auto (P6); wzorzec dobiera system (P8, P16); boli i skrytka w konstrukcji, i towar w ładunku — najczęściej podwójna podłoga albo ściana przy kabinie (P7, P12); ważniejsze nie przeoczyć niż uniknąć kilku fałszywych alarmów (P4, P13); trafienie wg P9; obecne narzędzie KAS słabe przy małych ilościach w konstrukcji (P10); wydajność i partie dopiero po pomiarze (P11); teksty ostrożnie (P15–P17).
- **Jaką decyzję ustawia odkrywanie:** co wchodzi do pierwszej działającej wersji i do pokazu (do 2 min).
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
| # | Rodzaj | Założenie | Ryzyko | Wpływ |
|---|---|---|---|---|
| Z1 | wykonalność | system trafnie dobiera wzorzec z biblioteki (P8) | W | W |
| Z2 | wykonalność | podwójną podłogę widać jako różnicę od wzorca (P7) | W | W |
| Z3 | użyteczność | przy kilku zaznaczeniach na auto operator im ufa i zdąży je obejrzeć (P13) | W | W |
| Z4 | wartość | zaznaczenia pomagają operatorowi spojrzeć jeszcze raz — nie obiecujemy skuteczności (P16, P17) | Ś | W |
| Z5 | użyteczność | jedno kliknięcie zatwierdź/odrzuć mieści się w kilku minutach na auto (P6) | Ś | Ś |
| Z6 | opłacalność | raport z miejscem i przedmiotem kontroli wystarcza do ewidencji | N | Ś |

## 5. Priorytety
Macierz wpływ × ryzyko: Z1, Z2, Z3 w prawym górnym rogu — „skok wiary”. Kolejność sprawdzania wg P23: Z1 i Z2 razem, potem Z3. Z4–Z6 po nich.

## 6. Eksperymenty
| Założenie | Eksperyment | Kryterium sukcesu (kryterium akceptacji w specu) |
|---|---|---|
| Z1 + Z2 (jeden przebieg) | prototyp na sztucznych naczepach .bmp: dla każdego obrazu system dobiera wzorzec i zaznacza różnice; porównanie z wiedzą o skrytkach | dobrany wzorzec zgodny z typem naczepy w co najmniej 9/10 obrazów (założenie); podwójna podłoga zaznaczona w co najmniej 7/10 obrazów z taką skrytką (założenie) |
| Z3 | próba na czystych i „brudnych” obrazach: ile zaznaczeń na czystym aucie, czy lista z kolejnością da się przejrzeć w kilka minut | na czystym aucie zaznaczeń nie ma lub są nieliczne (P13); lista mieści się na jednym ekranie |
| Z4 | przegląd tekstów ekranu i README pod kątem obietnic | brak zdań obiecujących skuteczność (P16, P17) |
| Z5 | przejście ścieżki pokazu ze stoperem | główna ścieżka w demo do 2 min |

Progi 9/10 i 7/10 to założenia robocze bez źródła — do potwierdzenia przy pierwszym przebiegu.

## 7. Plan odkrywania
1. Dobór wzorca + podwójna podłoga (Z1, Z2) — pierwszy przebieg na zbiorze naczep.
2. Czysta naczepa i kilka zaznaczeń (Z3).
3. Teksty ekranu (Z4) i stoper ścieżki (Z5) — po makiecie.

Brak badań z operatorami (UPROSZCZENIE z punktu 1): zastępują je sztuczne dane i ustalenia Artura.

## 8. Drzewo decyzji
- Z1 nie trzyma → ręczny wybór typu naczepy na ekranie, podpis „porównano z” zostaje.
- Z2 nie trzyma → strefy ryzyka (6) wskazują miejsce do ręcznego sprawdzenia bez twierdzenia o różnicy.
- Z3 nie trzyma → pokazujemy tylko najbardziej różne miejsca, reszta zwinięta pod listą.
- Wszystko trzyma → zakres bez zmian; następny krok: kontenery (P19).

## 9. Dalej
Wybór ekranu i ścieżki (moment c) przed `/write-prd`; eksperymenty i ryzyka wracają w `docs/spec.md` jako kryteria akceptacji.

<!-- skill: przeplywy-pm -->
<!-- skill: brainstorm-ideas-new -->
