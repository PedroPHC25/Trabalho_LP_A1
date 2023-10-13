"""Módulos dos testes do df_generator_functions

Este módulo contém todos os testes unitários das funções do módulo "df_generator_functions".
"""

import sys
import unittest
import pandas as pd
sys.path.append('..\Trabalho_LP_A1')

from df_generator_functions import select_columns, reset_index, not_necessary_columns

class TestDFGeneratorFunctions(unittest.TestCase):

    def test_select_columns(self):

        # Criando um dataframe para os testes
        test_data = {"Nome": ["Ana", "Beatriz", "Carlos"],
                     "Idade": [33, 41, 19],
                     "Estado natal": ["Rio de Janeiro", "São Paulo", "Rio Grande do Sul"]}
        df_test = pd.DataFrame(test_data, index = ["A", "B", "C"])

        # DataFrame esperado como retorno da função
        expected_result = pd.DataFrame({"Nome": ["Ana", "Beatriz", "Carlos"], "Idade": [33, 41, 19]},
                                       index = ["A", "B", "C"])
        
        # Teste normal
        pd.testing.assert_frame_equal(select_columns(df_test, ["Nome", "Idade"]), expected_result)
        # Testes com argumentos inválidos
        self.assertEqual(select_columns(1, ["Nome", "Estado natal"]), "Argumento(s) inadequado(s)")
        self.assertEqual(select_columns("A", ["Nome", "Estado natal"]), "Argumento(s) inadequado(s)")
        # Teste com coluna inexistente
        self.assertEqual(select_columns(df_test, ["Nome", "Cidade"]), "Coluna(s) não encontrada(s)")


    def test_reset_index(self):

        # Criando um dataframe para os testes
        test_data = {"Nome": ["Ana", "Beatriz", "Carlos"],
                     "Idade": [33, 41, 19],
                     "Estado natal": ["Rio de Janeiro", "São Paulo", "Rio Grande do Sul"]}
        df_test = pd.DataFrame(test_data, index = ["A", "B", "C"])

        # Dataframe esperado como retorno da função
        expected_result = pd.DataFrame({"index": ["A", "B", "C"],
                                        "Nome": ["Ana", "Beatriz", "Carlos"],
                                        "Idade": [33, 41, 19],
                                        "Estado natal": ["Rio de Janeiro", "São Paulo", "Rio Grande do Sul"]})
        
        # Teste normal
        pd.testing.assert_frame_equal(reset_index(df_test), expected_result)
        # Teste com argumento não dataframe
        self.assertEqual(reset_index(1), "Argumento não é um dataframe")


    def test_not_necessary_columns(self):

        # Criando um dataframe para os testes
        test_data = {"Nome": ["Ana", "Beatriz", "Carlos"],
                     "Idade": [33, 41, 19],
                     "Estado natal": ["Rio de Janeiro", "São Paulo", "Rio Grande do Sul"]}
        df_test = pd.DataFrame(test_data, index = ["A", "B", "C"])

        # Dataframe esperado como retorno da função
        expected_result = pd.DataFrame({"Nome": ["Ana", "Beatriz", "Carlos"],
                                        "Idade": [33, 41, 19]}, index = ["A", "B", "C"])
        
        # Teste normal
        pd.testing.assert_frame_equal(not_necessary_columns(df_test, ["Estado natal"]), expected_result)
        # Teste com argumento "df" não dataframe
        self.assertEqual(not_necessary_columns("A", ["Estado natal"]), "Argumento 'df' não é um dataframe")
        # Teste com coluna inexistente
        self.assertEqual(not_necessary_columns(df_test, ["Cidade"]), "Coluna(s) não encontrada(s)")


if __name__ == '__main__':
    unittest.main()