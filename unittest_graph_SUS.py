import unittest
import pandas as pd
from graph_bar_SUS import median_SUS

class TestMedian_SUS(unittest.TestCase):

    def test_median_a(self):
        example = pd.DataFrame(columns=["a", "b", "c"], data=[[1, 2, 3], [5, 6, 8], [14, 12, 23]])
        self.assertIsInstance(example, pd.DataFrame)
        self.assertIsInstance(example["a"], pd.Series)
        result = median_SUS(example, "a")
        self.assertEqual(result, 5.0)

    def test_median_b(self):
        example = pd.DataFrame(columns=["a", "b", "c"], data=[[1, 2, 3], [5, 6, 8], [14, 12, 23]])
        result = median_SUS(example, "b")
        self.assertEqual(result, 6.0)

    def test_invalid_key(self):
        example = pd.DataFrame(columns=["a", "b", "c"], data=[[1, 2, 3], [5, 6, 8], [14, 12, 23]])
        result = median_SUS(example, "d")
        self.assertNotIn("d", example.columns)
        self.assertEqual(result, "Chave fora da formatação necessária")

    def test_invalid_arguments(self):
        example = pd.DataFrame(columns=["a", "b", "c"], data=[[1, 2, 3], [5, 6, 8], [14, 12, 23]])
        result = median_SUS("d", example)
        self.assertEqual(result, "Argumentos inadequados")

if __name__ == '__main__':
    unittest.main()