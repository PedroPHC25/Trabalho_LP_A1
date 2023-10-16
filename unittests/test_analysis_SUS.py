'''Módulo de teste para análise Leitos SUS

Este módulo contém os teste unitários para as funções
que extraem as métricas estatísticas sobre a presença
de Leitos SUS em hospitais de diversas natureza.
'''
import unittest
import pandas as pd
import sys

sys.path.append('..\Trabalho_LP_A1')
from data_analysis_functions.analysis_functions_SUS import median_SUS, mean_SUS, max_min_SUS, std_SUS

class TestAnalysis_SUS(unittest.TestCase):

    def test_median(self):

        #Criando um df exemplo para os teste 
        example = pd.DataFrame(columns=["a", "b", "c"], 
                               data=[[1, 2, 3], [5, 6, 8], [14, 12, 23]])

        # Teste com resultados esperados
        self.assertEqual(median_SUS(example, "a"), 5.0)
        self.assertEqual(median_SUS(example, "b"), 6.0)
        
        # Teste com tratamento de exceção
        self.assertEqual(median_SUS(example, "d"), "Chave fora da formatação necessária")
        self.assertEqual(median_SUS("d", example), "Argumentos inadequados")

    def test_mean(self):

        #Criando um df exemplo para os teste 
        example = pd.DataFrame(columns=["a", "b", "c"], 
                               data=[[1, 2, 3], [7, 6, 8], [13, 7, 23]])

        # Teste com resultados esperados
        self.assertEqual(mean_SUS(example, "a"), 7.0)
        self.assertEqual(mean_SUS(example, "b"), 5.0)
        
        # Teste com tratamento de exceção
        self.assertEqual(mean_SUS(example, "d"), "Chave fora da formatação necessária")
        self.assertEqual(mean_SUS("d", example), "Argumentos inadequados")

    def test_min_max_SUS(self):

        #Criando um df exemplo para os teste 
        example = pd.DataFrame(columns=["a", "b", "c"], 
                               data=[[1, 2, 3], [7, 6, 8], [13, 7, 23]])

        # Teste com resultados esperados
        self.assertEqual(max_min_SUS(example, "a"), (1,13))
        self.assertEqual(max_min_SUS(example, "c"), (3,23))
        
        # Teste com tratamento de exceção
        self.assertEqual(max_min_SUS(example, "d"), "Chave fora da formatação necessária")
        self.assertEqual(max_min_SUS("d", example), "Argumentos inadequados")

    def test_std_SUS(self):

        #Criando um df exemplo para os teste 
        example = pd.DataFrame(columns=["a", "b", "c"], 
                               data=[[1, 2, 3], [7, 6, 8], [13, 7, 23]])

        # Teste com resultados esperados
        self.assertEqual(std_SUS(example, "a"), 6.0)
        self.assertEqual(std_SUS(example, "b"), 2.6457513110645907)
        
        # Teste com tratamento de exceção
        self.assertEqual(std_SUS(example, "d"), "Chave fora da formatação necessária")
        self.assertEqual(std_SUS("d", example), "Argumentos inadequados")


if __name__ == '__main__':
    unittest.main()