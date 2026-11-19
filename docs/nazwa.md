<!-- skill: product-name -->
<!-- skill: value-prop-statements -->
# Nazwa i hasło projektu (krok 6)

**Wybrane: Prześwit (P14)** — hasło: „Zaznacza na obrazie RTG miejsca różne od wzorca.” (50 zn.; zgodne z P15 i P16: „zaznacza miejsca różne od wzorca”, „system sam dobiera wzorzec z biblioteki”, liczba z pomiaru [__]). Poniżej kandydaci i rekomendacja z kroku 6 jako historia (rekomendacja Skrytka.AI nie została przyjęta).

Podstawa: `docs/zadanie.md`, `docs/decyzje.md` (P6 w trakcie oglądania obrazu; P8 wzorzec z biblioteki; P10 obecne narzędzie KAS słabe przy małych ilościach w konstrukcji; P11 bez obietnic o dużych plikach przed pomiarem; P12 przeróbki konstrukcji; P13 nie przeoczyć skrytki, kilka zaznaczeń na auto), `docs/pm/01-competitive-analysis.md` (konkurenci: Rapiscan Vehicle Compare, Smiths AXR, ACXIS — nazwy opisowe, w stylu „porównanie”, „kontrola”). Lista kandydatów jest zgodna z `docs/hacktribe.md` (Skrytka.AI, Wzorzec, Prześwit; wcześniejsze RTG-Różnica zastąpiono Prześwitem). Wybór: Prześwit (P14, Artur).

## 3 kandydaci

| # | Nazwa | Hasło (≤ 80 zn.) | Uzasadnienie |
|---|---|---|---|
| 1 | **Skrytka.AI** | Pokazuje operatorowi to, czego nie ma we wzorcu. (48 zn.) | Nazywa to, co mają znaleźć miejsca z P7 (podwójna podłoga, ściana przy kabinie) i przeróbki z P12, więc jest od razu zrozumiała, choć zawęża skojarzenie do skrytek, a nie towaru w ładunku (słowo „skrytka” to nasz wybór, nie sformułowanie z zadania ani z odpowiedzi Artura). |
| 2 | **Wzorzec** | Naczepa kontra wzorzec: różnice zaznaczone na obrazie. (56 zn.) | Krótka i wprost z zadania („obraz wzorcowy”), podkreśla wyróżnik z P8 (wzorzec dobiera system), ale nie mówi, że szukamy ukrytego towaru. |
| 3 | **Prześwit** | Drugie spojrzenie na obraz RTG, w trakcie oglądania. (53 zn.; hasło tego kandydata po P16, bez „na każdy obraz”) | Polskie, jedno słowo, kojarzy się z prześwietleniem i z „czymś, co prześwituje”; pasuje do P6 (podpowiedź na żywo), ale sama nazwa nie tłumaczy, co narzędzie robi. |

Domeny ani znaku towarowego (kandydatów i wybranego „Prześwit”) nie sprawdzamy — poza zakresem DRAFTu; do sprawdzenia przed publikacją.

## Rekomendacja Skrytka.AI — odrzucona (P14: Prześwit)

**Skrytka.AI**, z hasłem „Pokazuje operatorowi to, czego nie ma we wzorcu.” Powód: to jedyna z trzech nazw, którą operator zrozumie bez objaśnień, a hasło dopowiada resztę (porównanie ze wzorcem). Pasuje do priorytetu z P4/P13 (nie przeoczyć skrytki) i do tego, że obecne narzędzie KAS jest słabe właśnie przy małych ilościach ukrytych w konstrukcji (P10). Przeróbki konstrukcji (P12) to też skrytki. Gdyby Artur chciał nazwę szerszą niż „skrytka” (obejmującą też towar w ładunku), druga w kolejności jest **Wzorzec**.

## Wartość dla operatora kontroli (3 zdania)

1. Gdy oglądasz obraz naczepy, system sam dobiera wzorzec z biblioteki i zaznacza miejsca różne od wzorca.
2. Narzędzie pokazuje, gdzie obraz różni się od wzorca — tam warto spojrzeć jeszcze raz.
3. Liczbę zaznaczeń na czystych obrazach i pominięć podamy z pomiaru: [__]; decyzję o kontroli fizycznej nadal podejmujesz ty.

## Recenzja 1

Oceniono `docs/nazwa.md` (fd37b90) względem `docs/zadanie.md` i `docs/decyzje.md` (P4, P6–P13). Braki od najważniejszego:

1. **produkt** — rekomendowana „Skrytka.AI” zawęża produkt do skrytek, a P7 („oba”: konstrukcja i ładunek) i P12 B (przeróbki) obejmują więcej; plik sam to przyznaje, a mimo to rekomenduje. Hasło („czego nie ma we wzorcu”) też nie mówi o towarze w ładunku. Rozstrzygnięcie: rekomendować nazwę zgodną z P7 albo wprost pokazać Arturowi tę cenę wyboru.
2. **produkt** — zdanie 3 wartości: „kilka zaznaczeń na auto, nie kilkadziesiąt” (P13) obok zadania §6 (na czystych obrazach nic nie zaznaczać; każdy alarm = FP) może zostać odczytane jako obietnica fałszywych alarmów. Brak rozróżnienia, że chodzi o kompromis z P13, a cel to zero na czystych.
3. **produkt** — zdanie 1 („nie potrzebujesz zdjęcia czystej naczepy”) i hasło kandydata 3 („na każdy obraz”) obiecują dobór wzorca i pokrycie bez pomiaru; P11 wymaga wstrzymania obietnic do pomiaru, a założenie P8 B jest sprzeczne z §7 zadania (pary „przed/po”). Brak zastrzeżenia.
4. **technika** — plik pisze „Nazwa w `docs/hacktribe.md` bez zmian”, ale lista w hacktribe to RTG-Różnica / Skrytka.AI / Wzorzec, a tu Skrytka.AI / Wzorzec / Prześwit (RTG-Różnica wypadła, Prześwit doszedł) — sprzeczność między plikami bez wyjaśnienia.
5. **technika** — uzasadnienie 1 „słowo, którego szuka operator (P7)” bez źródła: P7 mówi o podwójnej podłodze i ścianie przy kabinie, nie o słowie „skrytka”. Znaczniki `<!-- skill: … -->` stoją na początku pliku, nie na końcu.


## Recenzja 2

Oceniono `docs/nazwa.md` i `docs/hacktribe.md` (3061476) względem `docs/zadanie.md` i `docs/decyzje.md` (P4, P6–P16). Braki recenzji 1 do nazwa.md zamknięte: 1–3 odpowiedziami P14 (Prześwit), P15, P16; 4–5 poprawką Prezentera i decyzją Szefa (znaczniki na górze zostają) — nie wracają. Opis HackTribe ma 820 znaków (limit 1000); hasło 50 zn. Braki od najważniejszego:

1. **produkt** — wartość zd. 2: „Łatwiej zauważysz małą skrytkę … bo narzędzie pokazuje ci, gdzie spojrzeć jeszcze raz” to obietnica skuteczności bez pomiaru; P16 A i P11 każą pisać ostrożnie, a P15 chce „zaznacza miejsca różne od wzorca” + liczba z pomiaru. Zd. 1 i 3 są zgodne, zd. 2 nie.
2. **technika** — `docs/hacktribe.md` (plik „tekst do formularza”) zawiera nadal stare sekcje „Recenzja 1” i „Recenzja 2” z nieaktualnymi stwierdzeniami (opis „793”/„972 znaków”, „P9–P12 nie wpisane”, Skrytka.AI jako otwarta) — sprzeczne z bieżącym tekstem; recenzje są w historii git, w pliku do wklejenia powinien zostać sam tekst.
3. **technika** — `docs/nazwa.md`: nagłówek mówi „hasło kandydata 3 poniżej sprzed P16”, a tabela ma już nową wersję, przy tym „51 zn.” — faktycznie 53 znaki (liczone `wc -m`). Sekcja „Rekomendacja Skrytka.AI” stoi bez oznaczenia przy samej sekcji, że odrzucona (P14).
4. **technika** — opis: „czyste obrazy z zaznaczeniem [__]” bez jednostki i definicji (liczba obrazów czy %; z P9: czysty obraz z ≥ 1 zaznaczeniem = fałszywy alarm); „pominięte dodatki [__]” bez określenia, czy wliczone przeróbki konstrukcji (P12). Wybrana nazwa „Prześwit”: dostępność domeny/znaku nie sprawdzona (zastrzeżenie dotyczy tylko kandydatów) — do sprawdzenia przed publikacją.


## Recenzja 3

Oceniono `docs/nazwa.md` i `docs/hacktribe.md` (974d7e9) względem `docs/zadanie.md` i `docs/decyzje.md` (P4–P17, zasada Artura z 12:17/12:18). Braki recenzji 2 zamknięte: 1 — P17 A (zdanie 2 wartości ostrożne), 2 — sekcje recenzji usunięte z hacktribe.md, 3 — hasło 53 zn. (zgodne z `wc -m`), Skrytka.AI oznaczona jako odrzucona (P14), 4 — opis z „[__] z [__]” i przeróbkami konstrukcji; domena i znak poza zakresem. Opis 867 znaków (limit 1000), hasło 50 zn. (limit 80).

brak braków zmieniających zakres lub kryteria

Uwaga niezmieniająca zakresu (technika): w `docs/hacktribe.md` linie „Recenzje 1–2: w historii git…” i „Poza zakresem DRAFTu…” są notatkami wewnętrznymi, nie tekstem do formularza — usunąć przy wklejaniu.

<!-- skill: review -->
