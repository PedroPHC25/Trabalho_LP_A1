import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
from df_generator import data

data_ped = data.groupby("REGIAO")["UTI_PEDIATRICO_EXIST"].sum()
print(data_ped)

import numpy as np

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
        'Média': np.mean(df),
        'Mediana': np.median(df),
        'Desvio Padrão': np.std(df),
        'Máximo': np.max(df),
        'Mínimo': np.min(df),
        'Moda': df.mode()[0],  # A moda pode ter múltiplos valores, pegamos o primeiro
        'Variância': np.var(df)
    }
    
    return statistics

# Agora, para calcular as estatísticas usando a função
data_ped = data.groupby("REGIAO")["UTI_PEDIATRICO_EXIST"].sum()

statistics = calculate_statistics(data_ped)
print(statistics)