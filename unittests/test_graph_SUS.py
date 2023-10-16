import sys
import unittest
import pandas as pd
sys.path.append('..\Trabalho_LP_A1')
from graphs_functions.graph_bar_SUS import graph_SUS

class TestGraphSUS(unittest.TestCase):

    def test_graph_SUS(self):
        # Um DataFrame de teste
        data = {
            "Estado": ["A", "B", "C"],
            "Coluna1": [10, 20, 30],
            "Coluna2": [5, 15, 25],
            "Coluna3": [2, 8, 18]}
        data = pd.DataFrame(data)

        # Gerando um gráfico exemplo
        result = graph_SUS(data, "Coluna1", "Coluna2", "Coluna3", "Título", "graph_test.png", 0.2, ['red', 'green', 'blue'])
        # Resultado esperado
        self.assertEqual(result, None)

        # Exceção com coluna não encontrada
        exception1 = graph_SUS(data, "coluna1", "Coluna2", "Coluna3", "Título", "graph_test.png", 0.2, ['red', 'green', 'blue'])
        self.assertEqual(exception1, "Chave fora da formatação necessária")

        # Exceção com dataframe não válido
        exception2 = graph_SUS(21, "coluna1", "Coluna2", "Coluna3", "Título", "graph_test.png", 0.2, ['red', 'green', 'blue'])
        self.assertEqual(exception2, "DataFrame inserido não válido")

if __name__ == '__main__':
    unittest.main()