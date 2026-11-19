# HackTribe — tekst do formularza zgłoszenia

> **DRAFT** — pierwszy szkic. Opis do uzgodnienia z `docs/spec.md`, gdy powstanie.

## Nazwa projektu (`product-name`) — 3 propozycje

1. **RTG-Różnica** — mówi, co robi: pokazuje różnice między obrazem wzorcowym a kontrolowanym.
2. **Skrytka.AI** — odwołanie do tego, czego szuka operator (skrytki w konstrukcji naczepy); łatwe do zapamiętania.
3. **Wzorzec** — krótkie; od „obrazu wzorcowego”, względem którego liczone są odstępstwa.

Nazwa nie jest wybrana — wybór w kroku 6 (`product-name`).

## Nazwa zespołu

Hackathon (ustalone: `docs/decyzje.md`, 12:03)

## Link do repozytorium

https://github.com/PawelPisarek/hacknation-proba16

## Opis wstępny (DRAFT, limit 1000 znaków)

Operator RTG na granicy ogląda obrazy naczep (ok. 50 MB) i musi wypatrzyć drobną przeróbkę lub skrytkę. Obecne narzędzie KAS wykrywa papierosy, ale przy małych ilościach ukrytych w konstrukcji pojazdu jest za słabe. Nasze narzędzie samo dobiera z biblioteki obraz wzorcowy (operator nie potrzebuje zdjęcia pustej naczepy), porównuje z nim kontrolowaną naczepę i zaznacza odstępstwa: dodatki w ładunku i konstrukcji oraz przeróbki konstrukcji, najczęściej podwójną podłogę i ścianę przy kabinie. Operator dostaje raport z oznaczonymi obszarami. Przetwarzamy pliki BMP. Wynik na naszym zbiorze: fałszywe alarmy [__], pominięte dodatki [__], czas [__] s na obraz; obsługę dużych plików i wielu obrazów naraz [__] dopiszemy po pomiarze. Dla operatorów Służby Celno-Skarbowej; docelowo bez chmury, w pokazie wynik liczy nasza usługa w sieci lokalnej, bez internetu. Obrazów KAS nie mamy — pracujemy na własnym, sztucznym zbiorze naczep.

## Recenzja 1

Wzorzec: `docs/zadanie.md` (§), `docs/decyzje.md`. Braki od najważniejszego (opis ma 793 znaki, limit 1000 — OK):

1. **produkt** — „obecne narzędzie dobrze wykrywa tylko papierosy” przekręca §1: narzędzie wykrywa papierosy, ale przy małych ilościach w elementach konstrukcyjnych jego skuteczność „nie jest zadowalająca”. Zdanie wprost sprzeczne z zadaniem.
2. **produkt** — „skaluje się na większe zbiory”, „przetwarza obrazy partiami”, „obsługuje BMP” to deklaracje (§3), nic z `docs/decyzje.md` nie potwierdza, że będą spełnione ani zmierzone (brak wyniku bazowego). Opis ma obiecywać tylko to, co mamy zmierzone; po wynikach dopisać liczby FP/FN i czas/obraz (§6, §7).
3. **produkt** — „zmiany konstrukcji, ukryte przedmioty” zapowiada więcej niż mierzymy: §6 i `decyzje.md` 12:01 liczą tylko „dodatki” niebędące elementami konstrukcji (FP/FN). Zawęzić do tego, co mamy w zbiorze, albo zaznaczyć, że przeróbki konstrukcji nie są mierzone.
4. **technika** — szkic nie wymienia reguły alarmu ani kryterium trafienia (IoU ≥ 0,1 / środek w ramce; czysty obraz z ≥ 1 zaznaczeniem = FP), więc „fałszywe alarmy / nietrafione dodatki” nie mają definicji w opisie. Dodać zdanie lub link do `docs/decyzje.md`.
5. **technika** — „docelowo bez chmury” (§9) bez dopowiedzenia, że demo działa przez usługę na OMENie w sieci lokalnej (`decyzje.md` 11:59); „Nazwa zespołu: Hackathon” bez źródła w `decyzje.md`/`zespol.md` (tam podpisy nieuzupełnione); wybór nazwy „Skrytka.AI” czeka na Szefa/ludzi — pozostawić jako otwarte, nie jako ustalone.

Poza tym szkic nie zawiera obrazów ani danych KAS (§7) — brak uwag.
