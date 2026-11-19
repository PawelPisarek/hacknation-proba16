# 01 — MVP z makiety (Programista)

Cel: każda decyzja P z makiety działa w prawdziwej aplikacji (wynik z karty OMENa, nie dane udawane), pod ksefbot.pl.
Wzór ekranu: https://pawelpisarek.github.io/hacknation-proba16/makieta/ (R3 ac5eedf), spec docs/spec.md §7.

| P | co ma działać w MVP | dowód |
|---|---|---|
| P29 | Zatwierdź / Odrzuć przy każdym miejscu | zrzut |
| P30 | stopień różnicy słownie niski/średni/wysoki, bez liczb; lista od wysokiego | test JSON + zrzut |
| P31 | wzorzec obok badanego obrazu + lista miejsc z boku | zrzut |
| P32 | Odrzuć tylko z powodem z listy (element konstrukcji, ładunek zgodny, cień) | zrzut |
| P33 | w oknie wzorca to samo miejsce przerywaną ramką | zrzut |
| P34 | „porównano z” — typ dobrany automatycznie, operator może zmienić | zrzut |
| P35 | raport: zestawienie + PNG z zaznaczeniami; pola przykładowe oznaczone „dane sztuczne” | pobrany plik |
| P36 | numer + krótki opis przy każdym miejscu, także małym | zrzut |
| P37 | bez napisu w oknie wzorca, bez zdania ostrożności na pasku | zrzut |
| P38 | B: przy nieprzejrzanych jedno ostrzeżenie „Nieprzejrzane: N miejsc. Zapisać mimo to?”, po potwierdzeniu zapis z „nieprzejrzane” w raporcie | zrzut |

Gotowe, gdy każdy wiersz ma dowód (zrzut w docs/zrzuty/mvp-*.png albo test), aplikacja odpowiada 200 pod linkiem,
a linia w docs/decyzje.md ma godzinę. Kolejność: najpierw rdzeń (bmp → PNG + JSON, test 4 obrazów), potem ekran.
