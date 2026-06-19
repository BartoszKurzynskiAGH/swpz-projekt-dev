# Testowanie programu

W celu weryfikacji poprawności działania skryptu automatyzującego, przeprowadziliśmy testy na przygotowanej bazie danych cenowych.

## Logi z uruchomienia skryptu
Poniższy wydruk z konsoli potwierdza, że biblioteka `pandas` prawidłowo zinterpretowała brak danych dla pierwszego roku (brak okresu poprzedzającego) oraz bezbłędnie wyliczyła indeksy łańcuchowe dla kolejnych lat.

--- REZULTATY ANALIZY DLA ZESPOŁU ---
 Rok  Cena_Chleba_PLN  Indeks_Lancuchowy_Procent
2022              4.2                        NaN
2023              4.5                 107.142857
2024              4.9                 108.888889
2025              4.9                 100.000000
2026              5.2                 106.122449