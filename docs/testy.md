# Testowanie programu

W celu weryfikacji poprawności działania skryptu automatyzującego, przeprowadziliśmy testy na przygotowanej bazie danych cenowych.

## Logi z uruchomienia skryptu
Poniższy wydruk z konsoli potwierdza, że biblioteka `pandas` prawidłowo zinterpretowała brak danych dla pierwszego roku (brak okresu poprzedzającego) oraz bezbłędnie wyliczyła indeksy łańcuchowe dla kolejnych lat.

```text
--- REZULTATY ANALIZY DLA ZESPOŁU ---
  Rok  Cena_Chleba_PLN  Indeks_Lancuchowy_Procent
 2022             4.20                        NaN
 2023             4.50                 107.142857
 2024             4.90                 108.888889
 2025             4.90                 100.000000
 2026             5.20                 106.122449