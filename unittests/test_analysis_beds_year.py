"""Módulo de testes de analysis_beds_year

Este módulo contém os testes unitários das 6 funções definidas no módulo analysis_beds_year, localizado na pasta data_analysis: group_and_sum, date_conversor, mean_per_year, median_per_year, std_per_year e max_and_min_per_year.
"""

import sys
import unittest
import pandas as pd
sys.path.append('..\Trabalho_LP_A1')

from data_analysis_functions.analysis_beds_year import group_and_sum, date_conversor, mean_per_year, median_per_year, std_per_year, max_and_min_per_year

class TestAnalysisBedsYear(unittest.TestCase):

    def test_group_and_sum(self):

        # Criando um dataframe para os testes
        test_data = {"Nome": ["Ana", "Ana", "Bruno", "Bruno", "Ana"],
                     "N° de produtos comprados": [3, 1, 4, 1, 5]}
        df_test = pd.DataFrame(test_data, index = ["001", "002", "003", "004", "005"])

        # Dataframe esperado como retorno da função
        expected_result = pd.DataFrame({"Nome": ["Ana", "Bruno"],
                                        "N° de produtos comprados": [9, 5]})
        
        # Teste normal
        pd.testing.assert_frame_equal(group_and_sum(df_test, ["Nome"], ["N° de produtos comprados"]), 
                                      expected_result)
        # Teste de argumento "df" não dataframe
        self.assertEqual(group_and_sum("A", ["Nome"], ["N° de produtos comprados"]),
                         "Argumento 'df' não é um dataframe")
        # Teste de coluna inexistente
        self.assertEqual(group_and_sum(df_test, ["Nome"], ["Idade"]), "Coluna(s) não encontrada(s)")
        # Teste de argumento inválido
        self.assertEqual(group_and_sum(df_test, ["Nome"], {"A": 1}), "Argumento inadequado")


    def test_date_conversor(self):

        # Criando um dataframe para os testes
        test_data = {"ID_Compra": [111, 222, 333], "Data": [20230127, 20220812, 20200417]}
        df_test = pd.DataFrame(test_data)

        # Dataframe esperado como retorno da função
        expected_result = pd.DataFrame({"ID_Compra": [111, 222, 333],
                                        "Data": pd.to_datetime(["20230127", "20220812", "20200417"])})
        
        # Teste normal
        pd.testing.assert_frame_equal(date_conversor(df_test, "Data", "%Y%m%d"), expected_result)
        # Teste com coluna inexistente
        self.assertEqual(date_conversor(df_test, "Mês", "%Y%m%d"), "Coluna(s) não encontrada(s)")
        # Teste com argumento inválido
        self.assertEqual(date_conversor(1, "Data", "%Y%m%d"), "Argumento inadequado")
        # Teste com coluna inadequada
        self.assertEqual(date_conversor(df_test, "ID_Compra", "%Y%m%d"),
                         "Coluna não adequada ao formato passado")
        

    def test_mean_per_year(self):

        # Criando um dataframe para os testes
        test_data = {"ID_Doação": [111, 222, 333, 444],
                     "Nome": ["Ana", "Bruno", "Carlos", "Daniela"],
                     "Data": [20210523, 20210810, 20220217, 20221204],
                     "Valor": [100, 200, 200, 500]}
        df_test = pd.DataFrame(test_data)
        df_test["Data"] = pd.to_datetime(df_test["Data"], format = "%Y%m%d")

        # Dicionário esperado como retorno da função
        expected_result = {2021: 150.0, 2022: 350.0}

        # Teste normal
        self.assertEqual(mean_per_year(df_test, "Data", "Valor", [2021, 2022]), expected_result)
        # Teste com coluna inadequada
        self.assertEqual(mean_per_year(df_test, "Valor", "Valor", [2021, 2022]),
                         "'column_date' não é do formato datetime")
        # Teste com coluna inexistente
        self.assertEqual(mean_per_year(df_test, "Data", "Quantia", [2021, 2022]),
                         "Coluna(s) não encontrada(s)")
        # Testes de erro de tipo
        self.assertEqual(mean_per_year(df_test, "Data", "Valor", 1),
                         "Argumento inadequado ou 'column_to_calculate' não numérica")
        self.assertEqual(mean_per_year(df_test, "Data", "Nome", [2021, 2022]),
                         "Argumento inadequado ou 'column_to_calculate' não numérica")
        

    def test_median_per_year(self):

        # Criando um dataframe para os testes
        test_data = {"ID_Doação": [111, 222, 333, 444],
                     "Nome": ["Ana", "Bruno", "Carlos", "Daniela"],
                     "Data": [20210523, 20210810, 20220217, 20221204],
                     "Valor": [100, 200, 200, 500]}
        df_test = pd.DataFrame(test_data)
        df_test["Data"] = pd.to_datetime(df_test["Data"], format = "%Y%m%d")

        # Dicionário esperado como retorno da função
        expected_result = {2021: 150.0, 2022: 350.0}

        # Teste normal
        self.assertEqual(median_per_year(df_test, "Data", "Valor", [2021, 2022]), expected_result)
        # Teste com coluna inadequada
        self.assertEqual(median_per_year(df_test, "Valor", "Valor", [2021, 2022]),
                         "'column_date' não é do formato datetime")
        # Teste com coluna inexistente
        self.assertEqual(median_per_year(df_test, "Data", "Quantia", [2021, 2022]),
                         "Coluna(s) não encontrada(s)")
        # Testes de erro de tipo
        self.assertEqual(median_per_year(df_test, "Data", "Valor", 1),
                         "Argumento inadequado ou 'column_to_calculate' não numérica")
        self.assertEqual(median_per_year(df_test, "Data", "Nome", [2021, 2022]),
                         "Argumento inadequado ou 'column_to_calculate' não numérica")
        

    def test_std_per_year(self):

        # Criando um dataframe para os testes
        test_data = {"ID_Doação": [111, 222, 333, 444],
                     "Nome": ["Ana", "Bruno", "Carlos", "Daniela"],
                     "Data": [20210523, 20210810, 20220217, 20221204],
                     "Valor": [100, 200, 200, 500]}
        df_test = pd.DataFrame(test_data)
        df_test["Data"] = pd.to_datetime(df_test["Data"], format = "%Y%m%d")

        # Dicionário esperado como retorno da função
        expected_result = {2021: 70.71067811865476, 2022: 212.13203435596427}

        # Teste normal
        self.assertEqual(std_per_year(df_test, "Data", "Valor", [2021, 2022]), expected_result)
        # Teste com coluna inadequada
        self.assertEqual(std_per_year(df_test, "Valor", "Valor", [2021, 2022]),
                         "'column_date' não é do formato datetime")
        # Teste com coluna inexistente
        self.assertEqual(std_per_year(df_test, "Data", "Quantia", [2021, 2022]),
                         "Coluna(s) não encontrada(s)")
        # Testes de erro de tipo
        self.assertEqual(std_per_year(df_test, "Data", "Valor", 1),
                         "Argumento inadequado ou 'column_to_calculate' não numérica")
        self.assertEqual(std_per_year(df_test, "Data", "Nome", [2021, 2022]),
                         "Argumento inadequado ou 'column_to_calculate' não numérica")
        

    def test_max_and_min_per_year(self):

        # Criando um dataframe para os testes
        test_data = {"ID_Doação": [111, 222, 333, 444],
                     "Nome": ["Ana", "Bruno", "Carlos", "Daniela"],
                     "Data": [20210523, 20210810, 20220217, 20221204],
                     "Valor": [100, 200, 200, 500]}
        df_test = pd.DataFrame(test_data)
        df_test["Data"] = pd.to_datetime(df_test["Data"], format = "%Y%m%d")

        # Dicionário esperado como retorno da função
        expected_result = {2021: (100, 200), 2022: (200, 500)}

        # Teste normal
        self.assertEqual(max_and_min_per_year(df_test, "Data", "Valor", [2021, 2022]), expected_result)
        # Teste com coluna inadequada
        self.assertEqual(max_and_min_per_year(df_test, "Valor", "Valor", [2021, 2022]),
                         "'column_date' não é do formato datetime")
        # Teste com coluna inexistente
        self.assertEqual(max_and_min_per_year(df_test, "Data", "Quantia", [2021, 2022]),
                         "Coluna(s) não encontrada(s)")
        # Teste com argumento inválido
        self.assertEqual(max_and_min_per_year(df_test, "Data", "Valor", 1), "Argumento inadequado")


if __name__ == '__main__':
    unittest.main()