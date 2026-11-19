# 01 — Analiza konkurencji (`/competitive-analysis`)

Źródła: `docs/zadanie.md`, `docs/materialy.md`, `docs/decyzje.md` (P3: szukamy sami; P4: **B** — liczy się skuteczność, przede wszystkim żeby nie przeoczyć skrytki; P5: **A** — analiza służy uzasadnieniu wyróżnika w opisie i na pokazie).
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
| Metoda | Jak działa | Plus | Minus / ryzyko dla nas |
|---|---|---|---|
| **Różnica pikselowa po wyrównaniu** (rejestracja, np. korelacja fazowa) | odjęcie wzorca od obrazu po wyrównaniu; różnica = kandydat | prosta, szybka, nie wymaga uczenia, wprost pasuje do pary „wzorzec–badany”; w ACXIS i patentach ([przykład](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5910973)) | wrażliwa na przesunięcia, skalę, szum → fałszywe alarmy; wzorzec musi być dopasowany do typu naczepy |
| **Korelacja okno po oknie** (Zheng i in., w tym samym przeglądzie UCL) | lokalna korelacja z wzorcem | odporniejsza na szum niż piksel | wolniejsza, słabsza na drobiazgach |
| **Autoenkoder / rekonstrukcja** | sieć uczona na czystych; duży błąd rekonstrukcji = anomalia | uczy się tylko na czystych (zgodnie z §5 zadania), bez przykładów anomalii | małe skrytki giną w uśrednieniu; próg trudny |
| **Pamięć cech normalnych (typ PatchCore)** | porównanie cech fragmentów z bazą normalnych | silna w przemyśle, bez etykiet | **nie znalazłem testu na RTG ładunków**; może mylić się na zróżnicowanych scenach (wnioskowanie, nie wynik) |
| **Nienadzorowana segmentacja anomalii** ([źródło](https://arxiv.org/pdf/2107.07333)) | maska anomalii bez etykiet (bagaż) | daje obszary do zaznaczenia (W4) | bagaż ≠ naczepa |
| **Klasyfikacja „pusty / niepusty”** | etykieta całego obrazu | prosta | nie lokalizuje (nie spełnia W4/W10) |
| **Detektor obiektów uczony na dodatkach** | wykrywa znane klasy | wysoka czułość na znane | wymaga przykładów anomalii — zadanie §5 ich nie gwarantuje |

Wniosek metodyczny: dla zadania (wzorzec + uczenie na czystych + wskazanie miejsca) najbliższe są: **różnica po wyrównaniu** jako podstawa i **model uczony na czystych** jako druga hipoteza do porównania; wybór potwierdzi pomiar FP/FN na zbiorze (decyzje 11:59, typ A). Liczb skuteczności z literatury nie przenoszę na nasze dane (inny zbiór) — jedyna liczba z wyszukiwania: slajd Rapiscan „96% wykrycia przy 3% fałszywych alarmów” dotyczy innego zadania i jest tu tylko przykładem rzędu wielkości (źródło wtórne, nieweryfikowane).

## 6. Porównanie funkcji (soczewka: skuteczność, brak przeoczeń skrytki)
| Zdolność | Nasze rozwiązanie (cel) | Rapiscan | Smiths AXR | Obecne narzędzie KAS |
|---|---|---|---|---|
| Porównanie ze wzorcem i wskazanie różnic | tak (podstawa) | tak (ten sam pojazd) | brak danych | nie |
| Wskazanie miejsca na obrazie | tak (wymóg §3) | tak | brak danych | częściowo (papierosy) |
| Małe skrytki w konstrukcji | cel główny | brak danych | brak danych | słabo (§1) |
| Miara FP/FN na zbiorze testowym | tak (mierzymy) | nie publikuje na naszym zbiorze | nie | nie |
| Praca bez internetu | tak (§9) | zwykle lokalnie, brak danych | brak danych | tak |
| Otwarte, powtarzalne, do oceny | tak | nie | nie | nie |
| Format `.bmp` ~50 MB, partie | tak (wymóg) | brak danych | brak danych | brak danych |

## 7. Szanse wyróżnienia (P5: do opisu i pokazu)
1. **Skrytki, nie tylko papierosy** — nasz cel to drobne przeróbki konstrukcji, gdzie dzisiejsze narzędzie jest słabe (zadanie §1).
2. **Wynik, który można sprawdzić** — raportujemy FP-obraz i FN-obraz oraz czułość wg rozmiaru dodatku (nie obiecujemy bez pomiaru).
3. **Wzorzec z innego pojazdu tego samego typu**, nie tylko „ten sam pojazd przed/po” (zakres Rapiscan Vehicle Compare) — **założenie do potwierdzenia**: zbiór KAS ma pary/grupy „przed i po” (§7).
4. **Działa lokalnie** i **skaluje się partiami** (§3, §9).

## 8. Zagrożenia
1. Rapiscan i inni oferują porównanie od dawna — wyróżnia nas wynik na naszym zbiorze, nie sama idea.
2. Zero fałszywych alarmów (§6) a czułość na małe skrytki (P4: nie przeoczyć) — kompromis do jawnego pokazania.
3. Sztuczny zbiór (decyzje 11:59) może zawyżać wyniki względem prawdziwych obrazów KAS.

## 9. Rekomendacje
- **Postawić na**: różnica po wyrównaniu + czytelne zaznaczenie miejsca + jawny pomiar FP/FN.
- **Nadrobić (wymóg wejścia)**: `.bmp` 50 MB, partie, czas < 1 min.
- **Pominąć**: rozpoznawanie papierosów (robi je istniejące narzędzie) i dopasowanie do manifestu (patenty — poza zadaniem).

## 10. Czego nie wiem o produkcie (lista przed momentem (a))
Każda pozycja to osobne pytanie do Artura z rekomendacją (numery w `docs/decyzje.md`):
1. Kiedy operator sięga po narzędzie: w trakcie oglądania obrazu (podpowiedź) czy po własnej ocenie (kontrola końcowa)?
2. Co dziś najbardziej boli: małe skrytki w konstrukcji pojazdu czy towar ukryty w ładunku?
3. Skąd operator bierze wzorzec: sam wskazuje obraz porównawczy, czy system dobiera go z biblioteki?
Pominięte, bo rozstrzyga zadanie: kto jest użytkownikiem (operator RTG, §1–2); jak sobie dziś radzi (ręcznie + narzędzie do papierosów, §1); praca bez internetu (§9); sztuczne dane (decyzje 11:59).

<!-- skill: przeplywy-pm -->
<!-- skill: competitor-analysis -->

## Recenzja przejścia 1

Porównano z `docs/zadanie.md` i `docs/decyzje.md` (P3–P8; P6–P8 odpowiedziane 12:04, po napisaniu pliku). Listy punktów skilla `przesluchanie-hackathon` nie miałem w klonie — sprawdzone tylko pytania i „pominięte”. Braki od najważniejszego:

1. **produkt** — P8: „system dobiera wzorzec z biblioteki; operator zwykle nie ma czystego zdjęcia tej samej naczepy”. Plik opiera się na „ten sam pojazd przed/po” (tabela §6, §7 pkt 3 jako „założenie do potwierdzenia”, §10 pkt 3 jako pytanie). Odpowiedź je zamyka, ale analiza nie wyciąga wniosku: dobór wzorca z biblioteki jest osobną funkcją (konkurent Rapiscan „Similar Cargo” oraz ACXIS robią to inaczej) i brakuje jej w porównaniu i w „Postawić na”.
2. **produkt** — P7: „oba (skrytki w konstrukcji i towar w ładunku), najczęściej podwójna podłoga albo ściana przy kabinie”. Plik ustawia „cel główny” tylko na małe skrytki w konstrukcji (§6, §7 pkt 1) i pomija towar w ładunku (zadanie §1 mówi o obu) oraz konkretne miejsca (podwójna podłoga, ściana przy kabinie) w porównaniu funkcji i metodach (§5).
3. **produkt** — P6: „w trakcie oglądania obrazu; operator ma kilka minut na auto”. Plik tego nie uwzględnia: brak wymogu czytelności zaznaczeń na żywo i czasu odpowiedzi względem „kilku minut” (zadanie §7: < 1 min) w szansach i rekomendacjach; §10 nadal wylicza pytania 1–3 jako niewiadome, choć P6–P8 zamknięte.
4. **technika** — sprzeczność wewnątrz pliku: §7 pkt 4 „skaluje się partiami” jako szansa wyróżnienia, a §9 „Nadrobić (wymóg wejścia): partie” — brak wyniku, który to potwierdza (P11 czeka; wyróżnikiem nie jest nic, co niezmierzone). Ujednolicić: wymóg, nie wyróżnik.
5. **technika** — liczba „96% wykrycia przy 3% fałszywych alarmów” (§5) pochodzi ze źródła wtórnego, nieweryfikowanego, bez linku; liczbę bez źródła usunąć albo podać źródło. Do tego P4 B („nie przeoczyć”) kontra §6 zadania („na czystych nic”): plik nazywa kompromis, ale nie podaje, którą stronę wybieramy, gdy się ścierają (pytanie do Artura — wpis, nie rekomendacja).
