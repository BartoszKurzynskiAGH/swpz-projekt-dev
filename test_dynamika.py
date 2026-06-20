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

if __name__ == '_main_':
    unittest.main()