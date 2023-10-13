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
from typing import Optional

# TODO adicionar tratamento de exceção, adicionar testes, adicionar docstring, adicionar a análise estatística

# Função recebe o df e retorna a mediana do tipo hospital requisitado
def median_SUS(df: pd.DataFrame, tipo_hospital: str) -> float:
    return df[tipo_hospital].median()

# Função recebe o df e retorna a média do tipo hospital requisitado
def mean_SUS(df: pd.DataFrame, tipo_hospital: str) -> float:
    return df[tipo_hospital].mean()

# Função recebe o df e retorna o desvio padrão do tipo hospital requisitado
def std_SUS(df: pd.DataFrame, tipo_hospital: str) -> float:
    return df[tipo_hospital].std()

# Função recebe o df e retorna o máximo e mínimo do tipo hospital requisitado
def max_min_SUS(df: pd.DataFrame, tipo_hospital: str) -> tuple:
    min = df[tipo_hospital].min()
    max = df[tipo_hospital].max()
    return min, max

# Função recebe o df e as colunas que serão as barras agrupadas 
def graph_SUS(df: pd.DataFrame, 
              y1: str, y2: str, y3: str, 
              title: Optional[str] = "Leitos SUS em janeiro 2022", 
              image_graph_name: Optional[str] = "graph_SUS", 
              width: Optional[str] = 0.2, 
              colors: Optional[list] = ['royalblue', 'lightseagreen', 'mediumpurple']) -> None:
    # Definido o eixo x como os registros da tabela
    x = np.arange(len(df))

    # Atribuindo as colunas as suas respectivas barras
    bar1 = df[y1]
    bar2 = df[y2]
    bar3 = df[y3]

    # Título, legenda e ticks 
    legend = [y1, y2, y3]
    plt.legend(legend) 
    plt.figure(figsize = (10, 6))
    plt.title(title, fontsize = 16)
    plt.xticks(x, df["Estado"]) 
    
    # Plotando as barras
    plt.bar(x - width, bar1, width, color=colors[0])
    plt.bar(x, bar2, width, color=colors[1])
    plt.bar(x + width, bar3, width, color=colors[2])
    
    plt.savefig(f"graphs/{image_graph_name}")
    plt.show()

print(type(median_SUS(df_formatado, "Hospital Público")))
print(type(mean_SUS(df_formatado, "Hospital Público")))
print(type(std_SUS(df_formatado, "Hospital Público")))
print(type(max_min_SUS(df_formatado, "Hospital Público")))