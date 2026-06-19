# Architektura systemu i struktura projektu

Poniżej znajduje się opis struktury modułów skryptu analitycznego oraz matematyczne podstawy wyliczania wskaźników.

## Model matematyczny
Główny algorytm zaimplementowany w skrypcie opiera się na wyliczaniu indeksów łańcuchowych przy użyciu biblioteki pandas:

## I = X_t / X_t-1 * 100%

## Legenda:
* I - indeks łańcuchowy
* X_t – cena w roku bieżącym
* X_t-1 – cena w roku poprzednim

## Skruktura repozytorium:
* skrypt.py – moduł wykonawczy
* mkdocs.yml – konfigurator struktury dokumentacji i motywu graficznego
* docs – pliki źródłowe dokumentacji w formacie Markdown
* .github/workflows/deploy.yml – automatyzacja wdrożenia na GitHub Pages