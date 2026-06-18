# Architektura systemu i struktura projektu

Poniżej znajduje się opis struktury modułów skryptu analitycznego oraz matematyczne podstawy wyliczania wskaźników.

## Model matematyczny
Główny algorytm zaimplementowany w skrypcie opiera się na wyliczaniu indeksów łańcuchowych przy użyciu biblioteki pandas:

$$I_{\text{łańcuchowy}} = \frac{X_t}{X_{t-1}} \cdot 100\%$$

Gdzie:
* $X_t$ – cena w roku bieżącym
* $X_{t-1}$ – cena w roku poprzednim

## Struktura komponentów
Repozytorium zostało podzielone na logiczne bloki zgodnie z paradygmatem DevOps:
* skrypt.py – moduł wykonawczy (kalkulacja danych wejściowych).
* mkdocs.yml – konfigurator struktury dokumentacji i motywu graficznego.
* docs/ – pliki źródłowe dokumentacji technicznej w formacie Markdown.
