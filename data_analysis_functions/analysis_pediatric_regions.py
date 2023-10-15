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
