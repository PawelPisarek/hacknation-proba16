# 04 — Trzy warianty ekranu (szkice dla Programisty)

Podstawa: `docs/spec.md` §7 (987a579). Wszystkie warianty mają to samo: obraz naczepy z zaznaczeniami, dobrany wzorzec, wybór typu z listy (1 kliknięcie), „Zatwierdź” (1 kliknięcie) / „Odrzuć” (przycisk + powód z listy: element konstrukcji / ładunek zgodny z deklaracją / cień lub zakłócenie obrazu / inne), pasek postępu, raport („miejsce kontroli”, „przedmiot kontroli”, zapis do pliku). Różni się tylko układ i kolejność pracy. Dane udawane: `naczepa_017.bmp`; typ dobrany „plandeka”, poprawny „chłodnia”; paski „Przejrzano 2 z 2” (obraz b), „Przejrzano 0 z 4” (obraz c), „0 miejsc” (obraz a). Tekst ostrożności (P17) na dole każdego wariantu.

Artur wybiera wariant i mówi, co mu się podoba, a co nie (jeszcze nie pytany).

## Wariant 1 — Jeden obraz na cały ekran
**Po co:** operator widzi całą naczepę naraz i ocenia ją „jednym spojrzeniem”; lista miejsc jest tylko dodatkiem z boku.
**Czym się różni:** obraz dominuje (~75% szerokości), lista wąska z prawej, decyzje na liście.

```
+--------------------------------------------------------------------------+
| Prześwit | naczepa_017.bmp | porównano z: [plandeka v] | [Zapisz raport]   |
+------------------------------------------------------+-------------------+
|                                                      | Miejsca (od       |
|   [ OBRAZ NACZEPY – duży ]                           | najbardziej różnych)|
|    ┌─────────┐  ← ramka czerwona „podwójna podłoga”  | 1 podw. podłoga  |
|    └─────────┘                                       |  [Zatwierdź][Odrzuć]|
|          ┌──┐ ← ramka zwykła                         | 2 ściana z kabiną |
|          └──┘                                        |  [Zatwierdź][Odrzuć]|
|   suwak pionowy: wzorzec | badany (przesuwany)       | 3 ...             |
+------------------------------------------------------+-------------------+
| Przejrzano 0 z 4  ▒▒░░░░░░   Narzędzie pokazuje, gdzie obraz różni się   |
| od wzorca — tam warto spojrzeć jeszcze raz.                              |
+--------------------------------------------------------------------------+
```
Główna ścieżka: wczytaj obraz → zobacz ramki → w razie złego typu zmień z listy na „chłodnia” → klikaj Zatwierdź/Odrzuć na liście → „Zapisz raport”.
Pierwsze widać: duży obraz z kolorowymi ramkami.

## Wariant 2 — Najpierw kolejka, miejsce po miejscu
**Po co:** prowadzi operatora przez miejsca jedno po drugim z powiększeniem, więc nic nie jest pominięte.
**Czym się różni:** to nie przegląd całości, tylko „kolejka kontroli”; cały obraz jest miniaturą.

```
+--------------------------------------------------------------------------+
| Prześwit | naczepa_017.bmp | porównano z: [plandeka v] |  Przejrzano 0 z 4 |
+--------------------------------------------------------------------------+
| Kolejka:  [1 podw. podłoga*] [2 ściana z kabiną] [3] [4]    (* = aktualne)|
+-----------------------------------------+--------------------------------+
|  POWIĘKSZENIE miejsca 1 z 4             |  Strefa: podwójna podłoga      |
|  ┌───────────────────────────────┐      |  Stopień różnicy: wysoki       |
|  │  zbliżenie badany | wzorzec    │      |  [ Zatwierdź ]                 |
|  └───────────────────────────────┘      |  [ Odrzuć ] → powód z listy v |
|  miniatura całej naczepy z ramkami →    |  [< Poprzednie] [Następne >]   |
+-----------------------------------------+--------------------------------+
| Na końcu kolejki: [Zapisz raport]  Narzędzie pokazuje, gdzie obraz różni |
| się od wzorca — tam warto spojrzeć jeszcze raz.                           |
+--------------------------------------------------------------------------+
```
Główna ścieżka: wczytaj → system ustawia pierwsze miejsce (najbardziej różne) → decyzja → automatycznie następne → po „4 z 4” zapis raportu.
Pierwsze widać: powiększone miejsce nr 1 i dwa przyciski decyzji.
Dla obrazu (a): ekran „0 miejsc — brak różnic od wzorca”.

## Wariant 3 — Wzorzec i obraz badany obok siebie
**Po co:** operator patrzy równocześnie na „jak powinno być” i „jak jest”, więc sam widzi różnicę.
**Czym się różni:** dwa równe okna zamiast jednego z suwakiem; ramki tylko po stronie badanej.

```
+--------------------------------------------------------------------------+
| Prześwit | naczepa_017.bmp | [Zapisz raport]                             |
+----------------------------------+---------------------------------------+
| WZORZEC: [plandeka v]            | BADANY: naczepa_017.bmp               |
| (zmień z listy → „chłodnia”)     |                                       |
| ┌──────────────────────────┐     | ┌──────────────────────────┐          |
| │ obraz wzorca              │ ⇄  | │ obraz z ramkami 1..4      │          |
| │ (te same miejsca szare)   │ wspólne│ ramka 1 czerwona         │          |
| └──────────────────────────┘ przewijanie└──────────────────────┘          |
+----------------------------------+---------------------------------------+
| Miejsce 1 podwójna podłoga: [Zatwierdź] [Odrzuć → powód v]  | 2 | 3 | 4    |
| Przejrzano 0 z 4  Narzędzie pokazuje, gdzie obraz różni się od wzorca —   |
| tam warto spojrzeć jeszcze raz.                                           |
+--------------------------------------------------------------------------+
```
Główna ścieżka: wczytaj → zobacz oba obrazy → sprawdź, czy wzorzec to właściwy typ (zmień z listy) → decyzje pod obrazami → zapis raportu.
Pierwsze widać: dwa obrazy obok siebie, ramki po prawej.

## Uwagi dla Programisty
- Wszystkie trzy mają mieć te same 4 gotowe obrazy (a)–(d) z §7.2 i ten sam raport.
- Link do każdej makiety osobno; Artur dostanie je razem (3 linki).
- UPROSZCZENIE: szkice tekstowe zamiast makiet graficznych — makiety robi Programista — brak dorabiania.

<!-- skill: przeplywy-pm -->
