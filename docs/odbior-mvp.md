# Odbiór MVP — lista sprawdzeń na noc

Źródła: `docs/zadania/01-mvp-z-makiety.md` (P29–P38), `docs/spec.md` §7.4 (A1–A10), §7.6. Dowody: zrzuty w `docs/zrzuty/mvp-*.png`, pliki pobrane z aplikacji (JSON/PNG), komendy. Spec i zadania bez zmian.
Skróty: „ap.” = prawdziwa aplikacja pod ksefbot.pl (wynik z karty OMENa); obrazy (a)–(d) to 4 gotowe obrazy z §7.2.

## 1. Wiersze P29–P38

| # | P | krok w aplikacji | oczekiwany wynik | dowód |
|---|---|---|---|---|
| 1 | P29 | Wczytaj (b). Przy miejscu 1 kliknij „Zatwierdź”. | 1 kliknięcie; miejsce oznaczone „zatwierdzone”; pasek postępu rośnie | zrzut `mvp-p29-zatwierdz.png` |
| 2 | P29 | Przy miejscu 2 kliknij „Odrzuć”. | Pojawia się lista powodów; bez wyboru powodu miejsce nie jest odrzucone | zrzut `mvp-p29-odrzuc.png` |
| 3 | P30 | Wczytaj (b) i (c); obejrzyj listę miejsc. | Przy każdym miejscu słowo niski / średni / wysoki; brak cyfr i % w liście; kolejność od wysokiego | zrzut + `curl` wyniku JSON: pole stopnia ∈ {niski,średni,wysoki}, lista posortowana (test JSON) |
| 4 | P31 | Wczytaj (b). | Dwa okna obok siebie: wzorzec (lewo), badany z ramkami (prawo), lista miejsc z boku; wspólne przewijanie | zrzut `mvp-p31-uklad.png` |
| 5 | P32 | Kliknij „Odrzuć”, nie wybieraj powodu. Potem wybierz powód. | Bez powodu odrzucenie niemożliwe; lista powodów = lista z A7 (zob. rozbieżność 1); po wyborze miejsce odrzucone | zrzut przed i po (`mvp-p32-*.png`) |
| 6 | P33 | Kliknij miejsce na liście. | W oknie wzorca przerywana ramka w tym samym punkcie co w badanym | zrzut `mvp-p33-ramka.png` |
| 7 | P34 | Wczytaj (b); potem (d). | (b): „porównano z: chłodnia”; (d): system dobiera „plandeka”, lista pozwala zmienić na „chłodnia” | 2 zrzuty `mvp-p34-b.png`, `mvp-p34-d.png` |
| 8 | P35 | Podejmij decyzje przy wszystkich miejscach (b), „Zapisz raport”, pobierz JSON i PNG. | PNG: obraz z zaznaczeniami; JSON: miejsce i przedmiot kontroli, ramki, decyzja i powód przy każdej; pola przykładowe (przejście, nr rej.) opisane „dane sztuczne” | pobrane pliki; `python3 -m json.tool raport.json`; zrzut okna raportu |
| 9 | P36 | Wczytaj (b); obejrzyj miejsca 1 i 2 (małe). | Przy każdym duży numer i krótki opis, także przy małym | zrzut `mvp-p36-opisy.png` |
| 10 | P37 | Wczytaj (b); obejrzyj okno wzorca i dolny pasek. | Brak napisu „WZORZEC: plandeka” w oknie wzorca (nagłówek i pole typu zostają); na pasku brak zdania ostrożności | zrzut `mvp-p37-ekran.png` + `grep -ri "WZORZEC:" <źródła ekranu>` bez trafień |
| 11 | P38 | Wczytaj (b), podejmij decyzję tylko przy 1 z 2 miejsc, „Zapisz raport”. | Jedno ostrzeżenie „Nieprzejrzane: 1 miejsc. Zapisać mimo to?” z właściwą liczbą N (zob. rozbieżność 4 co do odmiany); „anuluj” wraca na ekran bez zapisu | zrzut `mvp-p38-ostrzezenie.png` |
| 12 | P38 | Potwierdź zapis. | Raport zapisany; przy miejscu bez decyzji „nieprzejrzane” | JSON: `grep nieprzejrzane raport.json` |
| 13 | P38 | Podejmij decyzje przy wszystkich miejscach, zapisz. | Brak ostrzeżenia | zrzut / brak okna |

## 2. Testy akceptacji ze specu (A1–A10)

| # | A | krok | oczekiwany wynik | dowód |
|---|---|---|---|---|
| 14 | A1 | Skrypt oceny na zbiorze generatora 0P, podwójna podłoga (kryterium P9 A: zaznaczenie choć częściowo nachodzi na skrytkę albo środek leży w skrytce) | 0 przeoczeń (lub próg zapisany przez Programistę w `docs/decyzje.md` przed odbiorem); wynik „n z N” | komenda oceny na OMENie (jak `wyniki/0P/README.md`), linia FN |
| 15 | A2 | Ten sam przebieg: ściana przy kabinie i towar w ładunku liczone osobno | FN osobno dla konstrukcji (ściana) i towaru; progi zapisane w `docs/decyzje.md` | te same liczby FN w `wyniki/…/README.md` |
| 16 | A3 | Dobór wzorca na zbiorze 0P | wynik „n z N” trafności doboru; próg zapisany | linia z oceny |
| 17 | A4 | Zmierz czas od wczytania do wyniku dla (a)–(d) i wgranego .bmp | < 60 s każdy | `time curl …` / log z zegarem |
| 18 | A5 | Policz kliknięcia: „Zatwierdź”; „Odrzuć” z powodem | 1 i 2 kliknięcia | nagranie albo zrzut sekwencji `mvp-a5-*.png` |
| 19 | A6 | Na (d) zmień typ „plandeka”→„chłodnia” | najwyżej 1 kliknięcie; wzorzec się zmienia, porównanie odświeża (nowa lista i ramki) | zrzut przed/po `mvp-a6-*.png` |
| 20 | A7 | Zapis raportu z decyzjami zatwierdź/odrzuć/nieprzejrzane | JSON zawiera miejsce, przedmiot kontroli, decyzję przy każdym miejscu; przy „Odrzuć” powód z listy (element konstrukcji / ładunek zgodny z deklaracją / cień lub zakłócenie obrazu / inne); „nieprzejrzane” gdzie brak decyzji | JSON + schemat sprawdzony skryptem (`python3`) |
| 21 | A8 | Przegląd z Arturem jako operatorem (po MVP): miara 1 (zatwierdzone n z N, bez %) i miara 2 (zaznaczenia na czystym obrazie) | liczby „n z N”; „kilka, nie kilkadziesiąt” ustala Artur | **nie na noc** — wymaga Artura; na noc tylko liczba z 0P (komenda oceny) |
| 22 | A9 | Przeszukaj teksty ekranu i raportu | brak zdań obiecujących skuteczność | `grep -riE "skuteczn|wykryj(e|emy) (wszystk|każd)|żadn" <teksty ekranu>` + przegląd zrzutów |
| 23 | A10 | Czyste obrazy z generatora (a): policz FP = obraz z ≥1 zaznaczeniem; razem z FN | wynik „n z N”; próg FP po pomiarze zapisany w `docs/decyzje.md` | komenda oceny, linia FP |
| 24 | §7.2 | Wczytaj (a) | „0 miejsc”, brak ramek, brak komunikatu sugerującego „nic nie ma” inaczej niż „0 miejsc” (P15–P17) | zrzut `mvp-a-czysta.png` |
| 25 | §7.2/§7.3 | Wczytaj (c) | 4 zaznaczenia; na liście strefy „ściana przy kabinie” i towar w ładunku; pasek „Przejrzano 0 z 4” | zrzut `mvp-c.png` |
| 26 | §7.6 pkt 1 | Wgraj własny .bmp zamiast gotowego | wynik jak dla gotowych; typy z listy: plandeka, chłodnia, kontener na podwoziu, cysterna, skrzyniowa | zrzut + lista opcji |
| 27 | §7.6 pkt 3 | Podwójna podłoga (b) | ramka w strefie ryzyka (środek w pasie nad podłogą) ma wyróżniony kolor i etykietę „podwójna podłoga”; reszta bez koloru strefy | zrzut `mvp-b-strefa.png` |
| 28 | §7.6 pkt 4 | Sprawdź, co jest pod publicznym linkiem | tylko dane sztuczne; obraz od KAS nigdy nie jest wysyłany poza komputer (uruchomienie lokalne z Dockerfile) | `curl -s -o /dev/null -w "%{http_code}" <link>` = 200; przegląd żądań sieciowych / kodu |
| 29 | zadanie 01 „Gotowe” | Aplikacja pod linkiem | HTTP 200 | `curl -s -o /dev/null -w "%{http_code}\n" https://ksefbot.pl/…` (adres z `docs/uruchomienie.md`) |
| 30 | zadanie 01 „Kolejność” | Rdzeń: .bmp → PNG + JSON; test 4 obrazów | każdy z 4 obrazów daje PNG + JSON; ramki zgodne z §7.2 (b: 2, c: 4, a: 0) | linia wyniku testu (`pytest`/skrypt) |

Razem: **30 sprawdzeń** (13 z P29–P38, 17 z A1–A10, §7.2–7.6 i warunków zadania 01). Nr 21 wymaga Artura, reszta da się wykonać w nocy.

## 3. Rozbieżności spec ↔ zadanie 01

1. **produkt** — lista powodów odrzucenia (P32): zadanie 01 wymienia 3 („element konstrukcji, ładunek zgodny, cień”), spec A7 ma 4 (+ „inne”, „ładunek zgodny z deklaracją”, „cień lub zakłócenie obrazu”). Operator zobaczy różne listy. Poprawka (nie pytanie, P17 A): lista ze specu jest wiążąca (właściciel: Projektant; zmienia tylko Artur).
2. **technika** — dane: zadanie 01 wymaga „wynik z karty OMENa, nie dane udawane” pod ksefbot.pl, spec §7.6 pkt 4 mówi, że pod publicznym linkiem są tylko dane sztuczne, a obrazy KAS tylko lokalnie. Do doprecyzowania: obrazy (a)–(d) i .bmp z generatora = sztuczne, ale liczone naprawdę; obrazów KAS pod linkiem brak.
3. **technika** — zadanie 01 nie obejmuje A1–A4, A6, A9, A10 (miary FN/FP/czas/trafność doboru, zmiana typu jednym kliknięciem, brak obietnic); „Gotowe, gdy” sprawdza tylko P29–P38. Odbiór według tego pliku (wiersze 14–19, 22–23) pokrywa lukę; Szef może dopisać do zadania.
4. **technika** — P38: tekst „Nieprzejrzane: N miejsc. Zapisać mimo to?” przy N=1 będzie nieodmienny („1 miejsc”); zadanie i spec tak go podają. Do ustalenia, czy akceptujemy dosłowny napis (wtedy sprawdzenie 11 przechodzi z „1 miejsc”).
5. **technika** — A8 miara 2 i próg „kilka, nie kilkadziesiąt” czekają na Artura po MVP, zadanie 01 o tym milczy; na noc nie ma kryterium przejścia (wiersz 21).

<!-- skill: brak -->
