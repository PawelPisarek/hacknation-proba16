# 02 — Odkrywanie (`/discover`) — część 1 z 2 (do wyboru Artura)

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

## 3. Czego nie wiem o produkcie (pytania do Artura)
- **P18** — który zestaw 3–5 pomysłów z punktu 2 bierzemy dalej (wybór).
- **P19** — zakres obrazów: tylko naczepy ciężarowe (A) czy też kontenery, autokary i wagony (B)? Zadanie §1 wymienia wszystkie, a nasz zbiór i pokaz to naczepy.
- **P20** — co operator robi z zaznaczeniem: (A) odznacza „sprawdzone / pomyłka” i raport zapisuje się z miejscem i przedmiotem kontroli, czy (B) tylko ogląda zaznaczenia i pobiera raport?
- Po wyborze (P18) osobno: co zmienić w wybranych pomysłach; czy któryś odrzucony warto wziąć w części; które najryzykowniejsze założenia sprawdzamy najpierw.

Pominięte, bo rozstrzyga zadanie: język ekranu, praca bez internetu (§9), sztuczne dane (decyzje 11:59), „bez udziału człowieka” (§3).

## 4. Dalsze części (po wyborze Artura)
Założenia, ich priorytety, eksperymenty, plan odkrywania i drzewo decyzji — po P18 i odpowiedziach na pytania po wyborze.

<!-- skill: przeplywy-pm -->
<!-- skill: brainstorm-ideas-new -->
