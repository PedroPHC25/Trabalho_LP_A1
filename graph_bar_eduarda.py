"""Módulo do gráfico de barras "Total de leitos pediátricos X Região do Brasil"

Este módulo contém a  função que gera o gráfico de barras que permite uma
análise comparativa da quantidade total de leitos pediátricos por região 
do Brasil.
"""

import pandas as pd
import matplotlib.pyplot as plt
from df_concatenator import data
from matplotlib import ticker

# Função para plotar um gráfico de barras
def graph_bar(df, x_column, y_column, title, x_label, y_label, image_graph_name):
    # Ajustando o tamanho do gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(df[x_column], df[y_column], color='pink')  

    # Configurando os textos
    plt.title(title, fontsize=16)
    plt.xlabel(x_label, fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.tick_params(axis="x", labelsize=10)
    plt.tick_params(axis="y", labelsize=10)

    # Adicionando ponto como separador de milhar no eixo
    formatter = ticker.FuncFormatter(lambda x, pos: "{:,.0f}".format(x).replace(",", "."))
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.savefig(f"graphs/{image_graph_name}")
    plt.show()

graph_bar(data, 'REGIAO', 'UTI_PEDIATRICO_EXIST', 'TOTAL DE LEITOS PEDIÁTRICOS DE UTI POR REGIÃO', 'Região', 'Total de leitos pediátricos', 'uti_pediatrico_por_regiao.jpg')
