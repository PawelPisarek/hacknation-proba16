# Decyzje

11:59 Szef: start próby 16; zadanie w docs/zadanie.md (dosłownie, bez rozdz. 8 — zna Szef); typ A (wynik mierzony FP/FN na zbiorze czystych i z dodatkami).
11:59 Szef: dane — własny sztuczny zbiór naczep .bmp (czyste / z dodatkami), bo obrazów KAS nie mamy (ustalenie ludzi).
11:59 Szef: liczenie — orkiestrator: na karcie OMENa (--klasa gpu-tlo, GTX 1050 4 GB), nigdy na procesorze; reszta --maszyna dowolna; każdy przebieg ≥ 2 hipotezy naraz.
11:59 Szef: aplikacja pod linkiem dostaje wynik z usługi na karcie OMENa (sieć lokalna).
P1 12:00 Paweł: Kto jest kim w próbie 16? Podaj podpisy urządzeń ludzi (np. „Opera on Mac”, „Artur telefon”) i role; czy jest ktoś poza Tobą i Arturem? — czeka
12:00 Projektant: pominięte (produkt i kategoria dla /competitive-analysis) — z zadania: narzędzie wspierające operatora RTG, porównuje obraz naczepy ze wzorcem i wskazuje „dodatki”
P2 12:00 Artur: Jak podpisuje się Twoja wiadomość w tym pokoju (nazwa urządzenia, np. „Opera on Mac”)? — czeka
P3 12:00 Artur: Czy sami szukamy podobnych rozwiązań do porównania (obecne narzędzie KAS do papierosów, gotowe systemy skanerów, ogólne podejścia)? — czeka
P4 12:00 Artur: Co ma być głównym wyznacznikiem porównania: (A) co widzi operator i na ile ufa wskazaniu (czytelność zaznaczeń, mało fałszywych alarmów), czy (B) sama skuteczność wykrywania w liczbach? — czeka
P5 12:00 Artur: Do czego posłuży to porównanie: (A) do uzasadnienia, czym się wyróżniamy w opisie i na pokazie, czy (B) do wyboru funkcji? — czeka
12:01 Szef: trafienie przy liczeniu FN/FP — zaznaczenie trafia dodatek, gdy IoU ≥ 0,1 z ramką prawdy albo środek zaznaczenia leży w ramce dodatku; czysty obraz z ≥ 1 zaznaczeniem = FP obrazowy (propozycja Analityka z docs/materialy.md, zadanie §6 nie rozstrzyga).
P1 12:01 odpowiedź: Paweł — technika (rozmowa z Szefem), Artur — produkt (pokój Produkt), nikt więcej; podpisy urządzeń nieważne.
P2 12:01 odpowiedź: nieważne — pisze Artur (Artur w pokoju)
P3 12:01 odpowiedź: tak, szukamy sami (Artur w pokoju)
P4 12:01 odpowiedź: B — skuteczność, przede wszystkim żeby nie przeoczyć skrytki (Artur w pokoju)
P5 12:01 odpowiedź: A — uzasadnienie wyróżnika w opisie i na pokazie (Artur w pokoju)
P2 12:02 odpowiedź: zbędne — P1 (Paweł) (zamknięte na zlecenie Szefa)
12:02 Szef: cofnięte przez Szefa — wpis 12:01 o trafieniu (IoU/środek w ramce) to parametr produktu; idzie do Artura jako P (Projektant); do odpowiedzi skrypt oceny liczy obie miary (IoU ≥ 0,1 i środek w ramce) obok siebie.
12:03 Projektant: pominięte (perspektywa porównania, cel analizy) — z P4/P5; (kto jest użytkownikiem, jak sobie radzi dziś, praca offline, sztuczne dane) — z zadania §1–2, §9 i decyzji 11:59
P6 12:03 Artur: Kiedy operator sięga po narzędzie: (A) w trakcie oglądania obrazu, jako podpowiedź, czy (B) po własnej ocenie, jako kontrola końcowa? — czeka
P7 12:03 Artur: Co dziś najbardziej boli: (A) małe skrytki w konstrukcji pojazdu, czy (B) towar ukryty w samym ładunku? — czeka
P8 12:03 Artur: Skąd operator bierze obraz wzorcowy: (A) sam wskazuje obraz porównawczy, czy (B) system dobiera go z biblioteki? — czeka
12:03 Szef: recenzja 1 docs/hacktribe.md (Analityk, 263c9aa) — 5 braków; 1–3 „produkt” → Projektant pyta Artura; 4–5 technika → Prezenter.
12:03 Szef: nazwa zespołu „Hackathon” (ustalenie Pawła z poprzednich prób); nazwa projektu — otwarta do kroku 6 (product-name); w opisie HackTribe nie podajemy reguły trafienia (czeka P6), tylko po wyniku FP/FN.
P9 12:03 Artur: Kiedy uznajemy, że narzędzie wskazało skrytkę: (A) wystarczy, że zaznaczenie choć częściowo nachodzi na skrytkę albo jego środek leży w skrytce, czy (B) zaznaczenie musi objąć większą część skrytki? Obraz bez dodatków z choćby jednym zaznaczeniem liczymy jako fałszywy alarm. — czeka
P10 12:03 Artur: Jak opisujemy obecne narzędzie KAS: (A) zgodnie z zadaniem — papierosy wykrywa, ale przy małych ilościach ukrytych w konstrukcji pojazdu jest za słabe, czy (B) inaczej? — czeka
P11 12:03 Artur: Czy w opisie już teraz obiecujemy obsługę dużych plików i wielu obrazów naraz: (A) wpisujemy to dopiero, gdy zmierzymy, a teraz zostaje miejsce na liczby, czy (B) obiecujemy od razu? — czeka
P12 12:03 Artur: Czy szukamy: (A) tylko dodatków w ładunku i konstrukcji, a przeróbki konstrukcji (skrytki wbudowane w ramę) pokazujemy jako to, co narzędzie wskaże przy okazji, bez obietnicy, czy (B) obiecujemy też przeróbki konstrukcji? — czeka
P6 12:04 odpowiedź: A — w trakcie oglądania obrazu; operator ma kilka minut na auto (Artur w pokoju)
P7 12:04 odpowiedź: oba (skrytki w konstrukcji i towar w ładunku), najczęściej podwójna podłoga albo ściana przy kabinie (Artur w pokoju)
P8 12:04 odpowiedź: B — system dobiera wzorzec z biblioteki; operator zwykle nie ma czystego zdjęcia tej samej naczepy (Artur w pokoju)
12:04 Szef: krok 1a — docs/pm/01-competitive-analysis.md ze znacznikiem przeplywy-pm; recenzja przejścia runda 1 → Analityk.
12:04 Projektant: pominięte (cena, wejście na rynek w perspektywie porównania) — z zadania §9: narzędzie wewnętrzne KAS, wdrożenie przez usługodawców IT KAS, nie sprzedajemy
12:04 Projektant: recenzja 1a runda 1 (Analityk): brak 1 (zawężenie zakresu) — z P7 (oba), zakres poszerzony; brak 2 (wzorzec) — z P8 (biblioteka), sprzeczność z zadaniem §7 oznaczona jako założenie; brak 3 (liczba 96%) — usunięta; brak 4 — dodana kolumna wykonalności (założenia do pomiaru); brak 5 — linia „pominięte” powyżej
P13 12:05 Artur: Gdy nie da się mieć obu naraz, co ważniejsze: (A) nie przeoczyć skrytki, nawet kosztem kilku fałszywych alarmów na czystych obrazach, czy (B) zero fałszywych alarmów na czystych, nawet kosztem pominięcia najmniejszej skrytki? — czeka
12:05 Projektant: recenzja 1a runda 2 braki produkt 1–3 przyjęte: dobór wzorca (P8) jako osobna funkcja w porównaniu i rekomendacjach; miejsca z P7 w metodach i rekomendacjach; P6 (na żywo, < 1 min) w szansach i rekomendacjach; §10 przepisany (zamknięte P6–P8, otwarte P9–P13); partie z wyróżnika na wymóg
12:06 Szef: 1a recenzja przejścia runda 1 (Analityk, 891cada) — 5 braków; 1–3 to nieuwzględnione odpowiedzi Artura P6–P12 (bez nowych pytań), 4–5 technika; poprawka → Projektant.
12:06 Projektant: 1a — sekcje „Recenzja przejścia” usunięte z pliku kroku (zapis recenzji w historii git: 891cada, 0d9c8eb); liczba 96%/3% usunięta, brak źródła; priorytet przy kolizji celów: mniej przeoczeń (P4 B). Odpowiedzi P9–P12 w tym dzienniku jeszcze nie ma — nie wpisuję.
12:06 Szef: docs/hacktribe.md poprawka 1 (Prezenter, e7fbbde, wg P8, P10–P12) → recenzja 2 (Analityk).
P9 12:07 odpowiedź (Artur w pokoju): A — wystarczy, że zaznaczenie choć częściowo nachodzi na skrytkę albo jego środek leży w skrytce.
P10 12:07 odpowiedź (Artur w pokoju): A — KAS papierosy wykrywa, ale przy małych ilościach ukrytych w konstrukcji pojazdu jest za słabe.
P11 12:07 odpowiedź (Artur w pokoju): A — dużych plików i wielu obrazów naraz nie obiecujemy, dopóki nie zmierzymy; zostaje miejsce na liczby.
P12 12:07 odpowiedź (Artur w pokoju): B — obiecujemy też przeróbki konstrukcji; podwójna podłoga to najczęstszy przypadek (P7), bez tego narzędzie nie ma sensu.
12:07 Projektant: 1a runda 3 (Analityk): P12 B uwzględnione (przeróbki konstrukcji obiecujemy), P9–P11 w §10, §5 oznaczone jako hipoteza
12:07 Szef: recenzja 2 docs/hacktribe.md (Analityk, 67e6458) — braki 1–2 zamknięte odpowiedziami Artura P8 B i P12 B (odpowiedź zamyka punkt; bez ponownego pytania); jak sprawdzimy przeróbki konstrukcji → generator ma przeróbki z ramką prawdy i skrypt liczy je jak dodatki (Programista); brak 3 i 4 → Prezenter (krótko: podpowiedź w trakcie oglądania; liczby po pomiarze, skrócić tekst pod nie); brak 5 → Projektant wpisuje P9–P12.
P13 12:08 odpowiedź (Artur w pokoju): A — nie przeoczyć skrytki, nawet kosztem kilku fałszywych alarmów (zgodnie z P4); zaznaczeń na auto ma być kilka, nie kilkadziesiąt.
12:08 Szef: docs/hacktribe.md poprawka 2 (Prezenter, 886d666, 817 zn.) — braki recenzji 2 zamknięte (P9–P12 już wpisane przez Projektanta); recenzja 3 po pierwszym pomiarze FP/FN.
12:08 Szef: 1a — Projektant melduje v5 (75c848a) ze znacznikiem przeplywy-pm i zamkniętą pętlę (runda 3 Analityka na v4); werdykt nie jest zapisany w repo → Analityk potwierdza różnicę v4→v5 i zapisuje werdykt; 1b /discover (pytania a, b) startuje równolegle.
12:09 Programista: założenie (technika) — obraz 8-bit szary .bmp, pełny rozmiar 10000×5000 px = 50 MB; zbiór „male” 2000×1000 do szybkich przebiegów, „pelne” do pomiaru czasu; generator deterministyczny (ziarno 16), rtg/generator.py.
12:09 Programista: założenie (technika) — zgodnie z P8 B biblioteka = czyste egzemplarze każdego typu naczepy (inne niż w testach: wymiary ±2–3 px, gęstość ±4%, przesunięcie, rozciągnięcie 0,97–1,03, obrót ±0,25°, jasność ±7%, szum); testy = inne egzemplarze; dobór wzorca automatyczny (korelacja miniatury po wyrównaniu).
UPROSZCZENIE: deklarowany ładunek (palety) w testach — pominięty: testy to puste naczepy, „dodatki w ładunku” = obce paczki w przestrzeni ładunkowej — dorobienie: ładunek zmienny między wzorcem a obrazem wymaga osobnej metody (segmentacja ładunku), ~pół dnia.
12:09 Programista: ocena — główna miara P9 A (nachodzi choć częściowo albo środek w ramce), obok IoU ≥ 0,1; FN razem i osobno: przeróbki konstrukcji / ładunek / małe; FP obrazowy = czysty z ≥ 1 zaznaczeniem (rtg/ocena.py).
12:09 Programista: przebieg 1 (karta, jeden przebieg) — hipotezy: (A) samo przesunięcie globalne wystarczy na niskie FP [H1]; (B) tolerancja krawędzi 5×5 obniża FP bez wzrostu FN [H1t]; (C) skala osi jazdy + lokalne pole przesunięć obniża FP dalej [H2]; (D) mapa zmienności z biblioteki obniża FP bez straty skrytek [H2n]; (E) minimum różnic do 3 wzorców obniża FP [H2k]; (F) dobór wzorca z biblioteki trafia typ; (G) czas < 60 s na obraz 50 MB na GTX 1050.
12:09 Szef: krok 6 (nazwa, hasło → docs/nazwa.md) zlecony Prezenterowi; wybór nazwy pójdzie do Artura.
12:10 Szef: 1a zamknięte — v5 75c848a, znacznik przeplywy-pm, Recenzja przejścia 3 (Analityk, 5117f52): brak braków zmieniających zakres lub kryteria.
12:11 Szef: krok 6 — docs/nazwa.md (fd37b90, znaczniki product-name, value-prop-statements); recenzja 1 → Analityk; wybór nazwy → Artur jako P14 (Projektant). Duplikatu P1 w decyzje.md już nie ma.
P14 12:11 Artur: Jak nazwiemy projekt: „Skrytka.AI”, „Wzorzec” czy „Prześwit”? (rekomendacja: Skrytka.AI — „Pokazuje operatorowi to, czego nie ma we wzorcu.”, operator od razu rozumie, o co chodzi) — czeka
12:12 Projektant: dopisek do P14 (recenzja 1 nazwa.md, Analityk 3d10a77): „Skrytka.AI” sugeruje tylko skrytki, a P7 i P12 obejmują też towar w ładunku — czy to przeszkadza w wyborze nazwy?
P15 12:12 Artur: W tekstach mówimy (A) „zaznacza tylko różnice, na czystym aucie nic” czy (B) „kilka zaznaczeń na auto” (z P13)? Rekomendacja: A — B brzmi jak obietnica fałszywych alarmów na czystym aucie — czeka
P16 12:12 Artur: Teksty piszemy (A) ostrożnie: „system sam dobiera wzorzec z biblioteki”, bez „każdy obraz” i „bez zdjęcia czystej naczepy”, czy (B) śmiało, jak teraz? Rekomendacja: A — tego jeszcze nie zmierzyliśmy — czeka
12:12 Szef: nazwa.md recenzja 1 (3d10a77, 5 braków): 1–3 produkt → Artur przez Projektanta (1 w P14); 4–5 technika → Prezenter. Znaczniki skilli na górze pliku zostają (format zlecenia Szefa).
12:12 Prezenter: nazwa.md/hacktribe.md — poprawione braki 4–5 recenzji 1 (lista kandydatów zgodna: Skrytka.AI, Wzorzec, Prześwit; uzasadnienie „skrytki” bez „słowa operatora”); nazwy nie wybrano, czeka P14; braki 1–3 (produkt) po odpowiedzi Artura.
P14 12:13 odpowiedź (Artur w pokoju): „Prześwit” — krótkie, kojarzy się z RTG i nie obiecuje AI wprost. Dopisek (12:12) bez znaczenia: wybrana nazwa nie sugeruje samych skrytek.
P15 12:14 odpowiedź (Artur w pokoju): ani A, ani B — w tekstach: „zaznacza miejsca różne od wzorca” + liczba z pomiaru (A obiecuje niezmierzone, a w P13 Artur zgodził się na kilka fałszywych alarmów).
P16 12:14 odpowiedź (Artur w pokoju): A — ostrożnie: „system sam dobiera wzorzec z biblioteki”, bez „na każdy obraz” i „bez zdjęcia czystej naczepy”.
12:13 Szef: poprawiona linia dopisku do P14 (nie jest pytaniem, bez „czeka”). P14 zamknięte: Prześwit (Artur w pokoju) → Prezenter wpisuje nazwę w docs/hacktribe.md i docs/nazwa.md.
12:14 Prezenter: wybrana nazwa Prześwit (P14) wpisana w docs/hacktribe.md i docs/nazwa.md; hasło „Zaznacza na obrazie RTG miejsca różne od wzorca.” (50 zn., wg P15/P16); opisu i wartości nie zmieniam do osobnego zlecenia.
12:14 Szef: P15, P16 zamknięte (Artur w pokoju) → Prezenter wpisuje je razem z P14 w docs/hacktribe.md i docs/nazwa.md; potem recenzja 2 (Analityk).
