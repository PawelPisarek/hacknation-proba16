# Recenzja 1 — README.md (Prezenter, 7f9b27d)

Wzorzec: `docs/zadanie.md`, `docs/decyzje.md` (P4–P20), `docs/uruchomienie.md`, `requirements.txt`.

Sprawdzone bez braku: komendy w sekcji „Uruchomienie” są dosłownie z `docs/uruchomienie.md` (generator ×2, `rtg.uruchom`, `rtg.ocena`); biblioteki (numpy, pillow, scipy, torch z CUDA) zgadzają się z `requirements.txt`; opis jest zgodny z P6, P8, P10–P12, P15–P17.

Braki od najważniejszego:

1. **produkt** — P19 A (tylko naczepy ciężarowe; kontenery, autokary i wagony jako dalszy krok) nie występuje w README: „narzędzie dla operatora RTG na granicy” bez zawężenia, a zadanie §1 wymienia wszystkie rodzaje pojazdów. Brak zdania o zakresie i o dalszym kroku.
2. **produkt** — P20 A (operator zatwierdza albo odrzuca zaznaczenie jednym kliknięciem; raport zapisuje miejsce i przedmiot kontroli) nie występuje; jest tylko „decyzję o kontroli fizycznej podejmuje operator”. Raport z wykrytymi anomaliami to wymóg zadania §3 i §9 (przypisanie do miejsca i przedmiotu kontroli) — README go nie opisuje. (Zapis wg P20 A; czy wchodzi do pierwszej wersji — wg decyzji Artura, nie obiecywać ponad nią.)
3. **technika** — „Użyte narzędzia” wymienia „zespół 5 botów” bez ich ról; zlecenie wymaga listy zespołu botów (Szef, Projektant, Analityk, Programista, Prezenter — `docs/zespol.md`/instrukcje) z jednym zdaniem o roli każdego. Sekcja „Zespół” też tylko „zespół botów”.
4. **technika** — adresy i licencje „github.com/milind-soni/OpenMausBot, Apache-2.0” oraz „github.com/phuryn/pm-skills, MIT” nie mają źródła w repozytorium (`docs/`, `requirements.txt`); sprawdzić w źródle albo usunąć licencje.
5. **technika — wg P16** — README nie mówi, że docelowo narzędzie ma działać bez chmury (§9), a w pokazie liczy usługa na karcie w sieci lokalnej (decyzje 11:59); sekcja „Uruchomienie” pomija też linię z `docs/uruchomienie.md` o uruchamianiu przez orkiestrator (`--klasa gpu-tlo`), więc czytelnik bez karty nie wie, że metody nie ruszą na procesorze poza komunikatem w jednym zdaniu.

<!-- skill: review -->
