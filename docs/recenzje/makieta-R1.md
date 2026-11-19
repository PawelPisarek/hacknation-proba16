# Krytyk makiety R1 — zrzut docs/zrzuty/makieta-R1.png, źródło makieta/index.html + warianty/wspolne.js

**Ocena: 7/10.** Układ P31 (wzorzec | badany | lista z boku), lista od wysokiego i trzy słowa stopnia (P30 A), Zatwierdź/Odrzuć z powodem, pasek i zdanie P17 są na ekranie. Poniżej tylko braki.

1. **produkt** — Odrzucenie bez powodu przechodzi do raportu. Na ekranie: po „Odrzuć” pojawia się lista powodów, ale można ją zostawić; raport wypisuje wtedy „odrzucone: bez powodu” (`wspolne.js` l. 87), a pasek liczy miejsce jako przejrzane. Spec A7/P29 A: przy każdym „Odrzuć” zapisany powód z listy. Brak powodu ma blokować policzenie/zapis decyzji.
2. **produkt** — Wzorzec nie pokazuje, gdzie jest wybrane miejsce. Na ekranie: ramka i numer tylko w oknie „BADANY”, okno „WZORZEC” jest bez znacznika. Spec/P31: operator ma widzieć, z czym porównuje; spec §7.2 pisze o wspólnym przewijaniu, a przy pełnym obrazie nie ma czego przewijać. Potrzebna ta sama ramka (przerywana) w oknie wzorca albo wspólne powiększenie.
3. **technika** — (b) pokazuje „porównano z: plandeka”, a `docs/demo.md` wiersz 2 mówi (b) = „chłodnia”; spec §7.2 mówi, że błędny typ jest tylko w (d). Ujednolicić: (b) poprawny typ, błąd tylko w (d). Autor: Programista (dane), Prezenter (demo) — jedno z nich do zmiany.
4. **technika** — Raport pobiera się tylko jako JSON; spec §7.6 pkt 2 wymaga też obrazu PNG z ramkami (w kodzie brak PNG/canvas). Pola „miejsce/przedmiot kontroli” mają wpisane przykłady (nazwa przejścia, numery rejestracyjne) — oznaczyć jako dane sztuczne, bo pod publicznym linkiem mają być tylko takie (§7.6 pkt 4).
5. **produkt** — Ramka miejsca 2 („pod dachem przy drzwiach”) jest bardzo mała, a jej etykieta to samo „2”; przy czterech miejscach w (c) tej samej wielkości ramki nakładające się na towar będą nieczytelne. Powiększyć etykietę i dać opis jak przy miejscu 1 (tylko zbadać na (c) — nie sprawdzono, zrzut dotyczy (b)).

**Co wyrzucić bez straty dla operatora:** napis „WZORZEC: plandeka” wewnątrz okna wzorca (powtarza nagłówek „WZORZEC — typ: plandeka” i pole wyboru typu u góry).

Nie sprawdzono: zrzutów (a), (c), (d) ani okna raportu — tylko kod i zrzut (b).
