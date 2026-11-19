<!-- skill: product-name -->
<!-- skill: value-prop-statements -->
# Nazwa i hasło projektu (krok 6)

Podstawa: `docs/zadanie.md`, `docs/decyzje.md` (P6 w trakcie oglądania obrazu; P8 wzorzec z biblioteki; P10 obecne narzędzie KAS słabe przy małych ilościach w konstrukcji; P11 bez obietnic o dużych plikach przed pomiarem; P12 przeróbki konstrukcji; P13 nie przeoczyć skrytki, kilka zaznaczeń na auto), `docs/pm/01-competitive-analysis.md` (konkurenci: Rapiscan Vehicle Compare, Smiths AXR, ACXIS — nazwy opisowe, w stylu „porównanie”, „kontrola”). Nazwa w `docs/hacktribe.md` bez zmian; wybór należy do Artura.

## 3 kandydaci

| # | Nazwa | Hasło (≤ 80 zn.) | Uzasadnienie |
|---|---|---|---|
| 1 | **Skrytka.AI** | Pokazuje operatorowi to, czego nie ma we wzorcu. (49 zn.) | Używa słowa, którego szuka operator (podwójna podłoga, ściana przy kabinie — P7), więc jest od razu zrozumiała, choć zawęża skojarzenie do skrytek, a nie towaru w ładunku. |
| 2 | **Wzorzec** | Naczepa kontra wzorzec: różnice zaznaczone na obrazie. (53 zn.) | Krótka i wprost z zadania („obraz wzorcowy”), podkreśla wyróżnik z P8 (wzorzec dobiera system), ale nie mówi, że szukamy ukrytego towaru. |
| 3 | **Prześwit** | Drugie spojrzenie na każdy obraz RTG, w trakcie oglądania. (58 zn.) | Polskie, jedno słowo, kojarzy się z prześwietleniem i z „czymś, co prześwituje”; pasuje do P6 (podpowiedź na żywo), ale sama nazwa nie tłumaczy, co narzędzie robi. |

Nazwy nie zawierają zapewnień o dostępności domeny ani znaku towarowego: tego nie sprawdzałem (brak dostępu do rejestrów w tym kroku) — do sprawdzenia przed publikacją.

## Rekomendacja

**Skrytka.AI**, z hasłem „Pokazuje operatorowi to, czego nie ma we wzorcu.” Powód: to jedyna z trzech nazw, którą operator zrozumie bez objaśnień, a hasło dopowiada resztę (porównanie ze wzorcem). Pasuje do priorytetu z P4/P13 (nie przeoczyć skrytki) i do tego, że obecne narzędzie KAS jest słabe właśnie przy małych ilościach ukrytych w konstrukcji (P10). Przeróbki konstrukcji (P12) to też skrytki. Gdyby Artur chciał nazwę szerszą niż „skrytka” (obejmującą też towar w ładunku), druga w kolejności jest **Wzorzec**.

## Wartość dla operatora kontroli (3 zdania)

1. Gdy oglądasz obraz naczepy, narzędzie samo dobiera pasujący wzorzec i zaznacza miejsca, które się od niego różnią, więc nie potrzebujesz zdjęcia czystej naczepy.
2. Łatwiej zauważysz małą skrytkę w podwójnej podłodze czy ścianie przy kabinie oraz obcy towar w ładunku, bo narzędzie pokazuje ci, gdzie spojrzeć jeszcze raz.
3. Celem jest kilka zaznaczeń na auto, nie kilkadziesiąt, a decyzję o kontroli fizycznej nadal podejmujesz ty (liczby fałszywych alarmów i pominięć podamy po pomiarze).
