"""Módulo do gráfico "Leitos x Tipo de gestão"

Este módulo contém as funções necessárias para a análise
e para a geração da visualização dos dados sobre o total de 
leitos nos hospitais do Brasil e os tipos de gestão dos hospitais.
"""

import pandas as pd
import matplotlib.pyplot as plt
from df_concatenator import data

# Função para plotar um gráfico de barras
def graph_line(df, x_column, y_column, title, x_label, y_label, image_graph_name):
    # Ajustando o tamanho do gráfico
    plt.figure(figsize = (10, 6))
    plt.plot(df[x_column], df[y_column], linewidth = 3, color = "black")
    # Configurando os textos
    plt.title(title, fontsize = 16)
    plt.xlabel(x_label, fontsize = 14)
    plt.ylabel(y_label, fontsize = 14)
    plt.tick_params(axis = "x", labelsize = 10)
    plt.tick_params(axis = "y", labelsize = 10)
    # Adicionando ponto como separador de milhar no eixo
    formatter = ticker.FuncFormatter(lambda x, pos: "{:,.0f}".format(x).replace(",", "."))
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.savefig(f"graphs/{image_graph_name}]")
    plt.show()