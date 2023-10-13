import unittest
from graph_bar_eduarda import graph_bar
import pandas as pd

class TestGraphBar(unittest.TestCase):

    def test_graph_bar(self):
        data = pd.DataFrame({'REGIAO': ['Norte', 'Sul', 'Leste', 'Oeste'],
                             'UTI_PEDIATRICO_EXIST': [20, 15, 18, 12]})
        
        # Testando se a função não gera exceções
        graph_bar(data, 'REGIAO', 'UTI_PEDIATRICO_EXIST',
                  'TOTAL DE LEITOS PEDIÁTRICOS DE UTI POR REGIÃO',
                  'Região', 'Total de leitos pediátricos',
                  'uti_pediatrico_por_regiao.jpg')


if __name__ == '__main__':
    unittest.main()
