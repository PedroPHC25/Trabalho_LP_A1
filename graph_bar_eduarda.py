"""Módulo do gráfico de barras "Total de leitos pediátricos X Região do Brasil"

Este módulo contém a função que gera o gráfico de barras da quantidade total de leitos pediátricos por região 
do Brasil."""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
from df_generator import data

data_ped = data.groupby("REGIAO")["UTI_PEDIATRICO_EXIST"].sum()

def plot_bar_chart_from_series(data_series, color='pink'):
    """
    Cria um gráfico de barras a partir de uma série de dados.

    :param data_series: A série de dados.
    :type data_series: pandas.Series
    :param color: A cor das barras (opcional, padrão é 'pink').
    :type color: str
    """
    plt.figure(figsize=(10, 6))
    plt.bar(data_series.index, data_series.values, color=color)
    plt.title('UTI Pediátrica Existente por Região')
    plt.xlabel('Região')
    plt.ylabel('UTI Pediátrica Existente')
    plt.xticks(rotation=45)
    plt.show()


# Supondo que 'data_ped' seja a sua série de dados
plot_bar_chart_from_series(data_ped, color='skyblue')




