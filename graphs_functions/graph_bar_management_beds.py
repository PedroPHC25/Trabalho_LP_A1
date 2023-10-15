"""Módulo do gráfico "Leitos x Tipo de gestão"

Este módulo contém as funções necessárias a geração da visualização dos dados sobre o total de 
leitos nos hospitais do Brasil e os tipos de gestão dos hospitais.
"""

import pandas as pd
import  matplotlib.pyplot as plt
from typing import Optional
import doctest

# from df_generator import data_management

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
    
    


# Função para plotar um gráfico de barras
def graph_bar(df: pd.DataFrame, x_column: str, y_column: str, 
               title: Optional[str] = "", 
               x_label: Optional[str] = "", 
               y_label: Optional[str] = "", 
               image_graph_name: Optional[str] = "graph_bar") -> None:
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

    >>> test_data = {"TP_GESTAO":["M", "E", "D", "S", "M", "M", "E", "E"], "LEITOS_SUS":[2, 3, 6, 4, 2, 4, 3, 1], "LEITOS_EXISTENTES":[4, 5, 7, 5, 3, 6, 2, 1]}
    >>> df_test = pd.DataFrame(test_data)

    Teste normal
    
    >>> graph_bar(df_test, "TP_GESTAO", "LEITOS_SUS", title = "Teste gráfico barra", x_label = "Rótulo x", y_label = "Rótulo y", image_graph_name = "Teste")
    
    Teste com coluna inexistente

    >>> graph_bar(df_test, "DATA", "NOME")
    'Coluna(s) não encontrada(s)'

    Teste de argumento inválido

    >>> graph_bar(1, "TP_GESTAO", "LEITOS_SUS")
    'Argumento inadequado'

    """
    try:
        plt.barh(df[x_column], df[y_column], color = "DarkSlateBlue")

        # Configurando os textos
        plt.title(title, fontsize = 16)
        plt.xlabel(x_label, fontsize = 12)
        plt.ylabel(y_label, fontsize = 12)
        plt.tick_params(axis = "x", labelsize = 8)
        plt.tick_params(axis = "y", labelsize = 8)

        plt.savefig(f"graphs/{image_graph_name}")
        # plt.show()

    except KeyError:
        return "Coluna(s) não encontrada(s)"
    except TypeError:
        return "Argumento inadequado"
    except:
        return "Erro desconhecido"

if __name__ == "__main__":
    doctest.testmod(verbose = True)
