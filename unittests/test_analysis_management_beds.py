"""Módulo de testes de analysis_management_beds

Este módulo contém os testes unitários das 4 funções definidas no módulo 
analysis_management_beds,localizado na pasta data_analysis
"""

import sys
import unittest
import pandas as pd
sys.path.append('..\Trabalho_LP_A1')

from data_analysis_functions.analysis_management_beds import mean_by_management, median_by_management, std_by_management, unique_by_management

class TestAnalysisManagementBeds(unittest.TestCase):

    def test_mean_by_management(self):

        # Criando um dataframe para os testes
        test_data = {"TP_GESTAO":["M", "E", "D", "S", "M", "M", "E", "E"],
                     "LEITOS_SUS":[2, 3, 6, 4, 2, 4, 3, 1],
                     "LEITOS_EXISTENTES":[4, 5, 7, 5, 3, 6, 2, 1]}
        df_test = pd.DataFrame(test_data, index = ["A", "B", "C", "D", "E", "F", "G", "H"]) 
        

        # Teste normal
        self.assertEqual(mean_by_management(df_test, "M", "LEITOS_SUS"), ((2+2+4)/3))
        
        # #Teste de argumento "df" não dataframe
        # self.assertEqual(mean_by_management("a", "M", "LEITOS_SUS"),
        #                 "Argumentos inadequados")
        # Teste de coluna inexistente
        # self.assertEqual(mean_by_management(df_test, "p", "b"), "Chave fora da formatação necessária")
        # Teste de argumento inválido
        # self.assertEqual(group_and_sum(df_test, ["Nome"], {"A": 1}), "Argumento inadequado")


    

if __name__ == '__main__':
    unittest.main()

print("a")