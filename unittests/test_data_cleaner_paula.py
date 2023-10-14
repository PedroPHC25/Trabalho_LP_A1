import sys
import unittest
import pandas as pd
sys.path.append('..\Trabalho_LP_A1')
from df_generator_functions import delete_columns_na

class TestDataCleanerPaula (unittest.TestCase):

    def test_delete_columns_na(self):

        # Criando um dataframe para os testes
        test_data = {"Alunos": ["João", "Maria", "José"],
                     "Curso": ["Economia", "Biologia", "Pedagogia"],
                     "Trancamento do curso": [ "", "" , ""]}
        df_test = pd.DataFrame(test_data, index = ["1", "2", "3"])
        print(df_test)

        # DataFrame esperado como retorno da função
        expected_result = pd.DataFrame({"Alunos": ["João", "Maria", "José"],
                    "Curso": ["Economia", "Biologia", "Pedagogia"]},
                    index = ["1", "2", "3"])
        
        # Teste normal
        pd.testing.assert_frame_equal(delete_columns_na(df_test), expected_result)
        # Testes com argumentos inválidos
        self.assertEqual(delete_columns_na("A"), "Argumento 'df' não é um dataframe")
        self.assertEqual(delete_columns_na("Cursos"), "Argumento 'df' não é um dataframe")
        
if __name__ == '__main__':
    unittest.main()

print(df_test)

