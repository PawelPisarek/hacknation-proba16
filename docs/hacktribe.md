# HackTribe — tekst do formularza zgłoszenia

## Do formularza

**Nazwa projektu (`product-name`):** Prześwit

**Nazwa zespołu:** Hackathon

**Link do repozytorium:** https://github.com/PawelPisarek/hacknation-proba16

**Opis (limit 1000 znaków):**

Operator RTG na granicy ma kilka minut na naczepę ciężarową. Obecne narzędzie KAS wykrywa papierosy, ale przy małych ilościach ukrytych w konstrukcji jest za słabe. Prześwit podpowiada w trakcie oglądania: system sam dobiera wzorzec z biblioteki (gdy dobierze źle, operator wybiera typ naczepy z listy jednym kliknięciem), porównuje z nim naczepę i zaznacza miejsca różne od wzorca — dodatki w ładunku i przeróbki konstrukcji, m.in. podwójną podłogę. Narzędzie pokazuje, gdzie obraz różni się od wzorca — tam warto spojrzeć jeszcze raz. Operator zatwierdza zaznaczenie albo odrzuca je z powodem z listy; raport zapisuje miejsce i przedmiot kontroli. Wynik na zbiorze sztucznym: czyste obrazy z zaznaczeniem 7 z 20; pominięte dodatki 0 z 45, w tym podwójna podłoga 0 z 10; czas 1,1 s na obraz; wzorzec dobrany trafnie 37 z 40. Duże pliki — po pomiarze; kontenery, autokary, wagony — dalszy krok. W pokazie liczy usługa w sieci lokalnej. Obrazów KAS nie mamy.

Hasło (50 zn.), jeśli formularz o nie pyta: „Zaznacza na obrazie RTG miejsca różne od wzorca.”

---

## Notatki wewnętrzne (nie wklejać do formularza)

- Status: szkic zgodny z `docs/spec.md` i `docs/nazwa.md`; liczby z `wyniki/0P/README.md` (H2ko), dane sztuczne.
- Wybór nazwy: Prześwit (P14, Artur, `docs/decyzje.md` 12:13). Odrzucone propozycje: Skrytka.AI, Wzorzec (`docs/nazwa.md`).
- Nazwa zespołu: `docs/decyzje.md`, 12:03.
- Recenzje 1–2 nazwy: w historii git (263c9aa, 67e6458).
- Poza zakresem DRAFTu: domeny i znaku towarowego „Prześwit” nie sprawdzamy (do sprawdzenia przed publikacją, jeśli w ogóle).
