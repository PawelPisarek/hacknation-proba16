# 02 — Odkrywanie (`/discover`) — kompletny (po wyborze Artura P18–P23)

Źródła: `docs/zadanie.md`, `docs/pm/01-competitive-analysis.md`, `docs/decyzje.md` (P4–P23). Produkt nowy (nie ma użytkowników ani danych z użycia), nazwa robocza: **Prześwit** (P14).

## 1. Kontekst odkrywania (z zadania i ustaleń, bez pytań)
- **Co badamy:** narzędzie, które pokazuje operatorowi RTG miejsca różne od wzorca (zadanie §2–3).
- **Co już wiemy:** użytkownik to operator RTG KAS; ma kilka minut na auto (P6); wzorzec dobiera system, a gdy dobierze źle, operator wybiera typ naczepy z listy jednym kliknięciem — zawsze dostępne jako zapas (P8, P26 B, P16); boli i skrytka w konstrukcji, i towar w ładunku — najczęściej podwójna podłoga albo ściana przy kabinie (P7, P12); ważniejsze nie przeoczyć niż uniknąć kilku fałszywych alarmów (P4, P13); trafienie wg P9; obecne narzędzie KAS słabe przy małych ilościach w konstrukcji (P10); wydajność i partie dopiero po pomiarze (P11); teksty ostrożnie (P15–P17).
- **Jaką decyzję ustawia odkrywanie:** co wchodzi do pierwszej działającej wersji i do pokazu. „Pokaz do 2 min” to nasze ograniczenie (cel zespołu), nie odpowiedź Artura ani wymóg zadania.
- UPROSZCZENIE: brak badań z operatorami — rozmowy z użytkownikami zastępuje wiedza Artura i opis zadania — dorobienie: rozmowy po hackathonie.

## 2. Pomysły (rozbieżna faza; produkt nowy — perspektywy: PM, projektant, inżynier)
| # | Pomysł | Perspektywa | Co daje operatorowi | Wpływ | Wysiłek |
|---|---|---|---|---|---|
| 1 | **Zaznaczenia różnic na obrazie** — ramki na obrazie badanym w miejscach różnych od wzorca | PM | od razu widać, gdzie spojrzeć jeszcze raz (rdzeń zadania §3) | W | M |
| 2 | **Dobór wzorca z zapasu wzorców, podpis „porównano z: typ X” i wybór typu naczepy z listy jednym kliknięciem** (zawsze dostępny jako zapas, P26 B) | PM | operator nie szuka zdjęcia czystej naczepy (P8); wie, z czym porównano; gdy system pomyli typ, poprawia go jednym kliknięciem | W | M |
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

## 3. Wybór Artura (P18–P26)
- **P18:** pomysły 1, 2, 3, 4, 6. Strefy ryzyka (6) zamiast tablicy wyników (10); liczby z 10 trafiają do opisu, nie jako funkcja.
- **P19 A:** tylko naczepy ciężarowe; kontenery, autokary i wagony jako dalszy krok.
- **P20 A:** operator zatwierdza albo odrzuca zaznaczenie jednym kliknięciem; raport zapisuje miejsce i przedmiot kontroli. Pomysły 7 i 8 wchodzą do pierwszej wersji.
- **P21:** nic nie zmieniamy w pomysłach 1, 2, 3, 4, 6, 7.
- **P22:** pomysł 5 w części (kolor ramki tylko dla stref ryzyka); 9 odpada.
- **P23:** najryzykowniejsze założenia Z1, Z2, Z3 w tej kolejności; Z1 i Z2 sprawdzamy jednym przebiegiem.

Zakres pierwszej wersji: 1, 2 (z wyborem typu naczepy z listy jako stałym zapasem, P26 B), 3, 4, 6, 7, 8 + kolor ramki ze strefy ryzyka (5 w części). Poza zakresem: 9, 10 (jako funkcja).

UPROSZCZENIE: kolejka wielu obrazów (9) — jeden obraz naraz — dorobienie: średnie
UPROSZCZENIE: tablica wyników jako funkcja (10) — liczby tylko w opisie i na slajdzie — dorobienie: małe
UPROSZCZENIE: kontenery, autokary, wagony — tylko naczepy — dorobienie: duże (nowy zbiór)

## 3b. Dalsze odpowiedzi Artura (P25, P26)
- **P25 B:** celem jest nie przeoczyć podwójnej podłogi, ale bez obietnicy „żadnej” w tekstach (P15). Cel zapisujemy w specu bez liczby; w opisie podajemy liczbę z pomiaru.
- **P26 B:** operator zna typ naczepy z dokumentów przewozowych; gdy system dobierze wzorzec źle, wybiera typ z listy jednym kliknięciem. Wybór jest dostępny zawsze jako zapas (nie dopiero po „Z1 nie trzyma”). To zmienia P8 B — za zgodą Artura.

## 4. Założenia (wartość, użyteczność, wykonalność, opłacalność)
Definicje (P9 A): skrytka jest „zaznaczona”, gdy zaznaczenie choć częściowo nachodzi na skrytkę albo jego środek leży w skrytce. Fałszywy alarm (FP) = czysty obraz z co najmniej jednym zaznaczeniem. Przeoczenie (FN) = skrytka bez zaznaczenia. FN liczymy razem i osobno: konstrukcja (podwójna podłoga, ściana przy kabinie, przeróbki) oraz towar w ładunku (P7, 01 §5, §7).

| # | Rodzaj | Założenie | Ryzyko | Wpływ |
|---|---|---|---|---|
| Z1 | wykonalność | system trafnie dobiera wzorzec z biblioteki (P8 B). Uwaga z 01 §7 pkt 3: P8 B koliduje z zadaniem §7 — założenie do pomiaru | W | W |
| Z2 | wykonalność | podwójną podłogę widać jako różnicę od wzorca (P7) | W | W |
| Z2b | wykonalność | ścianę przy kabinie widać jako różnicę od wzorca (P7) — sprawdzane w przebiegu Z2, poza „skokiem wiary” | Ś | W |
| Z2c | wykonalność | towar w ładunku widać jako różnicę od wzorca (P7, P12) — sprawdzane w przebiegu Z2, poza „skokiem wiary” | Ś | W |
| Z3 | użyteczność | przy kilku zaznaczeniach na auto operator im ufa i zdąży je obejrzeć (P13) | W | W |
| Z4 | wartość | zaznaczenia pomagają spojrzeć jeszcze raz — nie obiecujemy skuteczności (P16, P17) | Ś | W |
| Z5 | użyteczność | obsługa zaznaczeń jest szybka: najwyżej 1 kliknięcie na zaznaczenie (P20 A), wynik w mniej niż 1 min na obraz (zadanie §7, 01 §9) | Ś | Ś |
| Z6 | opłacalność | raport zawiera miejsce i przedmiot kontroli (P20 A) | N | Ś |

## 5. Priorytety
Macierz wpływ × ryzyko. „Skok wiary” zgodnie z P23: tylko Z1, Z2, Z3. Z2b i Z2c mają wpływ wysoki, ale nie wchodzą do „skoku wiary” — sprawdzamy je w tym samym przebiegu co Z2. Kolejność wg P23: Z1 i Z2 jednym przebiegiem (z Z2b, Z2c i czasem na obraz), potem Z3. Z4–Z6 po nich.

## 6. Eksperymenty
**Próba:** zbiór z generatora Programisty (krok 0P). Liczby obrazów i wyniki „n z N” pochodzą z jego pomiaru; nie zakładamy własnej liczby. Gdy N jest małe, podajemy je wprost i nie przeliczamy na procenty.

| Założenie | Eksperyment | Kryterium sukcesu (kandydat na kryterium akceptacji) |
|---|---|---|
| Z1 | pomiar doboru wzorca na zbiorze z generatora | trafny typ naczepy — wynik „n z N” z pomiaru Programisty; próg po pomiarze |
| Z2 | zaznaczenia na obrazach z podwójną podłogą, FN osobno (P9 A) | cel: nie przeoczyć (P25 B); w specu bez liczby, liczba z pomiaru w opisie |
| Z2b | ten sam przebieg: obrazy ze ścianą przy kabinie, FN osobno | wynik „n z N”; raportowane osobno od Z2 |
| Z2c | ten sam przebieg: obrazy z towarem w ładunku, FN osobno | wynik „n z N”; raportowane osobno od konstrukcji |
| czas (Z5) | czas od wczytania obrazu do wyniku, w tym samym przebiegu | mniej niż 1 min na obraz |
| Z3 | dopiero po makiecie / MVP: czyste obrazy — rozkład liczby zaznaczeń na obraz; przegląd MVP, w którym operatora zastępuje Artur i klika zatwierdź/odrzuć (P20 A) | miara zaufania: odsetek zaznaczeń zatwierdzonych przez Artura; liczba zaznaczeń „kilka, nie kilkadziesiąt” (P13); próg po pomiarze |
| Z4 | przegląd tekstów ekranu i README | brak zdań obiecujących skuteczność (P15, P16, P17) |
| Z5 (kliknięcia) | przejście w MVP: obsługa zaznaczenia | najwyżej 1 kliknięcie na zaznaczenie |
| Z6 | test akceptacji MVP: otwarcie raportu po zatwierdzeniu | raport zawiera miejsce i przedmiot kontroli |
| wybór typu naczepy (P26 B) | test akceptacji MVP: operator zmienia typ naczepy na liście | najwyżej 1 kliknięcie; wzorzec się zmienia i porównanie odświeża się |

„Pokaz do 2 min” to nasze ograniczenie na demo, nie kryterium tych założeń. Żadnej liczby z tej tabeli nie przenosimy do `docs/spec.md` jako kryterium akceptacji, dopóki nie jest zmierzona albo potwierdzona przez Artura.

## 7. Plan odkrywania
1. Przed makietą: jeden przebieg na zbiorze z generatora — dobór wzorca, podwójna podłoga, ściana przy kabinie, towar w ładunku, czas na obraz (Z1, Z2, Z2b, Z2c, czas).
2. Po makiecie / MVP: przegląd z Arturem (Z3, kliknięcia Z5), test akceptacji raportu (Z6), przegląd tekstów (Z4).

Brak badań z operatorami (UPROSZCZENIE z punktu 1): zastępują je sztuczne dane i Artur przy przeglądzie MVP.

## 8. Drzewo decyzji
- Z1 nie trzyma (wzorzec źle dobrany w pomiarze Programisty 0P; próg ustala Programista po pomiarze 0P) → wybór typu naczepy z listy (P26 B) i tak jest zawsze dostępny; poprawiamy dobór (więcej wzorców w bibliotece), podpis „porównano z” zostaje.
- Z2 nie trzyma (przeoczone podwójne podłogi; próg ustala Programista po pomiarze 0P) → strefy ryzyka (6) wskazują miejsce do ręcznego sprawdzenia bez twierdzenia o różnicy.
- Z2b nie trzyma (próg ustala Programista po pomiarze 0P) → ściana przy kabinie jako strefa ryzyka (6) bez twierdzenia o różnicy; wynik raportujemy osobno.
- Z2c nie trzyma (próg ustala Programista po pomiarze 0P) → towar w ładunku zapowiadamy jako ograniczenie w tekstach; FN osobno w opisie.
- Czas ≥ 1 min na obraz → upraszczamy porównanie (mniejsza rozdzielczość podglądu) albo zawężamy zbiór; wynik w opisie.
- Z3 nie trzyma (niski odsetek zatwierdzonych; próg ustala Artur przy przeglądzie MVP) → pokazujemy tylko najbardziej różne miejsca, reszta zwinięta pod listą.
- Wszystko trzyma → zakres bez zmian; następny krok: kontenery (P19).

## 9. Otwarte pytania do Artura
Brak — P25 i P26 mają odpowiedzi (punkt 3b).

## 10. Dalej
Wybór ekranu i ścieżki (moment c) przed `/write-prd`, z wyborem typu naczepy (P26 B); eksperymenty i ryzyka wracają w `docs/spec.md` jako kryteria akceptacji (tylko zmierzone lub potwierdzone).

<!-- skill: przeplywy-pm -->
<!-- skill: brainstorm-ideas-new -->
