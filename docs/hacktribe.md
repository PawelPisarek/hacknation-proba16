# HackTribe — tekst do formularza zgłoszenia

> **DRAFT** — pierwszy szkic. Opis do uzgodnienia z `docs/spec.md`, gdy powstanie.

## Nazwa projektu (`product-name`): **Prześwit**

Hasło (50 zn.): „Zaznacza na obrazie RTG miejsca różne od wzorca.”

Historia wyboru — 3 propozycje:

1. **Skrytka.AI** — nazwa od skrytek (podwójna podłoga, ściana przy kabinie), których szuka operator wg P7; łatwe do zapamiętania.
2. **Wzorzec** — krótkie; od „obrazu wzorcowego”, względem którego liczone są odstępstwa.
3. **Prześwit** — polskie, jedno słowo; kojarzy się z prześwietleniem obrazu RTG i podpowiedzią w trakcie oglądania (P6).

Wybrane: Prześwit (P14, Artur, `docs/decyzje.md` 12:13). Lista zgodna z `docs/nazwa.md`.

## Nazwa zespołu

Hackathon (ustalone: `docs/decyzje.md`, 12:03)

## Link do repozytorium

https://github.com/PawelPisarek/hacknation-proba16

## Opis wstępny (DRAFT, limit 1000 znaków)

Operator RTG na granicy ma kilka minut na naczepę ciężarową. Obecne narzędzie KAS wykrywa papierosy, ale przy małych ilościach ukrytych w konstrukcji jest za słabe. Prześwit podpowiada w trakcie oglądania: system sam dobiera wzorzec z biblioteki (gdy dobierze źle, operator wybiera typ naczepy z listy jednym kliknięciem), porównuje z nim naczepę i zaznacza miejsca różne od wzorca — dodatki w ładunku i przeróbki konstrukcji, najczęściej podwójną podłogę. Operator jednym kliknięciem zatwierdza albo odrzuca zaznaczenie; raport zapisuje miejsce i przedmiot kontroli. Wynik na zbiorze sztucznym: czyste obrazy z zaznaczeniem 7 z 20; pominięte dodatki 0 z 45, w tym podwójna podłoga [__] z [__]; czas 1,1 s na obraz (cel < 1 min); wzorzec dobrany trafnie 37 z 40. Duże pliki i wiele obrazów — po pomiarze; kontenery, autokary, wagony — dalszy krok. Docelowo bez chmury; w pokazie liczy usługa w sieci lokalnej. Obrazów KAS nie mamy.


Recenzje 1–2: w historii git (263c9aa — recenzja 1, 67e6458 — recenzja 2).

Poza zakresem DRAFTu: domeny i znaku towarowego „Prześwit” nie sprawdzamy (do sprawdzenia przed publikacją, jeśli w ogóle).
