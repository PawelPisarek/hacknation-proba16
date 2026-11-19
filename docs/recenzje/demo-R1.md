# Recenzja docs/demo.md (scenariusz do 2 min), runda 1 — vs `docs/spec.md` §7.2–7.3 (P30–P37), `docs/decyzje.md`, `wyniki/0P/README.md`

Sprawdzone bez braku: suma czasu 105 s (wiersze 0–10, 10–19, 19–26, 26–38, 38–46, 46–58, 58–72, 72–82, 82–88, 88–105 ciągłe; ≤ 120 s, zapas 15 s); liczba słów lektora w każdym wierszu ≤ limit (najwięcej: wiersz 10, 33 z 34); kolejność kroków = spec §7.3 (b, dwa okna, Zatwierdź, Odrzuć z powodem, c, d, raport, a); pasek stanu zgodny ze specem §7.2 Dół; (b) „typ chłodnia”, zły dobór tylko w (d) (P34 A); liczby wiersza 10 = 0P (FP 7/20, FN 0/45, podwójna podłoga 0/10, 1,1 s) z zastrzeżeniem o danych sztucznych; wersja awaryjna jest.

Braki (3):

1. **produkt** — wiersz 8 (i spec §7.3 krok 7): „Zapisz raport” po obrazie (d), na którym operator nie podjął żadnej decyzji; okno raportu ma pokazywać decyzje, powody oraz „miejsce/przedmiot kontroli” (spec §7.2, P35 A) — w (d) byłoby puste. Raport należy zapisać po (b) (są Zatwierdź i Odrzuć z powodem) i przenieść ten krok przed (c). Zmiana kolejności kroków w specu §7.3 i demo (Projektant + Prezenter); czas bez zmian.
2. **produkt** — wiersz 3: P33 A (okno wzorca pokazuje to samo miejsce, przerywana ramka) nie ma w opisie ekranu ani w lektorze; to ono tłumaczy sens dwóch okien. Dopisać do „co widać”: „w oknie wzorca przerywana ramka w tym samym miejscu”; lektor: bez zmiany długości.
3. **produkt** — wiersz 9: lektor „na tej czystej naczepie w pokazie nie ma zaznaczeń” tuż przed slajdem z FP 7/20 może zabrzmieć jak obietnica skuteczności na czystych naczepach (P15–P17). Dopisać „to wybrany przykład” (limit 12 słów, zapas jest).

Poza listą (technika, drobne): wiersz 8 nie wspomina, że pola przykładowe w raporcie są oznaczone jako dane sztuczne (P35 A).

Niesprawdzone: żywa makieta (oglądałem tylko zrzut R1 i spec); czas nagrania na głos nie był mierzony.
