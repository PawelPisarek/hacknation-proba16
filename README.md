# Prześwit

**Zaznacza na obrazie RTG miejsca różne od wzorca.**

> SZKIC (DRAFT) — liczby w sekcji „Wyniki” pojawią się po pomiarze.

## Co to jest

Prześwit to narzędzie dla operatora RTG na granicy, który ma kilka minut na naczepę (obraz ok. 50 MB). Obecne narzędzie KAS wykrywa papierosy, ale przy małych ilościach ukrytych w konstrukcji pojazdu jest za słabe. Prześwit podpowiada w trakcie oglądania obrazu: system sam dobiera wzorzec z biblioteki, porównuje z nim naczepę i zaznacza miejsca różne od wzorca — dodatki w ładunku oraz przeróbki konstrukcji (np. podwójną podłogę, ścianę przy kabinie). Wczytuje pliki BMP. Operator jednym kliknięciem zatwierdza albo odrzuca zaznaczenie, a raport zapisuje miejsce i przedmiot kontroli; decyzję o kontroli fizycznej nadal podejmuje operator.

Zakres: pokazujemy tylko naczepy ciężarowe (dla nich mamy zbiór i pokaz); kontenery, autokary i wagony kolejowe to dalszy krok. Obrazów KAS nie mamy, więc pracujemy na własnym, sztucznym zbiorze naczep. Docelowo narzędzie ma działać bez chmury; w pokazie obliczenia robi usługa na karcie graficznej w sieci lokalnej.

Dla kogo: operatorzy RTG Służby Celno-Skarbowej.

- Repozytorium: https://github.com/PawelPisarek/hacknation-proba16
- Makieta: [link po wdrożeniu]
- Wersja na ksefbot.pl: [link po wdrożeniu]

## Uruchomienie

Kod: `rtg/` (Python 3.12, `requirements.txt`). Metody liczą wyłącznie na karcie (CUDA); bez karty kończą się komunikatem.

```sh
pip install -r requirements.txt
# 1. dane sztuczne (deterministyczne, ziarno 16)
python -m rtg.generator --wyjscie ~/dane/proba16/male                       # 5 typów × (3 wzorce + 4 czyste + 4 z dodatkami), 2000×1000
python -m rtg.generator --wyjscie ~/dane/proba16/pelne --typy 2 --biblioteka 2 --czyste 1 --z-dodatkami 1 --wysokosc 5000   # 10000×5000 = 50 MB
# 2. porównanie z biblioteką + ocena (kilka hipotez w jednym przebiegu)
python -m rtg.uruchom --dane ~/dane/proba16/male --metody H1,H1t,H2,H2n,H2k --wyjscie wyniki/male --podglad 4
# 3. sama ocena gotowych przewidywań
python -m rtg.ocena --prawda ~/dane/proba16/male/prawda.json --pred wyniki/male/H2.json
```

Na zespołowej flocie: przez orkiestrator (`--klasa gpu-tlo` dla `rtg.uruchom`, `--maszyna dowolna` dla generatora).

Szczegóły i format przewidywań: `docs/uruchomienie.md`, nagłówek `rtg/ocena.py`.

## Wyniki

Na naszym sztucznym zbiorze (pomiar):

| miara | wynik |
|---|---|
| czyste obrazy z zaznaczeniem | [__] z [__] |
| pominięte dodatki (w tym przeróbki konstrukcji) | [__] z [__] |
| czas na obraz (cel < 1 min) | [__] s |
| duże pliki i wiele obrazów naraz | [__] (po pomiarze) |

Wyniki dotyczą zbioru sztucznego i mogą być lepsze niż na prawdziwych obrazach KAS.

## Użyte narzędzia

- **OpenMausBot** — platforma, na której pracuje zespół 5 botów przygotowany przed hackathonem (role w sekcji „Zespół”).
- **Claude** (Anthropic) — modele, na których pracują boty.
- **pm-skills** — skille produktowe użyte przez boty (m.in. product-name, value-prop-statements, release-notes).
- **Biblioteki** z `requirements.txt`: numpy, pillow, scipy, torch (z CUDA).

## Zespół

Zespół „Hackathon”:

- **Paweł** — technika, wygląd, użyteczność.
- **Artur** — kształt produktu.

Zespół botów OpenMausBot:

- **Szef** — rozdział pracy i rozmowa z Pawłem.
- **Projektant** — spec, ścieżka użytkownika, ekrany makiety.
- **Analityk** — materiały, ryzyka, recenzje.
- **Programista** — kod, makieta, wdrożenie.
- **Prezenter** — README i teksty.
