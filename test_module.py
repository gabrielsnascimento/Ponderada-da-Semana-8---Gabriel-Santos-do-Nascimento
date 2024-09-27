import unittest
from mean_var_std import calculate

class TestCalculate(unittest.TestCase):

    def test_calculate_with_valid_input(self):
        # Teste com a entrada válida
        result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        expected = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        self.assertEqual(result, expected)

    def test_calculate_with_different_values(self):
        # Teste com outro conjunto de valores
        result = calculate([9, 8, 7, 6, 5, 4, 3, 2, 1])
        expected = {
            'mean': [[6.0, 5.0, 4.0], [8.0, 5.0, 2.0], 5.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[9, 8, 7], [9, 6, 3], 9],
            'min': [[3, 2, 1], [7, 4, 1], 1],
            'sum': [[18, 15, 12], [24, 15, 6], 45]
        }
        self.assertEqual(result, expected)

    def test_calculate_with_invalid_input(self):
        # Teste com entrada inválida (menos de 9 elementos)
        with self.assertRaises(ValueError) as context:
            calculate([1, 2, 3, 4, 5])
        self.assertTrue('A lista deve conter nove números' in str(context.exception))

    def test_calculate_with_negative_numbers(self):
        # Teste com números negativos
        result = calculate([-1, -2, -3, -4, -5, -6, -7, -8, -9])
        expected = {
            'mean': [[-4.0, -5.0, -6.0], [-2.0, -5.0, -8.0], -5.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[-1, -2, -3], [-1, -4, -7], -1],
            'min': [[-7, -8, -9], [-3, -6, -9], -9],
            'sum': [[-12, -15, -18], [-6, -15, -24], -45]
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
