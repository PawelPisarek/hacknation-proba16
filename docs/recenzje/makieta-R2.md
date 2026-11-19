# Krytyk makiety R2 — zrzut docs/zrzuty/makieta-R2.png (obraz c), kod makieta/ w 622e60f

**Ocena: 8/10.** R1: powód odrzucenia wymuszony (P32), przerywana ramka we wzorcu (P33), (b) = chłodnia (P34), duży numer małych miejsc (P36), brak napisu „WZORZEC: plandeka” (P37), raport = JSON + PNG (P35), kolejność przycisków obrazów b, c, d, a — zamknięte. Zrzut (c) zgadza się ze spec §7.2 (wzorzec | badany | lista od wysokiego, trzy słowa stopnia). Poniżej tylko braki.

1. **produkt — poprawka (P15–P17, P17 A: „poprawiajcie bez pytania”)** — Obraz (a): lista pokazuje zielone, pogrubione „Brak miejsc różnych od wzorca”, a pasek „0 miejsc — brak różnic od wzorca” (`r.js`, `htmlPasek`, `rysuj`). Brzmi jak orzeczenie „naczepa czysta”, czyli obietnica skuteczności; po P37 zdanie ostrożności nie jest na pasku. Spec §7.2: dół = „(a) 0 miejsc”. Zostawić „0 miejsc” bez zielonego komunikatu i bez „brak różnic”.
2. **technika — poprawka** — Okno BADANY zmienia rysunek wraz z listą „porównano z” w (a), (b), (c): `svgNaczepa` bierze `o.poprawny || typ(k)`, więc po zmianie typu zmienia się sam „obraz z RTG” (np. (b) jako cysterna) i znika lista miejsc. Badany obraz ma być stały, zmienia się tylko wzorzec i lista (spec A6). Do ustalenia: rysunek badanego = typ rzeczywisty (`o.poprawny || o.dobrany`).
3. **technika — poprawka** — Zrzut `makieta-R2.png` jest ucięty u dołu: nie widać paska „Przejrzano n z N” ani okna raportu (pola „dane sztuczne”, P35), nie ma zrzutów (b), (d), (a). Z kodu: pasek i pola są, ale ich wyglądu nie oceniłem. Dać zrzut całej strony i oknem raportu.

**Co wyrzucić z ekranu:** nic.

Nie sprawdzono: żywej strony (tylko kod w 622e60f i zrzut (c)), pobrania PNG/JSON, wyglądu (b), (d), (a).
