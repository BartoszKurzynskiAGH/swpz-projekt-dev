# Przykłady i kod źródłowy

Poniżej znajduje się prosty skrypt w Pythonie, który automatyzuje obliczenia.

## Skrypt dynamika_cen.py

```python
import pandas as pd

# Przygotowanie prostych danych o cenach produktu na przestrzeni 5 lat
dane_ekonomiczne = {
    'Rok': [2022, 2023, 2024, 2025, 2026],
    'Cena_Chleba_PLN': [4.20, 4.50, 4.90, 4.90, 5.20]
}

df = pd.DataFrame(dane_ekonomiczne)

# Obliczenie indeksów łańcuchowych
df['Indeks_Lancuchowy_Procent'] = (df['Cena_Chleba_PLN'] / df['Cena_Chleba_PLN'].shift(1)) * 100

print("--- REZULTATY ANALIZY DLA ZESPOŁU ---")
print(df.to_string(index=False))