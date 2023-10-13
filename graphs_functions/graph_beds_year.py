"""Módulo do gráfico "Leitos x Ano"

Este módulo contém a função necessária para a plotagem do gráfico sobre o total de leitos nos hospitais do Brasil por ano de 2019 a 2023.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from typing import Optional
import doctest

# Função para plotar um gráfico de linha
def graph_line(df: pd.DataFrame, x_column: str, y_column: str, 
               title: Optional[str] = "", 
               x_label: Optional[str] = "", 
               y_label: Optional[str] = "", 
               image_graph_name: Optional[str] = "graph_line") -> None:
    """
    Plota um gráfico de linhas com base em um dataframe e nos parâmetros especificados.

    :param df: DataFrame a ter os dados plotados
    :type df: pandas.DataFrame

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

    :param image_graph_name: Nome da imagem na qual o gráfico será salvo (opcional, padrão é "graph_line")
    :type image_graph_name: str

    :return: Salva o gráfico em uma imagem dentro da pasta "graphs" e o exibe.
    :rtype: None

    >>> test_data = {"ID_Fatura": [111, 222, 333, 444], "Data": [20210523, 20210810, 20220217, 20221204], "Valor": [100, 200, 200, 500]}
    >>> df_test = pd.DataFrame(test_data)
    >>> df_test["Data"] = pd.to_datetime(df_test["Data"], format = "%Y%m%d")

    Teste normal
    >>> graph_line(df_test, "Data", "Valor", title = "Teste", x_label = "Rótulo x", y_label = "Rótulo y", image_graph_name = "Teste")

    Teste de coluna inexistente
    >>> graph_line(df_test, "Data", "Quantia")
    'Coluna(s) não encontrada(s)'

    Teste de argumento inválido
    >>> graph_line(1, "Data", "Valor")
    'Argumento inadequado'
    """

    try:
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

        plt.savefig(f"graphs/{image_graph_name}")

    except KeyError:
        return "Coluna(s) não encontrada(s)"
    except TypeError:
        return "Argumento inadequado"
    except:
        return "Erro desconhecido"
    

if __name__ == "__main__":
    doctest.testmod(verbose = True)