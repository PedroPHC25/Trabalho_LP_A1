"""Módulo do gráfico de barras "Total de leitos pediátricos X Região do Brasil"

Este módulo contém a função que gera o gráfico de barras da quantidade total de leitos pediátricos por região 
do Brasil."""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
from df_generator import data_ped

def plot_bar_chart_from_tuples(labels, values):
    """
    Cria um gráfico de barras a partir de tuplas de rótulos e valores.

    :param labels: Os rótulos do eixo x.
    :type labels: list
    :param values: Os valores correspondentes no eixo y.
    :type values: list
    :param color: A cor das barras (opcional, padrão é 'pink').
    :type color: str
    """
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='skyblue')
    plt.title('Quantidade de leitos pediátricos existentes X Região brasileira')
    plt.xlabel('Região')
    plt.ylabel('Quantidade de leitos')
    plt.xticks(rotation=45)
    plt.show()


plot_bar_chart_from_tuples(data_ped[0], data_ped[1])
