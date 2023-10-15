import sys
import unittest
import pandas as pd
sys.path.append('..\Trabalho_LP_A1')

from graphs_functions.graph_bar_management_beds import graph_bar

class TestGraphManagement(unittest.TestCase):

    def test_graph_line(self):

        # Criando um dataframe para os testes
        test_data = {"TP_GESTAO":["M", "E", "D", "S", "M", "M", "E", "E"],
                     "LEITOS_SUS":[2, 3, 6, 4, 2, 4, 3, 1],
                     "LEITOS_EXISTENTES":[4, 5, 7, 5, 3, 6, 2, 1]}
        df_test = pd.DataFrame(test_data)

        # Teste normal (a função não retorna nada, apenas salva a imagem do gráfico na pasta "graphs")
        self.assertEqual(graph_bar(df_test, "TP_GESTAO", "LEITOS_SUS",
                                    title = "Teste gráfico barra", x_label = "Rótulo x", 
                                    y_label = "Rótulo y", image_graph_name = "Teste"), None)
        # Teste com coluna inexistente
        self.assertEqual(graph_bar(df_test, "DATA", "NOME"), "Coluna(s) não encontrada(s)")
        # Teste com argumento inválido
        self.assertEqual(graph_bar(1, "TP_GESTAO", "LEITOS_SUS"), "Argumento inadequado")


if __name__ == '__main__':
    unittest.main()