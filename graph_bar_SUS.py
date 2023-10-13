"""Módulo de análise das estatístcas e geração do gráfico

Este módulo contém a análise estatística com a
base já formatada sobre a presença de leitos SUS
em hospitais de várias naturezas e define a função
geradora para o gráfico de barras agrupadas.
"""

from data_graph_SUS import df_formatado
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def graph_SUS(df: pd.DataFrame, 
              y1: str, y2: str, y3: str, 
              title: str, image_graph_name: str, 
              legend: list = ["Hospital Filantrópico", "Hospital Privado", "Hospital Público"], 
              width: float = 0.2, 
              colors: list = ['royalblue', 'lightseagreen', 'mediumpurple']) -> None:
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

# TODO adicionar comentários, adicionar tratamento de exceção, adicionar testes, adicionar docstring, adicionar a análise estatística

def median_SUS(df: pd.DataFrame, tipo_hospital: str):
    return df[tipo_hospital].median()

def mean_SUS(df: pd.DataFrame, tipo_hospital: str):
    return df[tipo_hospital].mean()

def std_SUS(df: pd.DataFrame, tipo_hospital: str):
    return df[tipo_hospital].std()

def max_min_SUS(df: pd.DataFrame, tipo_hospital: str):
    min = df[tipo_hospital].min()
    max = df[tipo_hospital].max()
    return min, max

print(median_SUS(df_formatado, "Hospital Público"))
print(mean_SUS(df_formatado, "Hospital Público"))
print(std_SUS(df_formatado, "Hospital Público"))
print(max_min_SUS(df_formatado, "Hospital Público"))