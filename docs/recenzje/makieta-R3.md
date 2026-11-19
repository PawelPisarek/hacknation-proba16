# Krytyk makiety R3 — zrzuty docs/zrzuty/makieta-R3-{b,c,d,a}.png, kod makieta/ w ac5eedf

**Ocena: 8/10.**

**Braki z R2 (sprawdzone):**
1. (a): w liście, na pasku i w raporcie jest samo „0 miejsc” (zrzut R3-a, `r.js` `htmlPasek`) — zamknięty.
2. Badany obraz stały: `o.poprawny || o.dobrany` (`svgNaczepa`) — zamknięty w kodzie; skutek uboczny w braku 1 poniżej.
3. Zrzuty całej strony z paskiem i oknem raportu: są dla (b), (c), (d), (a); pola „dane sztuczne” widać — zamknięty.

**Braki:**
1. **technika — poprawka** — Po zamknięciu braku 2 zmiana typu w (a), (b), (c) na dowolny typ inny niż dobrany daje „0 miejsc” (`miejsca(k)`: `OBRAZY[k].miejsca[typ(k)] || []`), choć badany obraz dalej pokazuje podwójną podłogę czy ścianę z towarem. Na ekranie i w raporcie wygląda to jak „brak różnic” (P15–P17), a to tylko brak danych makiety. Dać dla pozostałych typów albo te same miejsca, albo komunikat „brak danych dla tego typu w makiecie”. W pokazie (§7.3) typ zmienia się tylko w (d), więc nie blokuje demo.
2. **produkt — prawdziwy wybór produktu (pytanie do Artura)** — Raport zapisuje się z miejscami „nieprzejrzane” (zrzut R3-d: „1. podwójna podłoga … — nieprzejrzane”, przycisk zapisu aktywny). Spec A7: raport ma decyzję przy każdym miejscu; spec nie mówi, czy zapis ma być zablokowany, ostrzegać, czy dopuszczać nieprzejrzane. Odpowiedzi nie ma w P29–P37. Wariant A: dopuścić z wyraźnym „nieprzejrzane” (stan dziś); B: ostrzeżenie przed zapisem. Rekomendacja: A (operator może zakończyć kontrolę wcześniej, a raport mówi prawdę).

**Co z ekranu wyrzucić:** nic.

Nie sprawdzono: żywej strony, pobrania PNG/JSON, widoku (d) przed zmianą typu (zły wzorzec „plandeka” z trzema dużymi ramkami — jest w kodzie, nie ma zrzutu), zrzutu cofnięcia decyzji.
