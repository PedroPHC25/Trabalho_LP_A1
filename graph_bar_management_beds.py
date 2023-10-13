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

# df = data.head(100)
# df = df[["MUNICIPIO", "LEITOS_SUS", "TP_GESTAO", "LEITOS_EXISTENTES"]]
# print(df)

# graph_bar(df, "TP_GESTAO", "LEITOS_EXISTENTES")

#Função que substitui os códigos de domínio pelo nome extenso
def replacement(df: pd.DataFrame,
                column:str, 
                word: str, 
                new_word: str)-> pd.DataFrame:
    """
    A função substitui todas as repetições da palavra fornecida por 
    outra palavra especificada. 

    :param df: Dataframe com os dados
    :type df: pandas.Dataframe

    :param column: coluna do dataframe que ocorrerá a mudança
    :type column: str

    :param word: palavra que consta inicialmente no df
    :type word: str

    :param new_word: palavra que substituirá a anterior
    :type new_word: str  

    :return: df com as palavras substituidas.
    :rtype: pandas.Dataframe
    """
    try:
        df[column].replace(word, new_word, inplace = True)
        return df
    except TypeError:
        return "Argumento(s) inadequado(s)"
    except KeyError:
        return "Coluna ou palavra não encontrada"


