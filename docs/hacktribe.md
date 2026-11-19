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

Operator RTG na granicy ma kilka minut na naczepę (obraz ok. 50 MB) i szuka drobnej przeróbki lub skrytki. Obecne narzędzie KAS wykrywa papierosy, ale przy małych ilościach ukrytych w konstrukcji pojazdu jest za słabe. Nasze narzędzie podpowiada w trakcie oglądania obrazu: system sam dobiera wzorzec z biblioteki (gdy dobierze źle, operator wybiera typ naczepy z listy jednym kliknięciem), porównuje z nim naczepę i zaznacza miejsca różne od wzorca — dodatki w ładunku oraz przeróbki konstrukcji, najczęściej podwójną podłogę i ścianę przy kabinie. Wczytuje pliki BMP. Wynik na naszym zbiorze: czyste obrazy z zaznaczeniem: [__] z [__]; pominięte dodatki (w tym przeróbki konstrukcji): [__] z [__], w tym przeoczona podwójna podłoga: [__] z [__]; czas [__] s na obraz (cel < 1 min); duże pliki i wiele obrazów — po pomiarze. Docelowo bez chmury; w pokazie liczy usługa w sieci lokalnej. Obrazów KAS nie mamy — używamy własnego, sztucznego zbioru naczep.


Recenzje 1–2: w historii git (263c9aa — recenzja 1, 67e6458 — recenzja 2).

Poza zakresem DRAFTu: domeny i znaku towarowego „Prześwit” nie sprawdzamy (do sprawdzenia przed publikacją, jeśli w ogóle).
