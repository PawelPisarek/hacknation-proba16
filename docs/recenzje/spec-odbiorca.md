# Recenzja odbiorcy: docs/spec.md (987a579) — Programista, 15:01

Pytanie: czego mi brakuje, żeby zbudować MVP. Pomiar 0P już jest (wyniki/0P, c156e12): H2ko FP 7/20, FN 0/45 — progi A1–A3, A10 wpisuję sam (P16).

1. **technika — wejście i biblioteka.** Spec nie mówi, jak obraz trafia do aplikacji (wgranie .bmp ~50 MB czy wybór z gotowych) ani skąd lista typów naczep: generator ma typy numerowane, spec podaje „plandeka”, „chłodnia”. Rekomendacja: wgranie .bmp + 4 gotowe obrazy (a–d) z generatora; biblioteka = katalog wzorców, nazwy typów nadaję w generatorze (plandeka, chłodnia, kontener na podwoziu, cysterna, skrzyniowa).
2. **technika — wyjście: format raportu.** „Plik do pobrania” bez formatu. Rekomendacja: PNG obrazu z ramkami + JSON (miejsce i przedmiot kontroli, ramki, decyzja i powód przy każdej) — JSON pasuje do repozytorium KAS z przypisaniem do miejsca i przedmiotu kontroli (zadanie §9).
3. **technika — granice stref ryzyka.** Nie wiadomo, jak wyznaczam „podwójną podłogę” i „ścianę przy kabinie” na obrazie ani kiedy ramka „jest w strefie”. Rekomendacja: strefy z geometrii wzorca danego typu (pas nad podłogą przestrzeni ładunkowej, pas przy ścianie od kabiny); ramka w strefie, gdy jej środek leży w strefie.
4. **technika — dane chronione a link publiczny.** Zadanie §7: obrazy KAS to dane chronione, zakaz udostępniania. Spec nie mówi, gdzie liczy MVP z prawdziwym obrazem. Rekomendacja: pod linkiem ksefbot.pl tylko dane sztuczne (porównanie na karcie OMENa); obraz KAS — uruchomienie lokalne z Dockerfile, bez wysyłki poza komputer.
5. **produkt — „stopień różnicy” na liście miejsc.** Brak skali, którą zobaczy operator. Rekomendacja: trzy poziomy słownie (niski / średni / wysoki) wg wyniku porównania, bez liczb i procentów (P15–P17).
