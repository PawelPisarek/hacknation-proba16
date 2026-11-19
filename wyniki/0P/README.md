# Krok 0P — pomiar bazowy (zbiór `male`, pełny: 40 obrazów = 20 czystych + 20 z dodatkami, 45 dodatków: 36 przeróbek, 9 w ładunku)

Liczone na karcie OMENa (GTX 1050, orkiestrator `--klasa gpu-tlo`), zgłoszenie zgl-4607, kod metod identyczny z 15e71fe
(`rtg/metody.py` bez zmian; późniejszy commit dodał tylko przegląd progów w ocenie). Próg k=6. Dane: `python -m rtg.generator --wyjscie ~/dane/proba16/male` (ziarno 16).
Ocena: `python -m rtg.ocena --prawda ~/dane/proba16/male/prawda.json --pred wyniki/0P/<H>.json`. FP = czysty obraz z ≥1 zaznaczeniem; FN wg P9A.

| hipoteza | FP | FN (P9A) | FN (IoU≥0,1) | fałszywe ramki | czas/obraz |
|---|---|---|---|---|---|
| H2 (skale + lokalne dopasowanie, tol 3) | 20/20 | 0/45 | 2/45 | 772 | 0,56 s |
| H2o (+ tol 5, otwarcie maski 3) | 18/20 | 0/45 | 1/45 | 400 | 0,56 s |
| H2no (H2o + nauka szumu z biblioteki) | 14/20 | 0/45 | 1/45 | 230 | 0,56 s |
| H2ko (H2o + 3 najlepsze wzorce) | **7/20** | **0/45** | 1/45 | 36 | 1,11 s |

Dobór wzorca trafny 37/40 we wszystkich. Wniosek: H2ko najlepsza; FN zero, ale FP 7/20 (35%) — do zbicia (próg, łączenie wzorców).
Potwierdzenie H2 w osobnym przebiegu 14:3x (zgl-4636): FP 20/20, FN 0/45 — zgodne.
