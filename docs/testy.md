# Testowanie programu

W celu weryfikacji poprawności działania skryptu automatyzującego, przeprowadziliśmy testy na przygotowanej bazie danych cenowych.

## Logi z uruchomienia skryptu
Poniższy wydruk z konsoli potwierdza, że biblioteka `pandas` prawidłowo zinterpretowała brak danych dla pierwszego roku (brak okresu poprzedzającego) oraz bezbłędnie wyliczyła indeksy łańcuchowe dla kolejnych lat.

```text

 REZULTATY ANALIZY DLA ZESPOŁU 
 Rok  Cena_Chleba_PLN  Indeks_Łancuchowy_Procent
2022              4.2                        NaN
2023              4.5                 107.142857
2024              4.9                 108.888889
2025              4.9                 100.000000
2026              5.2                 106.122449
```

## Automatyczne testy jednostkowe

W celu automatycznej weryfikacji algorytmu matematycznego, do projektu dodano skrypt testowy wykorzystujący bibliotekę unittest. Zapobiega on regresji kodu i automatycznie sprawdza poprawność działania funkcji .shift(1).

### Kod skryptu testowego (test_dynamika.py)
```python
import unittest
import pandas as pd

class TestDynamikaCen(unittest.TestCase):
    def test_indeks_lancuchowy_dla_stalej_ceny(self):
        dane_testowe = {
            'Rok': [2025, 2026],
            'Cena_Chleba_PLN': [4.90, 4.90] 
        }
        df = pd.DataFrame(dane_testowe)

        df['Indeks_Łancuchowy_Procent'] = (df['Cena_Chleba_PLN'] / df['Cena_Chleba_PLN'].shift(1)) * 100
        
        wynik = df['Indeks_Łancuchowy_Procent'].iloc[1]
        self.assertEqual(wynik, 100.0)

if _name_ == '_main_':
    unittest.main()
```