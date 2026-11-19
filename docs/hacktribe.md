# HackTribe — tekst do formularza zgłoszenia

> **DRAFT** — pierwszy szkic. Opis do uzgodnienia z `docs/spec.md`, gdy powstanie.

## Nazwa projektu (`product-name`) — 3 propozycje

1. **RTG-Różnica** — mówi, co robi: pokazuje różnice między obrazem wzorcowym a kontrolowanym.
2. **Skrytka.AI** — odwołanie do tego, czego szuka operator (skrytki w konstrukcji naczepy); łatwe do zapamiętania.
3. **Wzorzec** — krótkie; od „obrazu wzorcowego”, względem którego liczone są odstępstwa.

Rekomendacja: **Skrytka.AI** (zapadająca w pamięć, od razu kojarzona z przemytem). Ostateczny wybór: Szef / ludzie.

## Nazwa zespołu

Hackathon

## Link do repozytorium

https://github.com/PawelPisarek/hacknation-proba16

## Opis wstępny (DRAFT, limit 1000 znaków)

Operator RTG na granicy ogląda obrazy naczep wielkości ok. 50 MB i musi wypatrzyć drobną przeróbkę lub skrytkę — a obecne narzędzie dobrze wykrywa tylko papierosy. Nasze narzędzie porównuje obraz kontrolowanej naczepy z obrazami wzorcowymi (bez anomalii) i zaznacza na nim miejsca, które odstają od normy: dodatkowe elementy, zmiany konstrukcji, ukryte przedmioty. Operator dostaje raport z oznaczonymi obszarami zamiast szukania „na oko”. Obsługuje pliki BMP, przetwarza obrazy partiami i skaluje się na większe zbiory. Wynik mierzymy na zbiorze obrazów czystych (fałszywe alarmy) i z dodatkami (nietrafione dodatki). Dla operatorów Służby Celno-Skarbowej KAS; docelowo bez chmury. Uwaga: obrazów KAS nie mamy, więc pracujemy na własnym, sztucznym zbiorze naczep.
