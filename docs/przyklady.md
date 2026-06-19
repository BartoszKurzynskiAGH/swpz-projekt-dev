# Przykłady i kod źródłowy

Poniżej znajduje się prosty skrypt w Pythonie, który automatyzuje obliczenia.

## skrypt.py

```python

import pandas as pd

dane_ekonomiczne = {
    'Rok': [2022, 2023, 2024, 2025, 2026],
    'Cena_Chleba_PLN': [4.20, 4.50, 4.90, 4.90, 5.20]
}

df = pd.DataFrame(dane_ekonomiczne)

df['Indeks_Łancuchowy_Procent'] = (df['Cena_Chleba_PLN'] / df['Cena_Chleba_PLN'].shift(1)) * 100

print(" REZULTATY ANALIZY DLA ZESPOŁU ")
print(df.to_string(index=False))
```