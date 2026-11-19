# Recenzja docs/hacktribe.md (8333c95, opis 965 zn.), runda 1

Sprawdzone: liczby względem `wyniki/0P/README.md` (H2ko): FP 7/20, FN 0/45, podwójna podłoga 0/10, 1,1 s, dobór 37/40 — **zgodne**. Opis ≤ 1000 zn. (965). P25 B (cel w specu, liczba z pomiaru, bez „żadnej”), P26 B, P29 A, P15–P17 — w opisie zgodne. Braki:

1. **produkt** — Opis nie zawiera zdania ostrożności z P17/P37 A. Spec §7.2 „Dół”: zdanie „Narzędzie pokazuje, gdzie obraz różni się od wzorca — tam warto spojrzeć jeszcze raz.” zostaje w opisie produktu (zdjęte z paska). W `hacktribe.md` go brak. Opis ma 35 zn. zapasu, więc trzeba skrócić inne zdanie.
2. **produkt** — „zaznacza … najczęściej podwójną podłogę” to liczba/twierdzenie bez źródła. Pomiar 0P: na 45 dodatków podwójna podłoga to 10, ściana przy kabinie 15 — nie jest najczęstsza; P25 mówi tylko, że to „główna kryjówka” (wg ustaleń Artura), nie że system zaznacza ją najczęściej. Zmienić na „m.in. podwójną podłogę” albo oprzeć na P25 wprost.
3. **technika** — Plik miesza tekst do wklejenia z notatkami wewnętrznymi: nagłówek „DRAFT — opis do uzgodnienia z spec.md, gdy powstanie” (spec już jest), „Recenzje 1–2 w historii git…”, „Poza zakresem DRAFTu: domeny…”. Nie wiadomo, co trafia do formularza. Oddzielić sekcję „Do formularza” od uwag i zaktualizować status draftu.

Opis nie wspomina układu P30/P31 (dwa okna, niski/średni/wysoki) — uznane za nie zmieniające zakresu, limit 1000 zn. to ogranicza.
