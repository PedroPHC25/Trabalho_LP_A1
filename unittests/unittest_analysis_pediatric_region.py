import unittest
import pandas as pd
import sys

sys.path.append('../Trabalho_LP_A1')
from data_analysis_functions.analysis_pediatric_regions import calcular_estatisticas

class TestAnalysisPediatricRegions(unittest.TestCase):

    def test_calcular_estatisticas(self):
        dados = (['CENTRO-OESTE', 'NORDESTE', 'NORTE', 'SUDESTE', 'SUL'], [30450, 55476, 22550, 150046, 35870])
        estatisticas = calcular_estatisticas(dados)
        
        self.assertIn('Média', estatisticas)
        self.assertIn('Mediana', estatisticas)
        self.assertIn('Desvio Padrão', estatisticas)
        self.assertIn('Variância', estatisticas)
        
        self.assertIsInstance(estatisticas['Média'], float)
        self.assertIsInstance(estatisticas['Mediana'], (int, float))  
        self.assertIsInstance(estatisticas['Desvio Padrão'], float)
        self.assertIsInstance(estatisticas['Variância'], float)

if __name__ == '__main__':
    unittest.main()


if __name__ == "__main__":
    test_calcular_estatisticas()
    print("Todos os testes passaram.")
