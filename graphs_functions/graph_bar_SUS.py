"""Módulo de geração do gráfico de barras agrupadas

Este módulo contém a  função geradora do gráfico
sobre a presença de leitos SUS em hospitais de 
várias naturezas.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from typing import Optional
import doctest

# Função recebe o df e as colunas que serão as barras agrupadas 
def graph_SUS(df: pd.DataFrame, 
              y1: str, y2: str, y3: str, 
              title: Optional[str] = "Leitos SUS - Janeiro 2022", 
              image_graph_name: Optional[str] = "graph_SUS", 
              width: Optional[str] = 0.2, 
              colors: Optional[list] = ['royalblue', 'lightseagreen', 'mediumpurple']) -> None:
    """
    Geração do gráfico de barras agrupadas

    :param df: DataFrame com colunas explícitas.
    :type df: pd.DataFrame

    :param y1: Coluna que será a primeira barrra do seu respectivo estado.
    :type y1: str
    
    :param y2: Coluna que será a segunda barrra do seu respectivo estado.
    :type y2: str

    :param y3: Coluna que será a terceira barrra do seu respectivo estado.
    :type y3: str

    :param title: Título do gráfico plotado (opcional).
    :type title: str

    :param image_graph_name: Nome do arquivo imagem (opcional).
    :type image_graph_name: str

    :param width: Largura das barras presentes no gráfico (opcional).
    :type width: float

    :param colors: Lista de cores dos grupos de barras plotados (opcional).
    :type colors: list

    :return: Salva o arquivo imagem na pasta "graphs" e exibe o gráfico gerado.
    :rtype: None

    A função precisa de um DataFrame formatado com as informações necessárias
    expicitamente como colunas, assim é possível plotar suas respectivas barras.

    .. warning::
       A função não tem retorno, o gráfico gerado será salvo na pasta "graphs" e 
       após isso o terminal exibe o gráfico gerado.
    """
    
    try:
        # Definindo o eixo x como os registros da tabela   
        x = np.arange(len(df))

        # Atribuindo as colunas as suas respectivas barras
        bar1 = df[y1]
        bar2 = df[y2]
        bar3 = df[y3]

        # Título, tamanho e ticks 
        plt.figure(figsize = (10, 6))
        plt.title(title, fontsize = 16)
        plt.xticks(x, df["Estado"]) 
            
        # Plotando as barras
        plt.bar(x - width, bar1, width, color=colors[0])
        plt.bar(x, bar2, width, color=colors[1])
        plt.bar(x + width, bar3, width, color=colors[2])
            
        # Adcicionando a legenda    
        legend = [y1, y2, y3]
        plt.legend(legend) 
            
        plt.savefig(f"graphs/{image_graph_name}")
        plt.show()
        
    except KeyError:
        return "Chave fora da formatação necessária"
    except TypeError:
        return "DataFrame inserido não válido"
    except:
        return "Erro desconhecido"

if __name__ == "__main__":
    doctest.testmod(verbose = True)