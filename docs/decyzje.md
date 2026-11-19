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
