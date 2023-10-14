import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
from df_generator import data_ped

def calculate_statistics(df):
    """
    Calcula a média, mediana, desvio padrão, valor máximo, valor mínimo, moda e variância de uma coluna em um DataFrame.

    :param df: DataFrame contendo os dados.
    :type df: pandas.Series

    :return: Dicionário contendo as estatísticas calculadas.
    :rtype: dict
    """
    # Calcula as estatísticas
    statistics = {
        'Média': np.mean(df[1]),
        'Mediana': np.median(df[1]),
        'Desvio Padrão': np.std(df[1]),
        'Máximo': np.max(df[1]),
        'Mínimo': np.min(df[1]),
        'Variância': np.var(df[1])
    }
    
    return statistics

statistics = calculate_statistics(data_ped)