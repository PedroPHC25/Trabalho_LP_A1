"""Módulo do gráfico "Leitos x Tipo de gestão"

Este módulo contém as funções necessárias para a análise
e para a geração da visualização dos dados sobre o total de 
leitos nos hospitais do Brasil e os tipos de gestão dos hospitais.
"""

import pandas as pd
import  matplotlib.pyplot as plt
from df_concatenator import data
from typing import Optional












































# Função para plotar um gráfico de barras
def graph_bar(df: pd.DataFrame, x_column: str, y_column: str, 
               title: Optional[str] = "", 
               x_label: Optional[str] = "", 
               y_label: Optional[str] = "", 
               image_graph_name: Optional[str] = "graph_line") -> None:
    """
    Plota um gráfico de barras com base em um dataframe e nos parâmetros especificados.

    :param df: Dataframe com os dados
    :type df: pandas.Dataframe

    :param x_column: Coluna cujos dados serão colocados como o eixo x do gráfico
    :type x_column: str

    :param y_column: Coluna cujos dados serão colocados como o eixo y do gráfico
    :type y_column: str

    :param title: Título do gráfico (opcional, padrão é "")
    :type title: str

    :param x_label: Rótulo do eixo x (opcional, padrão é "")
    :type x_label: str

    :param y_label: Rótulo do eixo x (opcional, padrão é "")
    :type y_label: str

    :param image_graph_name: Nome da imagem na qual o gráfico será salvo (opcional, padrão é "graph_bar")
    :type image_graph_name: str

    :return: Salva o gráfico
    
    """
    plt.bar(df[x_column], df[y_column], color = "DarkBlue")

    # Configurando os textos
    plt.title(title, fontsize = 16)
    plt.xlabel(x_label, fontsize = 12)
    plt.ylabel(y_label, fontsize = 12)
    plt.tick_params(axis = "x", labelsize = 10)
    plt.tick_params(axis = "y", labelsize = 10)

    plt.savefig(f"graphs/{image_graph_name}")
    plt.show()

