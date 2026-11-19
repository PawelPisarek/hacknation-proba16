# 01 — Analiza konkurencji (`/competitive-analysis`)

Źródła: `docs/zadanie.md`, `docs/materialy.md`, `docs/decyzje.md` (P3: szukamy sami; P4: **B** — liczy się skuteczność, przede wszystkim żeby nie przeoczyć skrytki; P5: **A** — analiza służy uzasadnieniu wyróżnika w opisie i na pokazie; P6: narzędzie podpowiada w trakcie oglądania obrazu; P7: boli oba — skrytki w konstrukcji i towar w ładunku, najczęściej podwójna podłoga albo ściana przy kabinie; P8: wzorzec system dobiera z biblioteki, bo operator zwykle nie ma czystego zdjęcia tej samej naczepy).
Wyszukiwanie w sieci: listopad 2026, wyniki ze źródeł publicznych (linki w tekście). **Czego nie znalazłem, jest powiedziane wprost** (np. Nuctech, Multicontrol).

## 1. Kontekst (z zadania, bez pytań)
Produkt: narzędzie dla operatora RTG KAS: porównuje obraz naczepy ze wzorcem i wskazuje „dodatki” (możliwy przemyt). Kategoria: automatyczne wspomaganie analizy obrazów RTG środków przewozowych. Soczewka (P4): **skuteczność wykrycia, z naciskiem na brak przeoczeń skrytki**; zadanie dodatkowo wymaga zero fałszywych alarmów na czystych obrazach (§6) — te dwa cele się ścierają (patrz ryzyka w `docs/materialy.md` pkt 6).

## 2. Przegląd rynku
Automatyczna analiza obrazów RTG ładunków jest wg przeglądu [Automated X-ray Image Analysis for Cargo Security (UCL)](https://arxiv.org/pdf/1608.01017) dziedziną względnie niedojrzałą. Dostawcy skanerów dają dziś narzędzia „dla operatora”: rozpoznawanie pustych kontenerów, papierosów, niejednorodnego ładunku, porównanie z poprzednim obrazem. Dwie główne rodziny podejść: (a) porównanie z obrazem odniesienia po wyrównaniu, (b) uczenie wyłącznie na obrazach normalnych i wykrywanie odstępstw.

## 3. Konkurenci bezpośredni (ta sama kategoria, ten sam kupiec: służby graniczne/celne)
| Konkurent | Co robi | Mocna strona | Słabość / luka względem zadania |
|---|---|---|---|
| **Rapiscan InSight — Vehicle Compare** ([źródło](https://www.rapiscan-ase.com/products/software/insight-operator-assist-tools)) | porównuje bieżący pojazd z ostatnim obrazem odniesienia tego samego pojazdu i podświetla różnice | gotowy produkt, wprost to samo zadanie | wymaga wcześniejszego obrazu tego samego pojazdu; zamknięty, płatny, nie wiem czy działa na skanerach Nuctech/Multicontrol (**brak danych**) |
| **Rapiscan InSight — Empty Container / algorytmy anomalii** (to samo źródło) | ocena „pusty / nie” z poziomem pewności; algorytmy intensywności, tekstury, kształtu | prosta decyzja, pewność | decyzja zgrubna (cały kontener), nie lokalizacja małej skrytki w konstrukcji |
| **Rapiscan — Similar Cargo** (to samo źródło) | wyszukuje podobne zapisane obrazy do zestawienia obok siebie | wspiera ludzką ocenę | nie wskazuje różnic sam |
| **Smiths Detection — AXR** ([broszura](https://www.smithsdetection.com/media/iqxlbucf/securing-sea-and-land-borders-smiths-detection-ports-borders-digital-brochure.pdf)) | rozpoznanie papierosów, niejednorodny ładunek, pusty/częściowo pusty kontener | pokrywa te same kategorie co obecne narzędzie KAS | nie wiem, czy lokalizuje drobne przeróbki konstrukcji (**brak danych**); zamknięty |
| **Nuctech** (dostawca skanerów KAS, §1) | — | — | **nie znalazłem publicznych informacji o ich module porównania obrazów**; nie oceniam |
| **Multicontrol** (dostawca skanerów KAS) | — | — | **nie znalazłem** publicznych informacji; nie oceniam |

## 4. Konkurenci pośredni (inne podejście, to samo zadanie „znajdź to, czego nie powinno tu być”)
| Podejście | Opis | Plus | Minus |
|---|---|---|---|
| **Obecne narzędzie KAS (papierosy)** (zadanie §1) | wykrywa papierosy w pojazdach i towarze | działa w produkcji | słabe przy małych ilościach w konstrukcji (zadanie §1) — to nasza luka |
| **Praca ręczna operatora** | ocena obrazu okiem | elastyczna | zmęczenie, przeoczenia małych detali |
| **ACXIS — porównanie obrazów ze wzorcem z bazy** ([projekt UE](https://openaccessgovernment.org/automated-comparison-x-ray-images-cargo-scanning-acxis/25162)) | niezależna od producenta baza wzorców, obraz różnicowy po rejestracji | otwarta idea, to samo co nasz wzorzec | projekt badawczy, nie produkt |

Podejścia wschodzące (badania): uczenie wyłącznie na normalnych obrazach — m.in. detekcja anomalii na patchach dla kontenerów (Andrews i in., cytowane w [UCL](https://discovery.ucl.ac.uk/id/eprint/10062484/1/2nd%20revision%20in%20template%2002.pdf)), [nienadzorowana segmentacja anomalii w bagażu](https://arxiv.org/pdf/2107.07333) i [przegląd uczenia głębokiego w RTG](https://arxiv.org/pdf/2001.01293).

## 5. Przegląd metod wykrywania różnic i anomalii na obrazach RTG
| Metoda | Jak działa | Plus | Minus / ryzyko dla nas | Wykonalność (czas < 1 min, 50 MB, karta 4 GB, offline) |
|---|---|---|---|---|
| **Różnica pikselowa po wyrównaniu** (rejestracja, np. korelacja fazowa) | odjęcie wzorca od obrazu po wyrównaniu; różnica = kandydat | prosta, szybka, nie wymaga uczenia, wprost pasuje do pary „wzorzec–badany”; w ACXIS i patentach ([przykład](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5910973)) | wrażliwa na przesunięcia, skalę, szum → fałszywe alarmy; wzorzec musi być dopasowany do typu naczepy | tania; kafelki/partie, offline; założenie do pomiaru |
| **Korelacja okno po oknie** (Zheng i in., w tym samym przeglądzie UCL) | lokalna korelacja z wzorcem | odporniejsza na szum niż piksel | wolniejsza, słabsza na drobiazgach | średni koszt; do pomiaru przy 50 MB |
| **Autoenkoder / rekonstrukcja** | sieć uczona na czystych; duży błąd rekonstrukcji = anomalia | uczy się tylko na czystych (zgodnie z §5 zadania), bez przykładów anomalii | małe skrytki giną w uśrednieniu; próg trudny | uczenie na karcie 4 GB tylko na kafelkach; wagi lokalne; założenie do pomiaru |
| **Pamięć cech normalnych (typ PatchCore)** | porównanie cech fragmentów z bazą normalnych | silna w przemyśle, bez etykiet | **nie znalazłem testu na RTG ładunków**; może mylić się na zróżnicowanych scenach (wnioskowanie, nie wynik) | cechy wymagają lokalnych wag; pamięć/czas do pomiaru |
| **Nienadzorowana segmentacja anomalii** ([źródło](https://arxiv.org/pdf/2107.07333)) | maska anomalii bez etykiet (bagaż) | daje obszary do zaznaczenia (W4) | bagaż ≠ naczepa | jw., cięższa; do pomiaru |
| **Klasyfikacja „pusty / niepusty”** | etykieta całego obrazu | prosta | nie lokalizuje (nie spełnia W4/W10) | lekka, ale nie lokalizuje |
| **Detektor obiektów uczony na dodatkach** | wykrywa znane klasy | wysoka czułość na znane | wymaga przykładów anomalii — zadanie §5 ich nie gwarantuje | wymaga etykiet anomalii, których nie mamy (§5) |

Miejsca z P7 (podwójna podłoga, ściana przy kabinie) to obszary, gdzie wzorzec różni się najmniej od badanego obrazu — tam metody różnicowe są najbardziej narażone na fałszywe alarmy z powodu przesunięć; w pomiarze raportujemy wynik osobno dla dodatków w konstrukcji i w ładunku (założenie, do potwierdzenia na zbiorze).

Wniosek metodyczny: dla zadania (wzorzec + uczenie na czystych + wskazanie miejsca) najbliższe są: **różnica po wyrównaniu** jako podstawa i **model uczony na czystych** jako druga hipoteza do porównania; wybór potwierdzi pomiar FP/FN na zbiorze (decyzje 11:59, typ A). Liczb skuteczności z literatury nie przenoszę na nasze dane (inny zbiór) — liczb skuteczności konkurentów tu nie podaję (brak weryfikowalnego źródła).

## 6. Porównanie funkcji (soczewka: skuteczność, brak przeoczeń skrytki)
| Zdolność | Nasze rozwiązanie (cel) | Rapiscan | Smiths AXR | Obecne narzędzie KAS |
|---|---|---|---|---|
| Porównanie ze wzorcem i wskazanie różnic | tak (podstawa) | tak (ten sam pojazd) | brak danych | nie |
| **Dobór wzorca z biblioteki** (operator nie wskazuje go sam — P8; zwykle nie ma zdjęcia tej samej naczepy) | cel (osobna funkcja: system wybiera najbliższy wzorzec tego typu naczepy) | częściowo: „Similar Cargo” podsuwa podobne obrazy do oglądania obok siebie, nie liczy różnic | brak danych | nie |
| Czytelność zaznaczeń w trakcie oglądania i czas odpowiedzi (P6: kilka minut na auto; zadanie §7: < 1 min) | cel: zaznaczenia widoczne od razu na obrazie operatora, wynik w < 1 min | brak danych | brak danych | nie dotyczy |
| Wskazanie miejsca na obrazie | tak (wymóg §3) | tak | brak danych | częściowo (papierosy) |
| Skrytki w konstrukcji (podwójna podłoga, ściana przy kabinie — P7) i towar w ładunku | cel (oba, P7) | brak danych | brak danych | słabo przy małych ilościach w konstrukcji (§1) |
| Miara FP/FN na zbiorze testowym | tak (mierzymy) | nie publikuje na naszym zbiorze | nie | nie |
| Praca bez internetu | tak (§9) | brak danych | brak danych | tak |
| Otwarte, powtarzalne, do oceny | tak | nie | nie | nie |
| Format `.bmp` ~50 MB, partie | tak (wymóg) | brak danych | brak danych | brak danych |

## 7. Szanse wyróżnienia (P5: do opisu i pokazu)
1. **Skrytki w konstrukcji obok towaru w ładunku** (P7: oba) — tam, gdzie dzisiejsze narzędzie do papierosów jest słabe (zadanie §1); wskazujemy różnice względem wzorca, nie tylko papierosy.
2. **Wynik, który można sprawdzić** — raportujemy FP-obraz i FN-obraz oraz czułość wg rozmiaru dodatku (nie obiecujemy bez pomiaru).
3. **Wzorzec z biblioteki dla naczepy tego samego typu** (P8: operator zwykle nie ma czystego zdjęcia tej samej naczepy), a nie tylko „ten sam pojazd przed/po” (zakres Rapiscan Vehicle Compare). Uwaga: zadanie §7 opisuje dane jako pary/grupy „przed i po”; biblioteka wzorców z naszego zbioru to założenie wykonawcze do sprawdzenia w makiecie i danych.
4. **Podpowiedź w trakcie oglądania obrazu** (P6): operator ma kilka minut na auto, więc zaznaczenia muszą być czytelne od razu, a wynik w < 1 min (zadanie §7). To wymóg użyteczności, a wyróżnik tylko jeśli pokażemy to w demo.
5. **Działa lokalnie** (§3, §9). Obsługa partii i dużych plików to wymóg wejścia (§9), nie wyróżnik, dopóki nie zmierzymy (P11 czeka).

## 8. Zagrożenia
1. Rapiscan i inni oferują porównanie od dawna — wyróżnia nas wynik na naszym zbiorze, nie sama idea.
2. Zero fałszywych alarmów (§6) a czułość na małe skrytki (P4: nie przeoczyć) — kompromis do jawnego pokazania; przy konflikcie priorytetem jest mniej przeoczeń (P4: B, Artur: „żeby nie przeoczyć skrytki”); P13 to potwierdzi lub zmieni.
3. Sztuczny zbiór (decyzje 11:59) może zawyżać wyniki względem prawdziwych obrazów KAS.

## 9. Rekomendacje
- **Postawić na**: różnica po wyrównaniu ze wzorcem dobieranym z biblioteki + czytelne zaznaczenie miejsca + jawny pomiar FP/FN.
- **Zrobić jako osobną funkcję**: dobór wzorca z biblioteki (P8) — z możliwością pokazania operatorowi, który wzorzec wybrano.
- **Zadbać o użycie na żywo** (P6): czytelne zaznaczenia od razu, wynik w < 1 min.
- **Nadrobić (wymóg wejścia)**: `.bmp` 50 MB, partie, czas < 1 min.
- **Pominąć**: dopasowanie do manifestu (patenty — poza zadaniem). Cel obejmuje oba rodzaje ukrycia i oba miejsca z P7 (podwójna podłoga, ściana przy kabinie). Papierosów nie wyłączamy z zakresu (P7: boli także towar w ładunku); rozpoznawanie papierosów robi dziś osobne narzędzie KAS i go nie powielamy.

## 10. Czego nie wiem o produkcie
Zamknięte (odpowiedzi Artura): P6 — w trakcie oglądania obrazu, kilka minut na auto; P7 — oba rodzaje ukrycia, najczęściej podwójna podłoga albo ściana przy kabinie; P8 — wzorzec dobiera system z biblioteki.
Otwarte (osobne pytania do Artura z rekomendacją, numery w `docs/decyzje.md`): P9 — kiedy uznajemy trafienie w skrytkę; P10 — jak opisujemy obecne narzędzie KAS; P11 — obietnica dużych plików i partii; P12 — czy obiecujemy przeróbki konstrukcji; **P13 — którą stronę wybieramy, gdy „nie przeoczyć skrytki” (P4) ściera się z „zero fałszywych alarmów na czystych” (zadanie §6)**.
Pominięte, bo rozstrzyga zadanie: cena i wejście na rynek (narzędzie wewnętrzne KAS, wdrożenie przez usługodawców IT KAS — §9); kto jest użytkownikiem (operator RTG, §1–2); jak sobie radzi dziś (ręcznie + narzędzie do papierosów, §1); praca bez internetu (§9); sztuczne dane (decyzje 11:59).

<!-- skill: przeplywy-pm -->
<!-- skill: competitor-analysis -->
