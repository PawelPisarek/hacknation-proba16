# 01 — MVP z makiety (Programista)

Cel: każda decyzja P z makiety działa w prawdziwej aplikacji pod ksefbot.pl: ramki liczone naprawdę na karcie OMENa, na obrazach sztucznych (spec §7.6 pkt 4 — publicznie tylko dane sztuczne).
Wzór ekranu: https://pawelpisarek.github.io/hacknation-proba16/makieta/ (R3 ac5eedf), spec docs/spec.md §7.

| P | co ma działać w MVP | dowód |
|---|---|---|
| P29 | Zatwierdź / Odrzuć przy każdym miejscu | zrzut |
| P30 | stopień różnicy słownie niski/średni/wysoki, bez liczb; lista od wysokiego | test JSON + zrzut |
| P31 | wzorzec obok badanego obrazu + lista miejsc z boku | zrzut |
| P32 | Odrzuć tylko z powodem z listy wg spec A7 (4 pozycje, z „inne”) | zrzut |
| P33 | w oknie wzorca to samo miejsce przerywaną ramką | zrzut |
| P34 | „porównano z” — typ dobrany automatycznie, operator może zmienić | zrzut |
| P35 | raport: zestawienie + PNG z zaznaczeniami; pola przykładowe oznaczone „dane sztuczne” | pobrany plik |
| P36 | numer + krótki opis przy każdym miejscu, także małym | zrzut |
| P37 | bez napisu w oknie wzorca, bez zdania ostrożności na pasku | zrzut |
| P38 | B: przy nieprzejrzanych jedno ostrzeżenie „Nieprzejrzane: N miejsc. Zapisać mimo to?”, po potwierdzeniu zapis z „nieprzejrzane” w raporcie; poprawna odmiana (1 miejsce / 2 miejsca / 5 miejsc) | zrzut |

Gotowe, gdy każdy wiersz ma dowód (zrzut w docs/zrzuty/mvp-*.png albo test), aplikacja odpowiada 200 pod linkiem,
a linia w docs/decyzje.md ma godzinę. Kolejność: najpierw rdzeń (bmp → PNG + JSON, test 4 obrazów), potem ekran.

Sprawdzenia odbioru: docs/odbior-mvp.md (30 wierszy, także A1–A10 ze spec) — przechodzą wszystkie poza A8 (czeka na Artura po MVP).
Kryterium jakości na noc (P39 A, Artur 16:10): na danych sztucznych FN = 0 i FP ≤ 7/20 jako minimum; gdy da się zejść niżej z FP bez żadnego przeoczenia — schodzimy (hipotezy na karcie OMENa).
