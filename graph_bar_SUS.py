"""Módulo de análise das estatístcas e geração do gráfico

Este módulo contém a análise estatística com a
base já formatada sobre a presença de leitos SUS
em hospitais de várias naturezas e define a função
geradora para o gráfico de barras agrupadas.
"""

from data_graph_SUS import df_formatado
import matplotlib.pyplot as plt
import numpy as np

def graph_SUS(df, y1, y2, y3, title, image_graph_name, legend = ["Hospital Filantrópico", "Hospital Privado", "Hospital Público"], width = 0.2, colors = ['royalblue', 'lightseagreen', 'mediumpurple']):
    x = np.arange(len(df))
    plt.figure(figsize = (10, 6))
    plt.title(title, fontsize = 16)
    plt.bar(x - width, y1, width, color=colors[0])
    plt.bar(x, y2, width, color=colors[1])
    plt.bar(x + width, y3, width, color=colors[2])
    plt.xticks(x, df["Estado"]) 
    plt.legend(legend) 
    plt.savefig(f"graphs/{image_graph_name}")
    plt.show()

# TODO adiconar typehint, adicionar comentários, adicionar tratamento de exceção, adicionar testes, adicionar docstring, adicionar a análise estatística

def median_SUS(df, tipo_hospital):
    return df[tipo_hospital].median()

def mean_SUS(df, tipo_hospital):
    return df[tipo_hospital].mean()

def std_SUS(df, tipo_hospital):
    return df[tipo_hospital].std()
