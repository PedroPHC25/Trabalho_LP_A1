import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
from df_generator import data_ped

import numpy as np

def calcular_estatisticas(tupla):
    """
    Calcula a média, mediana, desvio padrão e variância de uma lista de números.

    :param tupla: Tupla contendo uma lista de rótulos de região e uma lista de números.
    :type tupla: tuple
    :return: Um dicionário contendo as estatísticas.
    :rtype: dict
    """
    rotulos, numeros = tupla
    media = np.mean(numeros)
    mediana = np.median(numeros)
    desvio_padrao = np.std(numeros)
    variancia = np.var(numeros)
    
    estatisticas = {
        'Média': media,
        'Mediana': mediana,
        'Desvio Padrão': desvio_padrao,
        'Variância': variancia
    }
    
    return estatisticas

def test_calcular_estatisticas():
    dados = (['CENTRO-OESTE', 'NORDESTE', 'NORTE', 'SUDESTE', 'SUL'], [30450, 55476, 22550, 150046, 35870])
    estatisticas = calcular_estatisticas(dados)
    
    assert 'Média' in estatisticas
    assert 'Mediana' in estatisticas
    assert 'Desvio Padrão' in estatisticas
    assert 'Variância' in estatisticas
    
    assert isinstance(estatisticas['Média'], float)
    assert isinstance(estatisticas['Mediana'], (int, float))  # Aceita tanto inteiros quanto floats
    assert isinstance(estatisticas['Desvio Padrão'], float)
    assert isinstance(estatisticas['Variância'], float)


if __name__ == "__main__":
    test_calcular_estatisticas()
    print("Todos os testes passaram.")
