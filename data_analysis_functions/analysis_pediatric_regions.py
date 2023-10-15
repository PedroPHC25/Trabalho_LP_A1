import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

def calcular_estatisticas(tupla):
    """
    Calcula a média, mediana, desvio padrão e variância de uma lista de números.

    :param tupla: Tupla contendo uma lista de rótulos de região e uma lista de números.
    :type tupla: tuple
    :return: Um dicionário contendo as estatísticas.
    :rtype: dict

    Exemplo:
    >>> calcular_estatisticas((['CENTRO-OESTE', 'NORDESTE', 'NORTE', 'SUDESTE', 'SUL'], [30450, 55476, 22550, 150046, 35870]))
    {'Média': 63878.4, 'Mediana': 35870.0, 'Desvio Padrão': 44653.90232867641, 'Variância': 1995723475.2}
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

