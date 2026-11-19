# HackTribe — tekst do formularza zgłoszenia

> **DRAFT** — pierwszy szkic. Opis do uzgodnienia z `docs/spec.md`, gdy powstanie.

## Nazwa projektu (`product-name`) — 3 propozycje

1. **Skrytka.AI** — nazwa od skrytek (podwójna podłoga, ściana przy kabinie), których szuka operator wg P7; łatwe do zapamiętania.
2. **Wzorzec** — krótkie; od „obrazu wzorcowego”, względem którego liczone są odstępstwa.
3. **Prześwit** — polskie, jedno słowo; kojarzy się z prześwietleniem obrazu RTG i podpowiedzią w trakcie oglądania (P6).

Nazwa nie jest wybrana — lista zgodna z `docs/nazwa.md`; wybór czeka na odpowiedź Artura (P14).

## Nazwa zespołu

Hackathon (ustalone: `docs/decyzje.md`, 12:03)

## Link do repozytorium

https://github.com/PawelPisarek/hacknation-proba16

## Opis wstępny (DRAFT, limit 1000 znaków)

Operator RTG na granicy ma kilka minut na naczepę (obraz ok. 50 MB) i szuka drobnej przeróbki lub skrytki. Obecne narzędzie KAS wykrywa papierosy, ale przy małych ilościach ukrytych w konstrukcji pojazdu jest za słabe. Nasze narzędzie podpowiada w trakcie oglądania obrazu: samo dobiera z biblioteki obraz wzorcowy (bez zdjęcia pustej naczepy), porównuje z nim naczepę i zaznacza odstępstwa — dodatki w ładunku oraz przeróbki konstrukcji, najczęściej podwójną podłogę i ścianę przy kabinie. Wczytuje pliki BMP. Wynik na naszym zbiorze: fałszywe alarmy [__], pominięcia [__], czas [__] s na obraz (cel < 1 min); duże pliki i wiele obrazów — po pomiarze. Docelowo bez chmury; w pokazie liczy usługa w sieci lokalnej. Obrazów KAS nie mamy — używamy własnego, sztucznego zbioru naczep.

## Recenzja 1

Wzorzec: `docs/zadanie.md` (§), `docs/decyzje.md`. Braki od najważniejszego (opis ma 793 znaki, limit 1000 — OK):

1. **produkt** — „obecne narzędzie dobrze wykrywa tylko papierosy” przekręca §1: narzędzie wykrywa papierosy, ale przy małych ilościach w elementach konstrukcyjnych jego skuteczność „nie jest zadowalająca”. Zdanie wprost sprzeczne z zadaniem.
2. **produkt** — „skaluje się na większe zbiory”, „przetwarza obrazy partiami”, „obsługuje BMP” to deklaracje (§3), nic z `docs/decyzje.md` nie potwierdza, że będą spełnione ani zmierzone (brak wyniku bazowego). Opis ma obiecywać tylko to, co mamy zmierzone; po wynikach dopisać liczby FP/FN i czas/obraz (§6, §7).
3. **produkt** — „zmiany konstrukcji, ukryte przedmioty” zapowiada więcej niż mierzymy: §6 i `decyzje.md` 12:01 liczą tylko „dodatki” niebędące elementami konstrukcji (FP/FN). Zawęzić do tego, co mamy w zbiorze, albo zaznaczyć, że przeróbki konstrukcji nie są mierzone.
4. **technika** — szkic nie wymienia reguły alarmu ani kryterium trafienia (IoU ≥ 0,1 / środek w ramce; czysty obraz z ≥ 1 zaznaczeniem = FP), więc „fałszywe alarmy / nietrafione dodatki” nie mają definicji w opisie. Dodać zdanie lub link do `docs/decyzje.md`.
5. **technika** — „docelowo bez chmury” (§9) bez dopowiedzenia, że demo działa przez usługę na OMENie w sieci lokalnej (`decyzje.md` 11:59); „Nazwa zespołu: Hackathon” bez źródła w `decyzje.md`/`zespol.md` (tam podpisy nieuzupełnione); wybór nazwy „Skrytka.AI” czeka na Szefa/ludzi — pozostawić jako otwarte, nie jako ustalone.

Poza tym szkic nie zawiera obrazów ani danych KAS (§7) — brak uwag.

## Recenzja 2

Wzorzec: `docs/zadanie.md` (§), `docs/decyzje.md`, odpowiedzi Artura P9 A, P10 A, P11 A, P12 B (z pokoju Produkt, 12:04; w `decyzje.md` jeszcze ich nie ma). Opis ma 972 znaki (limit 1000, zapasu ~28 znaków). Braki od najważniejszego:

1. **produkt** — „samo dobiera z biblioteki obraz wzorcowy (operator nie potrzebuje zdjęcia pustej naczepy)” obiecuje funkcję, której nie mierzymy ani nie mamy: zadanie §5/§7 daje wzorce i pary „przed/po”, a dobór z biblioteki to P8 B, które Projektant w `docs/pm/01` oznaczył jako założenie sprzeczne z §7. Opis pisze to jako fakt (przy P11 A tego samego rodzaju deklaracje mają czekać na pomiar).
2. **produkt** — P12 B każe obiecać przeróbki konstrukcji („podwójna podłoga”, „ściana przy kabinie”), a §6 i metryka (FP/FN na „dodatkach niebędących elementami konstrukcji”) ich nie mierzą. Opis nie mówi, jak sprawdzimy tę obietnicę; brak linii o zbiorze testowym zawierającym przeróbki konstrukcji (generator) — obietnica bez pokrycia w liczbach.
3. **produkt** — „Przetwarzamy pliki BMP” oraz „czas [__] s na obraz” bez progu: zadanie §7 wymaga < 1 min; P6 A (na żywo, kilka minut na auto) nie wchodzi do opisu w ogóle, choć to sposób użycia widoczny dla operatora.
4. **technika** — pola „[__]” (FP, pominięte, czas, duże pliki) muszą być wypełnione liczbami ze skryptu oceny przed oddaniem; nie ma tu odesłania do źródła (plik wynikowy), a wolne ~28 znaków może nie starczyć na cztery liczby i definicję „fałszywego alarmu” (czysty obraz z ≥ 1 zaznaczeniem, P9).
5. **technika** — P9–P12 nie są wpisane do `docs/decyzje.md` (są tylko z „czeka”), więc poprawki Prezentera nie mają śladu odpowiedzi w repozytorium; wpisać odpowiedzi z godziną. Nagłówek „DRAFT — do uzgodnienia z docs/spec.md” zostaje do czasu spec.md.
