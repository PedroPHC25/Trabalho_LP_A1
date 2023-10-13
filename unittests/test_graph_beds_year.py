import sys
import unittest
import pandas as pd
sys.path.append('..\Trabalho_LP_A1')

from graphs_functions.graph_beds_year import graph_line

class TestGraphBedsYear(unittest.TestCase):

    def test_graph_line(self):

        # Criando um dataframe para os testes
        test_data = {"ID_Fatura": [111, 222, 333, 444],
                     "Data": [20210523, 20210810, 20220217, 20221204],
                     "Valor": [100, 200, 200, 500]}
        df_test = pd.DataFrame(test_data)
        df_test["Data"] = pd.to_datetime(df_test["Data"], format = "%Y%m%d")

        # Teste normal (a função não retorna nada, apenas salva a imagem do gráfico na pasta "graphs")
        self.assertEqual(graph_line(df_test, "Data", "Valor", 
                                    title = "Teste", x_label = "Rótulo x", 
                                    y_label = "Rótulo y", image_graph_name = "Teste"), None)
        # Teste com coluna inexistente
        self.assertEqual(graph_line(df_test, "Data", "Quantia"), "Coluna(s) não encontrada(s)")
        # Teste com argumento inválido
        self.assertEqual(graph_line(1, "Data", "Valor"), "Argumento inadequado")


if __name__ == '__main__':
    unittest.main()