# Prześwit — konspekt slajdów (DRAFT, 10 slajdów, docelowo PDF)

Podstawa: `docs/spec.md`, `docs/demo.md`, `README.md`. Liczby `[__]` wpisujemy po pomiarze. Bez zdań obiecujących skuteczność (P15–P17, P25 B). Obrazki to zrzuty z makiety (sztuczne dane).

## 1. Prześwit
- Zaznacza na obrazie RTG miejsca różne od wzorca.
- Narzędzie dla operatora RTG na granicy; w trakcie oglądania obrazu.
- Zespół „Hackathon”, repo: github.com/PawelPisarek/hacknation-proba16
- **Obrazek:** logo/nazwa i hasło na tle obrazu naczepy w RTG.

## 2. Problem operatora
- Operator ma kilka minut na naczepę ciężarową (obraz ok. 50 MB).
- Obecne narzędzie KAS wykrywa papierosy, ale małe ilości ukryte w konstrukcji pojazdu są dla niego za słabe.
- Ukrycia: podwójna podłoga, ściana przy kabinie, dodatki w ładunku.
- **Obrazek:** obraz RTG naczepy z podwójną podłogą, bez zaznaczeń.

## 3. Rozwiązanie
- System sam dobiera wzorzec z biblioteki i porównuje z nim naczepę.
- Zaznacza miejsca różne od wzorca — tam warto spojrzeć jeszcze raz.
- „Zatwierdź” to jedno kliknięcie; przy „Odrzuć” operator wybiera powód z listy (element konstrukcji / ładunek zgodny z deklaracją / cień lub zakłócenie obrazu / inne). Decyzję o kontroli fizycznej podejmuje on.
- **Obrazek:** schemat: obraz → wzorzec z biblioteki → zaznaczone różnice → decyzja operatora.

## 4. Ekran: porównanie
- Obraz z ramkami i suwak wzorzec / obraz badany.
- Lista miejsc po prawej od najbardziej różnych.
- Pasek stanu zgodny z obrazem: (b) „Przejrzano 2 z 2”, (c) „Przejrzano 0 z 4”, (a) „0 miejsc”.
- **Obrazek:** zrzut głównego ekranu makiety (obraz (b), podwójna podłoga).

## 5. Ekran: wybór typu i raport
- Gdy wzorzec dobrany źle, operator wybiera typ naczepy z listy jednym kliknięciem; lista zawsze pod ręką.
- „Zapisz raport”: miejsce kontroli, przedmiot kontroli oraz powód każdego odrzucenia.
- **Obrazek:** zrzut obrazu (d) z listą typów oraz okna raportu.

## 6. Wyniki (pomiar na sztucznym zbiorze)
- Czyste obrazy z zaznaczeniem: [__] z [__].
- Pominięte dodatki (z przeróbkami konstrukcji): [__] z [__], w tym podwójna podłoga [__] z [__].
- Czas na obraz: [__] s (cel < 1 min).
- **Wariant bez liczb (gdy pomiaru brak):** tytuł „Wyniki — po pomiarze”; punkty: cel < 1 min na obraz; liczby z pomiaru podamy w opisie projektu; zbiór sztuczny, na danych KAS wyniki mogą być inne. Do PDF nie trafia tabela z samymi `[__]`.
- **Obrazek:** tabela wyników dopiero po pomiarze; do tego czasu wariant bez liczb (wyżej).

## 7. Ograniczenia
- Obrazów KAS nie mamy — własny, sztuczny zbiór naczep; na prawdziwych danych wyniki mogą być inne.
- Duże pliki i wiele obrazów naraz — po pomiarze.
- Tylko naczepy ciężarowe (P19 A).
- **Obrazek:** brak lub ikony trzech ograniczeń.

## 8. Dalsze kroki
- Kontenery, autokary, wagony kolejowe.
- Obliczenia bez chmury; w pokazie liczy usługa na karcie graficznej w sieci lokalnej.
- Próba na obrazach KAS i uzupełnienie wyników.
- **Obrazek:** oś: dziś (naczepy, zbiór sztuczny) → dalej (inne pojazdy, dane KAS).

## 9. Użyte narzędzia
- **OpenMausBot** (github.com/milind-soni/OpenMausBot, Apache-2.0) — platforma, zespół 5 botów.
- **Claude** (Anthropic) — modele, na których pracują boty.
- **pm-skills** (github.com/phuryn/pm-skills, MIT): competitor-analysis, brainstorm-ideas-new, product-name, value-prop-statements, create-prd; przeplywy-pm to skill zespołu na OpenMausBot, nie pm-skills.
- **Biblioteki:** numpy, pillow, scipy, torch (z CUDA); liczenie na zespołowej karcie graficznej przez orkiestrator (`docs/uruchomienie.md`).
- **Obrazek:** cztery logotypy/ikony w rzędzie.

## 10. Zespół
- Paweł — technika, wygląd, użyteczność; Artur — kształt produktu.
- Boty: Szef (rozdział pracy), Projektant (spec), Analityk (materiały, recenzje), Programista (kod, makieta), Prezenter (teksty).
- Linki: repo, makieta [link po wdrożeniu], ksefbot.pl [link po wdrożeniu].
- **Obrazek:** zdjęcie zespołu lub 2 awatary ludzi i 5 ikon botów.
