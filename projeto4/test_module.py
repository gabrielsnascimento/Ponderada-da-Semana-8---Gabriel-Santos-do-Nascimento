import unittest
import pandas as pd
from sea_level_predictor import *

class TestSeaLevelPredictor(unittest.TestCase):

    def setUp(self):
        # Carregar os dados para os testes
        self.df = pd.read_csv('epa-sea-level.csv')

    def test_data_loading(self):
        """Teste se os dados são carregados corretamente."""
        self.assertFalse(self.df.empty, "O DataFrame deve ser carregado e não deve estar vazio.")

    def test_columns_exist(self):
        """Teste se as colunas necessárias existem."""
        self.assertIn('Year', self.df.columns, "A coluna 'Year' deve existir no DataFrame.")
        self.assertIn('CSIRO Adjusted Sea Level', self.df.columns, "A coluna 'CSIRO Adjusted Sea Level' deve existir no DataFrame.")

    def test_linear_regression_all_data(self):
        """Teste a regressão linear para todos os dados."""
        slope_all, intercept_all, r_value_all, p_value_all, std_err_all = linregress(self.df['Year'], self.df['CSIRO Adjusted Sea Level'])
        self.assertIsInstance(slope_all, float, "A inclinação deve ser um número de ponto flutuante.")
        self.assertIsInstance(intercept_all, float, "A interceptação deve ser um número de ponto flutuante.")

    def test_linear_regression_recent_data(self):
        """Teste a regressão linear para dados a partir de 2000."""
        df_recent = self.df[self.df['Year'] >= 2000]
        slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
        self.assertIsInstance(slope_recent, float, "A inclinação deve ser um número de ponto flutuante.")
        self.assertIsInstance(intercept_recent, float, "A interceptação deve ser um número de ponto flutuante.")

    def test_future_prediction_all_data(self):
        """Teste se a previsão do nível do mar para 2050 está sendo calculada corretamente para todos os dados."""
        slope_all, intercept_all, r_value_all, p_value_all, std_err_all = linregress(self.df['Year'], self.df['CSIRO Adjusted Sea Level'])
        years_extended = pd.Series([i for i in range(1880, 2051)])
        sea_level_predicted_all = intercept_all + slope_all * years_extended
        self.assertEqual(len(sea_level_predicted_all), 171, "Deve haver uma previsão para cada ano de 1880 a 2050.")
    
    def test_future_prediction_recent_data(self):
        """Teste se a previsão do nível do mar para 2050 está sendo calculada corretamente para dados a partir de 2000."""
        df_recent = self.df[self.df['Year'] >= 2000]
        slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
        years_recent = pd.Series([i for i in range(2000, 2051)])
        sea_level_predicted_recent = intercept_recent + slope_recent * years_recent
        self.assertEqual(len(sea_level_predicted_recent), 51, "Deve haver uma previsão para cada ano de 2000 a 2050.")

if __name__ == '__main__':
    unittest.main()
