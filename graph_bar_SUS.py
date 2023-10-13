"""Módulo de análise das estatístcas e geração do gráfico

Este módulo contém a análise estatística com a
base já formatada sobre a presença de leitos SUS
em hospitais de várias naturezas e define a função
geradora para o gráfico de barras agrupadas.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from typing import Optional

# TODO adicionar testes

# Função recebe o df e retorna a mediana do tipo hospital requisitado
def median_SUS(df: pd.DataFrame, tipo_hospital: str) -> float:
    """
    Mediana do número de leitos SUS presentes em hospitais de diversas naturezas.

    :param df: DataFrame com colunas explícitas.
    :type df: pd.DataFrame

    :param tipo_hospital: Natureza do hospital que deseja calcular a mediana.
    :type tipo_hospital: str

    :return: Retorna a mediana calculada em float.
    :rtype: float

    A função precisa de um DataFrame formatado com as informações necessárias
    expicitamente como colunas, assim é possível calcular a sua respectiva mediana.

    .. warning::
       O parâmetro tipo_hospital deve estar na formatação correta
       para encontrar a coluna dentro do df inserido.
    """
    try:
        return df[tipo_hospital].median()
    except TypeError:
        print("Argumentos inadequados")
    except KeyError:
        print("Chave fora da formatação necessária")
    except:
        print("Erro desconhecido")


# Função recebe o df e retorna a média do tipo hospital requisitado
def mean_SUS(df: pd.DataFrame, tipo_hospital: str) -> float:
    """
    Média do número de leitos SUS presentes em hospitais de diversas naturezas.

    :param df: DataFrame com colunas explícitas.
    :type df: pd.DataFrame

    :param tipo_hospital: Natureza do hospital que deseja calcular a média.
    :type tipo_hospital: str

    :return: Retorna a média calculada em float.
    :rtype: float

    A função precisa de um DataFrame formatado com as informações necessárias
    expicitamente como colunas, assim é possível calcular a sua respectiva média.

    .. warning::
       O parâmetro tipo_hospital deve estar na formatação correta
       para encontrar a coluna dentro do df inserido.
    """
    try:
        return df[tipo_hospital].mean()
    except TypeError:
        print("Argumentos inadequados")
    except KeyError:
        print("Chave fora da formatação necessária")
    except:
        print("Erro desconhecido")

# Função recebe o df e retorna o desvio padrão do tipo hospital requisitado
def std_SUS(df: pd.DataFrame, tipo_hospital: str) -> float:
    """
    Desvio padrão do número de leitos SUS presentes em hospitais de diversas naturezas.

    :param df: DataFrame com colunas explícitas.
    :type df: pd.DataFrame

    :param tipo_hospital: Natureza do hospital que deseja calcular o desvio padrão.
    :type tipo_hospital: str
    
    :return: Retorna o desvio padrão calculado em float.
    :rtype: float

    A função precisa de um DataFrame formatado com as informações necessárias
    expicitamente como colunas, assim é possível calcular seu respectivo desvio padrão.

    .. warning::
       O parâmetro tipo_hospital deve estar na formatação correta
       para encontrar a coluna dentro do df inserido.
    """
    try:
        return df[tipo_hospital].std()
    except TypeError:
        print("Argumentos inadequados")
    except KeyError:
        print("Chave fora da formatação necessária")
    except:
        print("Erro desconhecido")

# Função recebe o df e retorna o máximo e mínimo do tipo hospital requisitado
def max_min_SUS(df: pd.DataFrame, tipo_hospital: str) -> tuple:
    """
    Máximo e mínimo do número de leitos SUS presentes em hospitais de diversas naturezas

    :param df: DataFrame com colunas explícitas.
    :type df: pd.DataFrame

    :param tipo_hospital: Natureza do hospital que deseja calcular o máximo e mínimo.
    :type tipo_hospital: str
    
    :return: Retorna uma tupla com o mínimo e máximo da coluna.
    :rtype: tuple

    A função precisa de um DataFrame formatado com as informações necessárias
    expicitamente como colunas, assim é possível calcular os respectivos máximos e mínimos.

    .. warning::
       O parâmetro tipo_hospital deve estar na formatação correta
       para encontrar a coluna dentro do df inserido.
    """
    try:
        min = df[tipo_hospital].min()
        max = df[tipo_hospital].max()
        return min, max
    except TypeError:
        print("Argumentos inadequados")
    except KeyError:
        print("Chave fora da formatação necessária")
    except:
        print("Erro desconhecido")

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
        # Definido o eixo x como os registros da tabela   
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
        print("Chave fora da formatação necessária")
    except TypeError:
        print("DataFrame inserido não válido")
    except:
        print("Erro desconhecido")