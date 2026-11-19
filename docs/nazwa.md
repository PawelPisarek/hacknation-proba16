<!-- skill: product-name -->
<!-- skill: value-prop-statements -->
# Nazwa i hasło projektu (krok 6)

**Wybrane: Prześwit (P14)** — hasło: „Zaznacza na obrazie RTG miejsca różne od wzorca.” (50 zn.; wersja zgodna z P15 i P16, bez „każdy obraz”). Poniżej kandydaci i rekomendacja z kroku 6 jako historia (rekomendacja Skrytka.AI nie została przyjęta; hasło kandydata 3 poniżej sprzed P16).

Podstawa: `docs/zadanie.md`, `docs/decyzje.md` (P6 w trakcie oglądania obrazu; P8 wzorzec z biblioteki; P10 obecne narzędzie KAS słabe przy małych ilościach w konstrukcji; P11 bez obietnic o dużych plikach przed pomiarem; P12 przeróbki konstrukcji; P13 nie przeoczyć skrytki, kilka zaznaczeń na auto), `docs/pm/01-competitive-analysis.md` (konkurenci: Rapiscan Vehicle Compare, Smiths AXR, ACXIS — nazwy opisowe, w stylu „porównanie”, „kontrola”). Lista kandydatów jest zgodna z `docs/hacktribe.md` (Skrytka.AI, Wzorzec, Prześwit; wcześniejsze RTG-Różnica zastąpiono Prześwitem). Wybór: Prześwit (P14, Artur).

## 3 kandydaci

| # | Nazwa | Hasło (≤ 80 zn.) | Uzasadnienie |
|---|---|---|---|
| 1 | **Skrytka.AI** | Pokazuje operatorowi to, czego nie ma we wzorcu. (48 zn.) | Nazywa to, co mają znaleźć miejsca z P7 (podwójna podłoga, ściana przy kabinie) i przeróbki z P12, więc jest od razu zrozumiała, choć zawęża skojarzenie do skrytek, a nie towaru w ładunku (słowo „skrytka” to nasz wybór, nie sformułowanie z zadania ani z odpowiedzi Artura). |
| 2 | **Wzorzec** | Naczepa kontra wzorzec: różnice zaznaczone na obrazie. (56 zn.) | Krótka i wprost z zadania („obraz wzorcowy”), podkreśla wyróżnik z P8 (wzorzec dobiera system), ale nie mówi, że szukamy ukrytego towaru. |
| 3 | **Prześwit** | Drugie spojrzenie na każdy obraz RTG, w trakcie oglądania. (60 zn.) | Polskie, jedno słowo, kojarzy się z prześwietleniem i z „czymś, co prześwituje”; pasuje do P6 (podpowiedź na żywo), ale sama nazwa nie tłumaczy, co narzędzie robi. |

Nazwy nie zawierają zapewnień o dostępności domeny ani znaku towarowego: tego nie sprawdzałem (brak dostępu do rejestrów w tym kroku) — do sprawdzenia przed publikacją.

## Rekomendacja

**Skrytka.AI**, z hasłem „Pokazuje operatorowi to, czego nie ma we wzorcu.” Powód: to jedyna z trzech nazw, którą operator zrozumie bez objaśnień, a hasło dopowiada resztę (porównanie ze wzorcem). Pasuje do priorytetu z P4/P13 (nie przeoczyć skrytki) i do tego, że obecne narzędzie KAS jest słabe właśnie przy małych ilościach ukrytych w konstrukcji (P10). Przeróbki konstrukcji (P12) to też skrytki. Gdyby Artur chciał nazwę szerszą niż „skrytka” (obejmującą też towar w ładunku), druga w kolejności jest **Wzorzec**.

## Wartość dla operatora kontroli (3 zdania)

1. Gdy oglądasz obraz naczepy, narzędzie samo dobiera pasujący wzorzec i zaznacza miejsca, które się od niego różnią, więc nie potrzebujesz zdjęcia czystej naczepy.
2. Łatwiej zauważysz małą skrytkę w podwójnej podłodze czy ścianie przy kabinie oraz obcy towar w ładunku, bo narzędzie pokazuje ci, gdzie spojrzeć jeszcze raz.
3. Celem jest kilka zaznaczeń na auto, nie kilkadziesiąt, a decyzję o kontroli fizycznej nadal podejmujesz ty (liczby fałszywych alarmów i pominięć podamy po pomiarze).

## Recenzja 1

Oceniono `docs/nazwa.md` (fd37b90) względem `docs/zadanie.md` i `docs/decyzje.md` (P4, P6–P13). Braki od najważniejszego:

1. **produkt** — rekomendowana „Skrytka.AI” zawęża produkt do skrytek, a P7 („oba”: konstrukcja i ładunek) i P12 B (przeróbki) obejmują więcej; plik sam to przyznaje, a mimo to rekomenduje. Hasło („czego nie ma we wzorcu”) też nie mówi o towarze w ładunku. Rozstrzygnięcie: rekomendować nazwę zgodną z P7 albo wprost pokazać Arturowi tę cenę wyboru.
2. **produkt** — zdanie 3 wartości: „kilka zaznaczeń na auto, nie kilkadziesiąt” (P13) obok zadania §6 (na czystych obrazach nic nie zaznaczać; każdy alarm = FP) może zostać odczytane jako obietnica fałszywych alarmów. Brak rozróżnienia, że chodzi o kompromis z P13, a cel to zero na czystych.
3. **produkt** — zdanie 1 („nie potrzebujesz zdjęcia czystej naczepy”) i hasło kandydata 3 („na każdy obraz”) obiecują dobór wzorca i pokrycie bez pomiaru; P11 wymaga wstrzymania obietnic do pomiaru, a założenie P8 B jest sprzeczne z §7 zadania (pary „przed/po”). Brak zastrzeżenia.
4. **technika** — plik pisze „Nazwa w `docs/hacktribe.md` bez zmian”, ale lista w hacktribe to RTG-Różnica / Skrytka.AI / Wzorzec, a tu Skrytka.AI / Wzorzec / Prześwit (RTG-Różnica wypadła, Prześwit doszedł) — sprzeczność między plikami bez wyjaśnienia.
5. **technika** — uzasadnienie 1 „słowo, którego szuka operator (P7)” bez źródła: P7 mówi o podwójnej podłodze i ścianie przy kabinie, nie o słowie „skrytka”. Znaczniki `<!-- skill: … -->` stoją na początku pliku, nie na końcu.

<!-- skill: review -->
