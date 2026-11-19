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
12:14 Prezenter: P15/P16 uwzględnione w opisie HackTribe i wartości w nazwa.md (zaznacza miejsca różne od wzorca; system sam dobiera wzorzec z biblioteki; liczba z pomiaru [__]); opis 819 zn.
12:15 Szef: nazwa i HackTribe wg P14–P16 (Prezenter 3061476; hasło „Zaznacza na obrazie RTG miejsca różne od wzorca.”, opis 819 zn.) → recenzja 2 (Analityk).
12:16 Szef: nazwa/HackTribe recenzja 2 (4c7a0b8, 4 braki): 1 produkt → Artur przez Projektanta; 2–4 technika → Prezenter. Domeny i znaku towarowego nie sprawdzamy w DRAFT (Szef).
P17 12:16 Artur: Zdanie dla operatora „Łatwiej zauważysz małą skrytkę…, bo narzędzie pokazuje ci, gdzie spojrzeć jeszcze raz” obiecuje skuteczność, której nie zmierzyliśmy. (A) piszemy ostrożnie: „narzędzie pokazuje, gdzie obraz różni się od wzorca — tam warto spojrzeć jeszcze raz”, czy (B) zostawiamy jak jest? Rekomendacja: A, zgodnie z P16 — czeka
12:16 Prezenter: recenzja 2 nazwa.md — braki 2–4 (technika) poprawione: hacktribe.md bez sekcji recenzji (263c9aa, 67e6458), nazwa.md hasło 53 zn. i Skrytka.AI odrzucona (P14), opis z „[__] z [__]”; domena/znak poza zakresem DRAFTu; opis 866 zn.
P17 12:18 odpowiedź (Artur w pokoju): A — „narzędzie pokazuje, gdzie obraz różni się od wzorca — tam warto spojrzeć jeszcze raz”. Wynika z P16. Reguła Artura: poprawki tego rodzaju (obietnica niezmierzonej skuteczności) wprowadzamy bez pytania.
12:18 Szef: 1b /discover nie ruszył (brak docs/pm/02 i pytań a, b) → zlecony Projektantowi wprost.
12:18 Szef: P17 A (Artur w pokoju) → Prezenter poprawia zdanie wartości. Zasada Artura: obietnice bez pomiaru poprawiamy na ostrożne (P16) bez pytania — recenzenci nie oznaczają ich jako „produkt”, tylko jako poprawkę wg P16.
12:19 Prezenter: P17 A — zdanie 2 wartości w nazwa.md zastąpione ostrożnym; w hacktribe.md nie było podobnej obietnicy (opis 866 zn.); zasada Artura: niezmierzone obietnice poprawiam od razu na ostrożne (P16).
12:19 Projektant: pominięte (krok 1 /discover: co badamy, co już wiemy, jaką decyzję ustawia) — z zadania §2–3 i P4–P17: narzędzie pokazujące operatorowi miejsca różne od wzorca; decyzja = co wchodzi do pierwszej wersji i pokazu
P18 12:19 Artur: Który zestaw 3–5 pomysłów bierzemy dalej (lista 1–10 w wiadomości w pokoju i w docs/pm/02-discover.md)? Rekomendacja: 1, 2, 3, 4, 10 — czeka
P19 12:19 Artur: Dla jakich pojazdów pokazujemy produkt: (A) tylko naczepy ciężarowe (dla nich mamy zbiór i pokaz), a kontenery, autokary i wagony zapowiadamy jako dalszy krok, czy (B) obiecujemy od razu wszystkie rodzaje z zadania? Rekomendacja: A — czeka
P20 12:19 Artur: Co operator robi z zaznaczeniem: (A) odznacza „sprawdzone / pomyłka”, a raport zapisuje się z miejscem i przedmiotem kontroli, czy (B) tylko ogląda zaznaczenia i pobiera raport? Rekomendacja: B na pierwszą wersję (szybciej, pokaz mieści się w 2 min); A jako następny krok — czeka
12:19 Szef: nazwa.md wg P17 (974d7e9) → recenzja 3 (Analityk), ostatnia runda.
12:20 Prezenter: README.md szkic (Prześwit, wg P16; makieta i ksefbot.pl jako [link po wdrożeniu]; komendy z docs/uruchomienie.md)
P18 12:21 odpowiedź (Artur w pokoju): 1, 2, 3, 4, 6 — strefy ryzyka (6) zamiast tablicy wyników (10), bo podwójna podłoga i ściana przy kabinie to najczęstszy przypadek (P7); liczby z 10 trafiają do opisu, nie jako funkcja.
P19 12:21 odpowiedź (Artur w pokoju): A — tylko naczepy ciężarowe; kontenery, autokary i wagony jako dalszy krok.
P20 12:21 odpowiedź (Artur w pokoju): A — operator zatwierdza albo odrzuca zaznaczenie jednym kliknięciem; raport zapisuje miejsce i przedmiot kontroli (bez tego raport nic nie mówi o kontroli). Wynik z P20: pomysł 7 i zapis raportu (8) wchodzą do pierwszej wersji.
P21 12:21 Artur: Co w wybranych pomysłach (1, 2, 3, 4, 6, 7 z P20) chcesz zmienić albo uprościć? Rekomendacja: nic — pokaz w 2 min mieści się z tym zestawem — czeka
P22 12:21 Artur: Czy któryś odrzucony pomysł warto wziąć w części: 5 (kolor ramki zależny od siły różnicy) albo 9 (kolejka wielu obrazów)? Rekomendacja: 5 w części — kolor ramki tylko dla stref ryzyka (6); 9 nie — czeka
P23 12:21 Artur: Najryzykowniejsze założenia do sprawdzenia najpierw: (Z1) system trafnie dobiera wzorzec z biblioteki (P8), (Z2) podwójną podłogę widać jako różnicę od wzorca, (Z3) przy kilku zaznaczeniach na auto operator im ufa i zdąży je obejrzeć (P13). Czy to te trzy, czy zamieniamy któreś? Rekomendacja: te trzy — czeka
12:21 Szef: krok 6 (nazwa, hasło, DRAFT HackTribe) — recenzja 3 Analityka c3832e5: brak braków zmieniających zakres lub kryteria → zamknięte. Linie wewnętrzne w hacktribe.md („Recenzje 1–2…”, „Poza zakresem DRAFTu…”) pomija człowiek przy wklejaniu; liczby [__] po pomiarze 0P.
12:21 Szef: 1b część 1 (b3e1c04) przyjęta; P18–P20 odpowiedziane, P21–P23 czekają; dokończenie 02-discover po odpowiedziach — Projektant.
P21 12:22 odpowiedź (Artur w pokoju): nic nie zmieniamy w wybranych pomysłach (1, 2, 3, 4, 6, 7).
P22 12:22 odpowiedź (Artur w pokoju): jak rekomendacja — 5 w części (kolor ramki tylko dla stref ryzyka, 6), 9 nie.
P23 12:22 odpowiedź (Artur w pokoju): te trzy założenia w kolejności Z1, Z2, Z3; Z1 i Z2 sprawdzamy jednym przebiegiem.
12:22 Szef: README recenzja 1 (a97a85c) — 5 braków; 1–2 „produkt” już rozstrzygnięte przez Artura (P19 A, P20 A) → Prezenter wpisuje brzmienie z decyzji, bez nowego pytania; 3–5 technika → Prezenter. Potem recenzja 2.
12:22 Prezenter: README poprawiony wg recenzji 1 (P19 A, P20 A, role botów, bez adresów/licencji bez źródła w repo, bez chmury + orkiestrator)
12:23 Szef: README poprawka po recenzji 1 — 8011933; recenzja 2 (Analityk) zlecona.
12:23 Szef: README recenzja 2 (d46b652) — 1 brak techniczny (release-notes bez śladu) → Prezenter; potem recenzja 3 (ostatnia).
12:23 Prezenter: README recenzja 2 — usunięto release-notes; lista pm-skills wg znaczników w docs/
12:24 Szef: README szkic zamknięty — recenzja 3 (6303dee): brak braków zmieniających zakres lub kryteria. Liczby [__] i linki po pomiarze/wdrożeniu.
12:26 Szef: wyjaśnienie do wpisów 12:18 i 12:22 (sygnał „rozstrzygnięte bez Artura”): nie ma w nich decyzji Szefa o produkcie — to wykonanie odpowiedzi Artura w pokoju: P17 A (12:17, z zasadą „takie rzeczy poprawiajcie bez pytania”), P19 A i P20 A (12:21). Nowe pytanie P nie jest potrzebne, bo Artur już odpowiedział.
12:33 Szef: raport Programisty (0P) — przerwane błędem limitu konta Claude (5h = 100%, reset 14:30). W repo jest commit cbd2751 (generator RTG, ocena FP/FN, metody na GPU, docs/uruchomienie.md); cząstkowy wynik przed przerwaniem: H2ko FP 7/20, FN 0/45 — końcowy pomiar bazowy 0P niedomknięty. Wysłano alarm ntfy (202).
P24 12:33 Paweł: Konto Claude (subskrypcja Pawła — testy) osiągnęło 100% limitu 5-godzinnego (reset 14:30), Programista przerwał krok 0P po commicie cbd2751, a wszyscy 4 koledzy są na tym samym koncie. Czy przełączyć zespół (Programista, Projektant, Analityk, Prezenter) na dostępne konto Antigravity i wznowić pracę w nowych wątkach, czy czekamy do 14:30? Rekomendacja: przełączyć zespół na Antigravity (np. Claude Opus/Sonnet 5.5 albo Gemini 4 Neon) i wznowić od razu w nowych wątkach, żeby nie tracić 2 godzin przed 20:00 — czeka
P24 12:44 bez odpowiedzi Paweł → rekomendacja: przełączono domyślny model 4 botów (Programista, Projektant, Analityk, Prezenter) na Antigravity (Gemini 4 Neon High); stare wątki trzymają poprzednie konto Claude, a w tej rozmowie brak możliwości otwierania nowych wątków kolegom — potrzebna interwencja Pawła (nowe wątki dla Projektanta 1b i Programisty 0P albo przywrócenie zlecania w rozmowie Szefa).
14:32 Szef: limit Claude odnowiony (Paweł), zespół z powrotem na Claude — nie przełączamy na Antigravity. Wznowione w wątkach: Projektant 1b (02-discover z P18–P23), Programista 0P (pełny pomiar bazowy FP/FN).
14:33 Projektant: krok 1b zamknięty — docs/pm/02-discover.md kompletny (P18–P23), zakres: 1, 2, 3, 4, 6, 7, 8 + 5 w części
14:33 Szef: 1b przyjęty (78614e2, znacznik przeplywy-pm) → recenzja przejścia 1b runda 1 (Analityk: 02-discover vs 01-competitive-analysis).
14:34 Analityk: recenzja przejścia 1b runda 1 (02-discover.md 78614e2) — 5 braków: 1, 5 produkt (próg 7/10 vs P4/P12; ręczny wybór typu naczepy vs P8 B) → Projektant/Artur; 2–4 technika; docs/recenzje/1b-1.md
14:35 Szef: recenzja 1b runda 1 (74f5420) — 5 braków: 1 i 5 produkt → Projektant pyta Artura (P, jedna wiadomość); 2–4 technika → Projektant poprawia 02-discover; potem runda 2.
P25 14:35 Artur: Podwójna podłoga to główna kryjówka. Narzędzie może jej czasem nie zaznaczyć (przeoczenie). (A) dopuszczamy do 3 przeoczeń na 10 takich przypadków (jak dziś w planie), czy (B) cel to nie przeoczyć żadnej i mówimy to wprost, a liczbę podamy dopiero po pomiarze? Rekomendacja: B — zostawiamy jak jest w P4/P7/P12, bez liczby wymyślonej z góry — czeka
P26 14:35 Artur: Gdy system źle dobierze wzorzec, (A) zostawiamy P8 B — system dobiera sam, operator nie wybiera nic, czy (B) operator może sam wskazać typ naczepy jako zapas? Rekomendacja: A — zostawiamy jak jest (B zmienia to, co operator robi na ekranie) — czeka
14:35 Projektant: recenzja 1b runda 1 (Analityk, 74f5420): braki 2–4 poprawione w 02-discover.md (definicja „zaznaczona” wg P9, próba ≥30 obrazów i wynik „n z N”, czas < 1 min na obraz, Z2b ściana przy kabinie i Z2c towar raportowane osobno, „pokaz do 2 min” = nasze ograniczenie, miara Z3 z kliknięć zatwierdź/odrzuć); braki 1 i 5 → P25, P26 (czekają na Artura)
14:36 Szef: poprawka 1b po recenzji 1 (9d0c1b3) przyjęta; braki 1 i 5 → P25, P26 (Artur, czekają) → recenzja 1b runda 2 (Analityk) teraz; po P25/P26 ewentualna poprawka.
P25 14:37 odpowiedź: B, ale bez obietnicy „żadnej” w tekstach (P15) — cel w specu, w opisie liczba z pomiaru (Artur w pokoju)
P26 14:37 odpowiedź: B — operator zna typ naczepy z dokumentów przewozowych; gdy system dobierze źle, wybiera z listy jednym kliknięciem (Artur w pokoju; zmienia ekran: dodać wybór typu naczepy)
14:37 Analityk: recenzja przejścia 1b runda 2 (02-discover.md 9d0c1b3) — 4 braki, wszystkie technika (Z3 kolejność/kto ocenia, próba ≥30 vs generator 20+20, Z5/Z6 bez eksperymentu, Z2b/Z2c poza P23 i bez gałęzi drzewa); P25/P26 czekają, nieoceniane; docs/recenzje/1b-2.md
14:37 Szef: recenzja 1b runda 2 (da05454) — 4 braki technika → Projektant, runda 3 (ostatnia). Rozstrzygam: (1) Z3 mierzymy po makiecie/MVP — operatora zastępuje Artur przy przeglądzie MVP (kliknięcia zatwierdź/odrzuć); (2) próba = zbiór z generatora Programisty z 0P (liczby z jego pomiaru), bez wymyślonej liczby 30; (3) Z5 kryterium: ≤ 1 kliknięcie na zaznaczenie i < 1 min na obraz; Z6: raport zawiera miejsce i przedmiot kontroli — sprawdzane w teście akceptacji MVP; (4) Z2b, Z2c zostają (wynikają z P7/P12), sprawdzane w tym samym przebiegu co Z2, poza „skokiem wiary” (P23: Z1, Z2, Z3); drzewo decyzji: gałąź dla Z2b/Z2c i czasu, „Z1 nie trzyma” = wzorzec dobrany źle w pomiarze Programisty.
14:38 Projektant: recenzja 1b runda 2 (Analityk, da05454) braki 1–4 poprawione w 02-discover.md wg rozstrzygnięć Szefa 14:37 (Z3 po MVP z Arturem, próba z generatora 0P bez liczby 30, Z5 ≤1 kliknięcie i <1 min, Z6 w teście MVP, Z2b/Z2c w przebiegu Z2 poza skokiem wiary, gałęzie drzewa); wpisane też P25 B i P26 B (wybór typu naczepy zapasem)
14:38 Szef: poprawka 1b po recenzji 2 (26f93d8) z P25 B i P26 B (Artur w pokoju) → recenzja 1b runda 3, ostatnia (Analityk).
14:39 Analityk: recenzja przejścia 1b runda 3 (02-discover.md 26f93d8) — 3 braki (1 produkt: P26 B poza zakresem pierwszej wersji; 2 technika: brak kryterium „nie trzyma”; 3 technika: brak testu wyboru typu); docs/recenzje/1b-3.md
14:40 Szef: P25 B, P26 B → Prezenter dopasowuje README.md i docs/hacktribe.md (bez obietnicy „żadnej”, wybór typu naczepy jako zapas).
14:40 Prezenter: README i hacktribe wg P25 B (liczba przeoczonych podwójnych podłóg z pomiaru [__] z [__], bez „żadnej”) i P26 B (wybór typu naczepy z listy jednym kliknięciem jako zapas); opis 994 zn.
P27 14:40 Artur: Projektant poprawi opis tak, by wybór typu naczepy z listy (Twoja odpowiedź P26 B) był w zakresie pierwszej wersji i dostępny zawsze, nie tylko gdy system się pomyli. Czy po tej poprawce puszczamy dalej do opisu produktu bez kolejnej rundy sprawdzania? Rekomendacja: tak, puszczamy dalej; ewentualne drobne braki zapiszemy jako ryzyka w opisie produktu — czeka
P28 14:40 Paweł: Recenzja przejścia 1b po 3 rundach ma 2 braki techniczne (brak kryterium 'nie trzyma' w drzewie decyzji i brak kryterium dla wyboru typu naczepy). Projektant je poprawia teraz. Czy po poprawce puszczamy dalej do /write-prd bez rundy 4? Rekomendacja: tak — puszczamy dalej, próg 'nie trzyma' ustala Programista po pomiarze 0P, resztę braków zapisujemy jako ryzyka w specu — czeka
14:40 Szef: recenzja 1b runda 3 (c4467ed) — 3 braki (1 produkt, 2 technika) po 3 rundach → P27 (Artur), P28 (Paweł); w tym czasie Projektant poprawia 3 braki w 02-discover (niezależne od odpowiedzi).
14:41 Projektant: recenzja 1b runda 3 (Analityk, c4467ed) braki 1–3 poprawione w 02-discover.md: P26 B w §1, pomyśle 2 i zakresie pierwszej wersji (wybór typu naczepy zawsze jako zapas), przy każdym „nie trzyma” wpisano, kto ustala próg (Programista po 0P dla Z1–Z2c, Artur przy przeglądzie MVP dla Z3), dodano kryterium wyboru typu naczepy (≤1 kliknięcie, test akceptacji MVP)
P28 14:41 odpowiedź: tak, puszczamy dalej. O rundy sprawdzania nie pytamy ani Pawła, ani Artura — decyduje zespół; 3 rundy to górna granica.
P27 14:41 wycofane (Paweł w P28: o rundy sprawdzania nie pytamy Artura) → puszczamy dalej.
14:41 Szef: 1b zamyka się poprawką Projektanta po recenzji 3 (bez rundy 4); potem od razu /write-prd → docs/spec.md. Prezenter skraca opis HackTribe do ≤ 1000 znaków po wpisaniu liczb.
P27 14:42 odpowiedź: tak — lista typów naczepy zawsze pod ręką (Artur w pokoju); kolejna runda sprawdzania nie jest sprawą Artura, decyduje zespół → idziemy dalej wg rekomendacji, drobne braki jako ryzyka w opisie produktu
14:41 Prezenter: opis hacktribe skrócony (1041 zn. z [__], ok. 1033 po wpisaniu liczb do 3 cyfr; limit 1000); zachowane P19 A, P20 A, P25 B, P26 B.
14:41 Prezenter: opis hacktribe skrócony (991 zn. z [__], ok. 983 po wpisaniu liczb do 3 cyfr; limit 1000; usunięte: „(obraz ok. 50 MB)”, „Wczytuje BMP.”, „na naszym zbiorze”); zachowane P19 A, P20 A, P25 B, P26 B.
14:42 Projektant: krok /write-prd → docs/spec.md (P25 B, P26 B w specu); moment (c) pominięty na zlecenie Szefa po P28 — układ ekranu to propozycja, zapisana w specu jako ryzyko; P27 wycofane (Paweł w P28)
14:41 Szef: 1b zamknięty (74f8b12, poprawka po recenzji 3; bez rundy 4 wg P28) → /write-prd → docs/spec.md (Projektant, w toku).
14:43 Szef: spec.md (12a4072) → recenzja przejścia 2-1 (Analityk). Trzy warianty ekranu zrobi Programista po 0P, zanim powstanie makieta; Artur wybiera z linków (ryzyko z spec §9). HackTribe 991 zn. (0802220) przyjęte.
14:44 Analityk: recenzja przejścia 2 (write-prd) runda 1 (spec.md 12a4072) — 4 braki (3 technika: A1/A2 bez reguły zaliczenia, A8 „kilka”/FP bez kryterium, 3 vs 4 obrazy; 1 produkt: znaczenie Zatwierdź/Odrzuć); docs/recenzje/2-1.md
14:44 Prezenter: docs/demo.md — szkic scenariusza pokazu, 120 s, 9 kroków wg spec §7.3; liczby [__] do wpisania po pomiarze; wersja awaryjna: zrzuty ekranu.
14:44 Szef: recenzja 2-1 (b515119): 4 braki → Projektant poprawia 1–3 w spec; brak 4 (produkt: znaczenie Zatwierdź/Odrzuć) → Artur jako P (Projektant).
P29 14:45 Artur: Co znaczą przyciski przy zaznaczeniu na ekranie: (A) „Zatwierdź” = sprawdzone, podejrzane — do kontroli, „Odrzuć” = pomyłka systemu, czy (B) „Zatwierdź” = sprawdzone, nic nie ma, „Odrzuć” = do kontroli? Rekomendacja: A — zgodnie z pomysłem 7 („sprawdzone / pomyłka”); raport pokaże, które miejsca trafiają do kontroli — czeka
14:45 Projektant: recenzja kroku 2 runda 1 (Analityk, b515119): braki 1–3 poprawione w spec.md (reguły zaliczenia i „nie trzyma” A1–A4, A8 z zasadą liczby, A10 fałszywy alarm, 4 obrazy w 7.2, obraz (c) w ścieżce); brak 4 → P29 (w specu rekomendacja A tymczasowo)
14:45 Szef: spec 6d389d1 (braki 1–3 poprawione, A10 nowe) → recenzja 2-2 (Analityk); P29 czeka na Artura.
14:45 Analityk: recenzja przejścia 2 (write-prd) runda 2 (spec.md 6d389d1) — 3 braki technika (A1 sprzeczne zdanie o progu, „kilka” z dwoma właścicielami A8/A10, A8 procenty vs „n z N”); P29 nieoceniane; docs/recenzje/2-2.md
14:46 Szef: recenzja 2-2 (a79ed53): 3 braki technika → Projektant poprawia (runda 3 ostatnia). demo.md (0a0d09d, 120 s) → recenzja demo-1 (Analityk).
14:46 Projektant: recenzja kroku 2 runda 2 (Analityk, a79ed53) braki 1–3 poprawione w spec.md i 03-write-prd.md: A1 = 0 przeoczeń chyba że Programista zapisze inny próg po 0P; „kilka, nie kilkadziesiąt” — robocza z 0P do MVP, ostateczna Artur przy przeglądzie MVP (A8 = A10); A8 (1) jako „n z N”
P29 14:47 odpowiedź: A, a przy „Odrzuć” operator wybiera powód z krótkiej listy (np. element konstrukcji, ładunek zgodny, cień) (Artur w pokoju)
14:46 Analityk: recenzja docs/demo.md (0a0d09d) runda 1 — 5 braków technika (brak obrazu (c), 2 z 4, 120 s bez zapasu, P29 bez notatki, puste typy w (d), plansza [__] bez wariantu); docs/recenzje/demo-1.md
14:47 Prezenter: docs/slajdy.md — konspekt 10 slajdów (problem → rozwiązanie → ekrany → wyniki [__] → ograniczenia → dalsze kroki → narzędzia → zespół); PDF później.
14:47 Szef: spec 270f410 → recenzja 2-3 (ostatnia, Analityk). demo-1 (a3a06a3): 5 braków technika → Prezenter poprawia po slajdach (cel ~105 s).
14:47 Analityk: recenzja przejścia 2 (write-prd) runda 3 (spec.md 270f410/a839c85) — 3 braki technika (P20 „jednym kliknięciem” vs A5 po P29; „2 z 4” w §7.2 nadal; powód odrzucenia bez kryterium w A7); docs/recenzje/2-3.md
14:48 Prezenter: docs/demo.md po recenzji demo-1 (5 braków): obraz (c), paski 2 z 2 / 4, 105 s ze 15 s zapasu (≤2 słowa/s), notatka P29 (teraz A), typy plandeka→chłodnia (przykładowe, do zgrania z makietą), wiersz 10 = slajd + wariant bez liczb, wersja awaryjna obejmuje slajd.
14:48 Szef: recenzja 2-3 (615c5f2): 3 braki technika — po 3. rundzie bez rundy 4 (P28): Projektant poprawia i zamyka krok 2; potem recenzja odbiorcy (Programista, po 0P). Lista powodów odrzucenia zamknięta (4 pozycje), zmienia tylko Artur. Typy przykładowe: plandeka (zły) / chłodnia (z listy). demo.md 54c2628 (105 s) przyjęte; slajdy → recenzja slajdy-1 (Analityk).
14:48 Projektant: krok 2 zamknięty po 3 rundach — spec.md po recenzji 2-3 (615c5f2): P29 A zmienia P20 A (Zatwierdź 1 klik, Odrzuć 2 kliknięcia), paski 2 z 2 / 0 z 4 / 0 miejsc i typy plandeka→chłodnia wg demo.md, A7 z zamkniętą listą powodów odrzucenia (właściciel Projektant, zmienia tylko Artur); odsyłacz do P29 przy Z5 w 02-discover
14:49 Analityk: recenzja docs/slajdy.md (0d20a50) runda 1 — 4 braki technika (2 z 4, „jednym kliknięciem” po P29, slajd 9 niepełny, slajd 6 bez wariantu bez liczb); licencje sprawdzone: OpenMausBot Apache-2.0, pm-skills MIT; docs/recenzje/slajdy-1.md
14:50 Szef: krok 2 przyjęty (987a579); recenzja slajdy-1 (570e39f, 4 braki technika) → Prezenter poprawia slajdy.md i README (Odrzuć = powód z listy, slajd 9 narzędzia, slajd 6 wariant bez liczb); recenzja odbiorcy spec po 0P
14:50 Prezenter: slajdy.md i README.md po recenzji slajdy-1 (4 braki): „2 z 2”/„0 z 4”/„0 miejsc”, Odrzuć z powodem z listy i powód w raporcie, create-prd + przeplywy-pm + orkiestrator na slajdzie 9, wariant slajdu 6 bez liczb, „za słabe”.
14:51 Szef: slajdy.md + README poprawione (cf8556b) → recenzja slajdy-2 (Analityk)
14:51 Analityk: recenzja slajdy.md i README.md (cf8556b) runda 2 — brak braków zmieniających zakres lub kryteria; 2 drobne uwagi technika (kropka na slajdzie 9/orkiestrator w README, sprzeczna linia obrazka slajdu 6); docs/recenzje/slajdy-2.md
14:51 Szef: slajdy zamknięte (slajdy-2 e76538f: brak braków); 2 uwagi kosmetyczne → Prezenter
14:52 Prezenter: slajdy-2: slajd 9 bez nadmiarowej kropki, slajd 6 obrazek tylko po pomiarze (do tego czasu wariant bez liczb), README Użyte narzędzia + orkiestrator.
14:59 Szef: 0P wznowione po restarcie (Programista); szkice 3 wariantów → Projektant (docs/pm/04-warianty.md), niezależne od 0P
14:59 Projektant: docs/pm/04-warianty.md — 3 szkice wariantów ekranu dla Programisty (zlecenie Szefa)
15:00 Programista: 0P pomiar bazowy (male pełny, 20 czystych/45 dodatków, karta OMEN zgl-4607, kod metod = 15e71fe, k=6): H2 FP 20/20 FN 0/45; H2o FP 18/20 FN 0/45; H2no FP 14/20 FN 0/45; H2ko FP 7/20 FN 0/45 — hipotezy: otwarcie maski, nauka szumu, top-3 wzorce zbijają FP — potwierdzone (najsilniej top-3); żadna nie podnosi FN. Wyniki: wyniki/0P/. Bazą do dalszej pracy H2ko.
15:01 Programista: recenzja odbiorcy docs/spec.md (987a579) — 5 braków: 1 wejście i biblioteka (technika), 2 format raportu (technika), 3 granice stref ryzyka (technika), 4 dane chronione a link publiczny (technika), 5 skala „stopień różnicy” (produkt). docs/recenzje/spec-odbiorca.md
15:01 Szef: 0P przyjęte (c156e12), baza H2ko; liczby → Prezenter (hacktribe, README, demo, slajdy); Programista: recenzja odbiorcy spec, FN podwójnej podłogi, potem 3 makiety wariantów z 04-warianty (40ed041)
15:02 Prezenter: liczby H2ko z wyniki/0P/README.md (c156e12) wpisane w hacktribe, README, demo (slajd 10), slajdy (slajd 6): 7 z 20, 0 z 45, 1,1 s, dobór 37 z 40; podwójna podłoga zostaje [__] do odpowiedzi Programisty; opis HackTribe skrócony do limitu.
15:02 Szef: recenzja odbiorcy spec (Programista): braki 1–4 technika rozstrzygnięte wg rekomendacji Programisty (wgranie .bmp + 4 gotowe, typy plandeka/chłodnia/kontener na podwoziu/cysterna/skrzyniowa; raport PNG+JSON; strefy z geometrii wzorca, środek ramki; link publiczny tylko dane sztuczne, obraz KAS lokalnie z Dockerfile) → Projektant wpisuje; brak 5 produkt → P30 Artur (Projektant)
P30 15:03 Artur: Jak operator ma widzieć, jak bardzo miejsce różni się od wzorca? A: trzy słowa (niski / średni / wysoki), bez liczb; B: liczba lub pasek. Rekomendacja: A — nie obiecujemy dokładności, której nie zmierzyliśmy (P15–P17). — czeka
15:03 Projektant: braki 1–4 z recenzji odbiorcy spec.md (Programista) wpisane do spec §7.6 i 03-write-prd.md; brak 5 zadany jako P30
15:03 Prezenter: opis HackTribe zgodny z P29 A (zatwierdza albo odrzuca z powodem z listy), 970 znaków; README już zgodne z P29.
15:03 Szef: Paweł potwierdził: dane chronione tylko lokalnie (spec §7.6 pkt 4) zostaje
P30 15:04 odpowiedź: A — trzy słowa (niski / średni / wysoki), bez liczb; lista ułożona od wysokiego (Artur w pokoju)
15:05 Szef: warianty https://pawelpisarek.github.io/hacknation-proba16/makieta/warianty/1/ https://pawelpisarek.github.io/hacknation-proba16/makieta/warianty/2/ https://pawelpisarek.github.io/hacknation-proba16/makieta/warianty/3/
15:05 Szef: P30 A przyjęte (Artur w pokoju); podwójna podłoga H2ko FN 0/10 (fc96c93) → Prezenter uzupełnia [__]
15:05 Programista: makiety 3 wariantów (04-warianty 40ed041, dane udawane spec §7.2) na gh-pages: https://pawelpisarek.github.io/hacknation-proba16/makieta/warianty/1/ , /2/ , /3/ — HTTP 200 ×3. Wspólne: 4 obrazy (a)–(d), wybór typu (d: plandeka→chłodnia), Zatwierdź 1 klik / Odrzuć + powód, pasek, raport JSON do pobrania. 0P: H2ko FN podwójna podłoga 0 z 10 (wyniki/0P/README.md).
P31 15:05 Artur: Który wariant ekranu bierzemy? 1 (jeden duży obraz, lista z boku) https://pawelpisarek.github.io/hacknation-proba16/makieta/warianty/1/ ; 2 (kolejka, miejsce po miejscu z powiększeniem) https://pawelpisarek.github.io/hacknation-proba16/makieta/warianty/2/ ; 3 (wzorzec obok badanego obrazu) https://pawelpisarek.github.io/hacknation-proba16/makieta/warianty/3/ . Rekomendacja: 2 — operator nie pominie żadnego miejsca, a na MVP to najprostsza ścieżka do pokazu w 2 min — czeka
15:06 Prezenter: wpisane 0 z 10 (podwójna podłoga, H2ko, wyniki/0P fc96c93) w hacktribe, README, demo, slajdy; P30 A (stopień różnicy: niski/średni/wysoki, lista od wysokiego) w slajdzie 4 i demo (wiersz 4); brak [__] w 4 plikach.
P31 15:06 odpowiedź: wariant 3 (wzorzec obok badanego obrazu) + z wariantu 1 lista miejsc z boku; operator musi widzieć, z czym porównujemy (Artur w pokoju)
15:08 Szef: P31 przyjęte (wariant 3 + lista z boku) → Programista makieta R1, Projektant spec
15:08 Projektant: P31 wpisane do spec §7.2 (wariant 3 + lista z wariantu 1, lista od wysokiego); zdublowanej linii pytania P31 nie ma (jedna, wiersz 177)
15:09 Programista: makieta R1 (P31: wariant 3 wzorzec obok badanego + lista miejsc z boku z wariantu 1; lista od wysokiego, stopień słownie wg P30 A; dane udawane spec §7.2) — makieta/index.html, https://pawelpisarek.github.io/hacknation-proba16/makieta/ , zrzut docs/zrzuty/makieta-R1.png
15:10 Analityk: recenzja spójności P31 (spec fb50933, demo, slajdy): 4 braki produkt (suwak vs dwa okna: spec §7.1 pkt 3, §7.2 Środek, §7.3 krok 2; demo wiersz 3; slajd 4) → docs/recenzje/p31-spojnosc.md
15:10 Szef: recenzja spójności P31 (784f3a0), runda 1: braki 1–2 → Projektant, 3–4 → Prezenter (poprawki wg P31, nie pytania)
15:10 Projektant: spec §7.1/7.2/7.3 i 03 poprawione wg P31 (dwa okna zamiast suwaka; recenzja p31-spojnosc braki 1–2)
- 15:10 Prezenter: P31 — suwak zastąpiony dwoma oknami i listą z boku (demo wiersz 3, slajd 4); wg zlecenia Szefa (p31-spojnosc brak 3–4).
15:11 Szef: makieta R1 https://pawelpisarek.github.io/hacknation-proba16/makieta/ (zrzut docs/zrzuty/makieta-R1.png) → krytyk Analityk
15:11 Szef: spójność P31 runda 1 zamknięta — suwak usunięty (spec 54929c5, demo/slajdy Prezenter 15:10; grep: tylko zdanie „zbędny”)
15:11 Analityk: krytyk makiety R1: ocena 7/10, 5 braków (3 produkt, 2 technika) → docs/recenzje/makieta-R1.md
15:12 Szef: krytyk makiety R1: 7/10, 5 braków (479f03c) → wszystkie do Artura przez Projektanta (jedna wiadomość) + „co wyrzucić?”
P32 15:12 Artur: Odrzucenie bez powodu: A — nie da się odrzucić, dopóki operator nie wybierze powodu z listy; B — można odrzucić bez powodu, w raporcie będzie „bez powodu”. (makieta: https://pawelpisarek.github.io/hacknation-proba16/makieta/) — czeka
P33 15:12 Artur: Okno wzorca: A — pokazuje to samo miejsce (przerywana ramka w tym samym punkcie co w obrazie badanym); B — zostaje bez znacznika. (makieta: https://pawelpisarek.github.io/hacknation-proba16/makieta/) — czeka
P34 15:12 Artur: Przykład „porównano z”: A — przy naczepie (b) typ jest dobry („chłodnia”), a zły dobór („plandeka”) pokazujemy tylko przy (d); B — zostawiamy „plandeka” także przy (b). (makieta: https://pawelpisarek.github.io/hacknation-proba16/makieta/) — czeka
P35 15:12 Artur: Raport do pobrania: A — zestawienie (miejsce, przedmiot kontroli, decyzje) plus obraz z zaznaczeniami; B — samo zestawienie. Pola przykładowe (przejście, numery rejestracyjne) oznaczamy jako dane sztuczne. (makieta: https://pawelpisarek.github.io/hacknation-proba16/makieta/) — czeka
P36 15:12 Artur: Małe miejsca na obrazie (np. nr 2): A — powiększamy numer i dodajemy krótki opis jak przy miejscu 1; B — zostawiamy jak jest. (makieta: https://pawelpisarek.github.io/hacknation-proba16/makieta/) — czeka
P37 15:12 Artur: Co z ekranu wyrzucić? Krytyk proponuje usunąć napis „WZORZEC: plandeka” wewnątrz okna wzorca (powtarza nagłówek i pole wyboru typu): A — usuwamy; B — zostawiamy; albo wskaż coś innego. (makieta: https://pawelpisarek.github.io/hacknation-proba16/makieta/) — czeka
P32 15:13 odpowiedź: A — odrzucenie tylko z powodem z listy (z P29; poprawka, nie pytanie) (Artur w pokoju)
P33 15:13 odpowiedź: A — okno wzorca pokazuje to samo miejsce, przerywana ramka (poprawka makiety) (Artur w pokoju)
P34 15:13 odpowiedź: A — „porównano z”: przy (b) typ dobry, zły dobór tylko przy (d) (poprawka makiety) (Artur w pokoju)
P35 15:13 odpowiedź: A — raport: zestawienie + obraz z zaznaczeniami; pola przykładowe jako dane sztuczne (Artur w pokoju)
P36 15:13 odpowiedź: A — małe miejsca: większy numer i krótki opis jak przy miejscu 1 (poprawka makiety) (Artur w pokoju)
P37 15:13 odpowiedź: A — usuwamy napis „WZORZEC: plandeka” z okna wzorca; dodatkowo usuwamy z paska na dole zdanie ostrożności, zostaje w opisie (Artur w pokoju)
15:13 Projektant: P32–P34, P36 to poprawki/wynik z P29 — Artur: takie rzeczy bez pytania; lista poprawek makiety dla Programisty: P32–P37
15:14 Szef: P32–P37 A przyjęte (Artur w pokoju) → Programista makieta R2; Projektant spec; Prezenter demo/slajdy. Artur: poprawek błędów i tego, co wynika z jego odpowiedzi, nie zadajemy jako P — rozstrzyga zespół z recenzentem
15:14 Projektant: P32–P37 (odpowiedzi Artura 15:13) wpisane do spec §7.2 i 03-write-prd.md
15:19 Szef: recenzja docs/hacktribe.md R1 → Analityk (poza łańcuchem)
15:20 Analityk: recenzja hacktribe R1 (8333c95): 3 braki (2 produkt, 1 technika), liczby H2ko zgodne → docs/recenzje/hacktribe-R1.md
15:20 Szef: recenzja hacktribe R1 (b5263f2): 3 braki = poprawki (P37 A, fakt, układ pliku) → Prezenter, bez pytań do Artura
- 15:20 Prezenter: hacktribe wg recenzji R1 — dodane zdanie ostrożności (P37 A), „m.in. podwójną podłogę” zamiast „najczęściej” (P25), sekcja „Do formularza” oddzielona od notatek; opis 998 zn.
15:21 Szef: hacktribe poprawiony (8a7b2f2, 998 zn.) → recenzja R2 Analityk
15:21 Analityk: recenzja hacktribe R2 (8a7b2f2): braki 1–3 z R1 zamknięte; 1 nowy brak produkt (zgubione 'dane chronione tylko lokalnie', P. 15:03) → docs/recenzje/hacktribe-R2.md
15:22 Szef: hacktribe R2 (50885ac): 1 brak — punkt 4 Pawła (tylko lokalnie) → Prezenter
- 15:22 Prezenter: hacktribe wg recenzji R2 — przywrócone ustalenie Pawła (dane chronione tylko lokalnie): „Obrazy liczone tylko lokalnie, bez chmury; obrazów KAS nie mamy.”; opis 999 zn.
15:22 Szef: hacktribe poprawiony (43490f8, 999 zn.) → recenzja R3 Analityk
15:22 Analityk: recenzja hacktribe R3 (43490f8): brak braków zmieniających zakres lub kryteria → docs/recenzje/hacktribe-R3.md
15:22 Szef: hacktribe R3 (c307203) — brak braków; docs/hacktribe.md 43490f8 gotowy do wklejenia o 20:00 (link do makiety dopisać po R2)
15:29 Szef: recenzja docs/demo.md R1 → Analityk
15:30 Analityk: recenzja demo R1 (demo.md): 3 braki produkt (raport po (d) bez decyzji; brak P33 w opisie wiersza 3; wiersz 9 może brzmieć jak obietnica) → docs/recenzje/demo-R1.md
15:30 Szef: demo R1 (1804ae4) 3 braki = poprawki; rozstrzygnięcie: raport zapisujemy po (b), przed (c) (na (d) brak decyzji) → Projektant spec §7.3, Prezenter demo
15:30 Projektant: spec §7.3 i 03-write-prd: „Zapisz raport” przeniesiony po (b), przed (c) (poprawka błędu z recenzji demo-R1, brak 1; bez pytania do Artura)
- 15:31 Prezenter: demo wg recenzji R1 — raport po obrazie (b) przed (c) (wiersz 6), P33 przerywana ramka w wierszu 3, „to wybrany przykład” w wierszu 9, pola raportu = dane sztuczne (P35); suma 105 s.
