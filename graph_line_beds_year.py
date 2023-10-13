"""Módulo do gráfico "Leitos x Ano"

Este módulo contém as funções necessárias para a análise e para a geração da visualização dos dados sobre o total de leitos nos hospitais do Brasil por ano de 2019 a 2023.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from typing import Optional
import doctest


# Função para somar dados de uma coluna de acordo com o agrupamento de outra
def group_and_sum(df: pd.DataFrame, column_group: list, column_sum: list) -> pd.DataFrame:
    """
    Soma os dados de uma ou mais colunas do dataframe com base no agrupamento de outra(s) coluna(s).

    :param df: DataFrame a ser manipulado
    :type df: pandas.DataFrame

    :param column_group: Coluna(s) a ser(em) agrupada(s)
    :type column_group: list

    :param column_sum: Coluna(s) que terá(ão) os elementos somados.
    :type column_sum: list

    :return: DataFrame alterado
    :rtype: pandas.DataFrame

    >>> test_data = {"Nome": ["Ana", "Ana", "Bruno", "Bruno", "Ana"], "N° de produtos comprados": [3, 1, 4, 1, 5]}
    >>> df_test = pd.DataFrame(test_data, index = ["001", "002", "003", "004", "005"])

    Teste normal
    >>> group_and_sum(df_test, ["Nome"], ["N° de produtos comprados"])
        Nome  N° de produtos comprados
    0    Ana                         9
    1  Bruno                         5

    Teste de argumento 'df' não dataframe
    >>> group_and_sum("A", ["Nome"], ["N° de produtos comprados"])
    "Argumento 'df' não é um dataframe"

    Teste de coluna inexistente
    >>> group_and_sum(df_test, ["Nome"], ["Idade"])
    'Coluna(s) não encontrada(s)'

    Teste de argumento inadequado
    >>> group_and_sum(df_test, ["Nome"], {"A": 1})
    'Argumento inadequado'
    """

    try:
        df = df.groupby(column_group)[column_sum].sum().reset_index()
        return df
    except AttributeError:
        return "Argumento 'df' não é um dataframe"
    except KeyError:
        return "Coluna(s) não encontrada(s)"
    except TypeError:
        return "Argumento inadequado"
    except:
        return "Erro desconhecido"


# Função para converter uma coluna do dataframe para o formato de data
def date_conversor(df: pd.DataFrame, column: str, date_format: str) -> pd.DataFrame:
    """
    Converte os dados de uma coluna do dataframe para o tipo datetime.

    :param df: DataFrame a ser manipulado
    :type df: pandas.DataFrame

    :param column: Coluna cujos dados serão convertidos
    :type column: str

    :param date_format: Formato da informação de data na coluna original
    :type date_format: str

    :return: DataFrame alterado
    :rtype: pandas.DataFrame

    >>> test_data = {"ID_Compra": [111, 222, 333], "Data": [20230127, 20220812, 20200417]}
    >>> df_test = pd.DataFrame(test_data)

    Teste normal
    >>> date_conversor(df_test, "Data", "%Y%m%d")
       ID_Compra       Data
    0        111 2023-01-27
    1        222 2022-08-12
    2        333 2020-04-17

    Teste de coluna inexistente
    >>> date_conversor(df_test, "Mês", "%Y%m%d")
    'Coluna(s) não encontrada(s)'

    Teste de argumento inválido
    >>> date_conversor(1, "Data", "%Y%m%d")
    'Argumento inadequado'

    Teste de coluna inadequada
    >>> date_conversor(df_test, "ID_Compra", "%Y%m%d")
    'Coluna não adequada ao formato passado'
    """

    try:
        df[column] = pd.to_datetime(df[column], format = date_format)
        return df
    except KeyError:
        return "Coluna(s) não encontrada(s)"
    except TypeError:
        return "Argumento inadequado"
    except ValueError:
        return "Coluna não adequada ao formato passado"
    except:
        return "Erro desconhecido"


# Função para calcular a média dos registros dos anos especificados
def mean_per_year(df: pd.DataFrame, column_date: str, column_to_calculate: str, years: list) -> dict:
    """
    Calcula a média dos dados da coluna de um dataframe segmentando-os por ano com base em uma coluna com formato datetime.

    :param df: DataFrame a ser manipulado
    :type df: pandas.DataFrame

    :param column_date: Coluna com a informação de data no formato datetime
    :type column_date: str

    :param column_to_calculate: Coluna que terá as médias dos dados calculadas
    :type column_to_calculate: str

    :param years: Lista com os anos a serem considerados para o cálculo
    :type years: list

    :return: Média dos dados de cada ano especificado
    :rtype: dict

    >>> test_data = {"ID_Doação": [111, 222, 333, 444], "Nome": ["Ana", "Bruno", "Carlos", "Daniela"], "Data": [20210523, 20210810, 20220217, 20221204], "Valor": [100, 200, 200, 500]}
    >>> df_test = pd.DataFrame(test_data)
    >>> df_test["Data"] = pd.to_datetime(df_test["Data"], format = "%Y%m%d")

    Teste normal
    >>> mean_per_year(df_test, "Data", "Valor", [2021, 2022])
    {2021: 150.0, 2022: 350.0}

    Teste de coluna de data inadequada
    >>> mean_per_year(df_test, "Valor", "Valor", [2021, 2022])
    "'column_date' não é do formato datetime"

    Teste de coluna inexistente
    >>> mean_per_year(df_test, "Data", "Quantia", [2021, 2022])
    'Coluna(s) não encontrada(s)'

    Testes de erro de tipo
    >>> mean_per_year(df_test, "Data", "Valor", 1)
    "Argumento inadequado ou 'column_to_calculate' não numérica"
    >>> mean_per_year(df_test, "Data", "Nome", [2021, 2022])
    "Argumento inadequado ou 'column_to_calculate' não numérica"
    """

    try:
        means = {}
        for each_year in years:
            # Filtra para o ano especificado, calcula a média e adiciona ao dicionário
            means[each_year] = df[df[column_date].dt.year == each_year][column_to_calculate].mean()
        return means
    except AttributeError:
        return "'column_date' não é do formato datetime"
    except KeyError:
        return "Coluna(s) não encontrada(s)"
    except TypeError:
        return "Argumento inadequado ou 'column_to_calculate' não numérica"
    except:
        return "Erro desconhecido"
    

# Função para calcular a mediana dos registros dos anos especificados
def median_per_year(df: pd.DataFrame, column_date: str, column_to_calculate: str, years: list) -> dict:
    """
    Calcula a mediana dos dados da coluna de um dataframe segmentando-os por ano com base em uma coluna com formato datetime.

    :param df: DataFrame a ser manipulado
    :type df: pandas.DataFrame

    :param column_date: Coluna com a informação de data no formato datetime
    :type column_date: str

    :param column_to_calculate: Coluna que terá as medianas dos dados calculadas
    :type column_to_calculate: str

    :param years: Lista com os anos a serem considerados para o cálculo
    :type years: list

    :return: Mediana dos dados de cada ano especificado
    :rtype: dict

    >>> test_data = {"ID_Doação": [111, 222, 333, 444], "Nome": ["Ana", "Bruno", "Carlos", "Daniela"], "Data": [20210523, 20210810, 20220217, 20221204], "Valor": [100, 200, 200, 500]}
    >>> df_test = pd.DataFrame(test_data)
    >>> df_test["Data"] = pd.to_datetime(df_test["Data"], format = "%Y%m%d")

    Teste normal
    >>> median_per_year(df_test, "Data", "Valor", [2021, 2022])
    {2021: 150.0, 2022: 350.0}

    Teste de coluna de data inadequada
    >>> median_per_year(df_test, "Valor", "Valor", [2021, 2022])
    "'column_date' não é do formato datetime"

    Teste de coluna inexistente
    >>> median_per_year(df_test, "Data", "Quantia", [2021, 2022])
    'Coluna(s) não encontrada(s)'

    Testes de erro de tipo
    >>> median_per_year(df_test, "Data", "Valor", 1)
    "Argumento inadequado ou 'column_to_calculate' não numérica"
    >>> median_per_year(df_test, "Data", "Nome", [2021, 2022])
    "Argumento inadequado ou 'column_to_calculate' não numérica"
    """

    try:
        medians = {}
        for each_year in years:
            # Filtra para o ano especificado, calcula a mediana e adiciona ao dicionário
            medians[each_year] = df[df[column_date].dt.year == each_year][column_to_calculate].median()
        return medians
    except AttributeError:
        return "'column_date' não é do formato datetime"
    except KeyError:
        return "Coluna(s) não encontrada(s)"
    except TypeError:
        return "Argumento inadequado ou 'column_to_calculate' não numérica"
    except:
        return "Erro desconhecido"


# Função para calcular o desvio padrão dos registros dos anos especificados
def std_per_year(df: pd.DataFrame, column_date: str, column_to_calculate: str, years: list) -> dict:
    """
    Calcula o desvio padrão dos dados da coluna de um dataframe segmentando-os por ano com base em uma coluna com formato datetime.

    :param df: DataFrame a ser manipulado
    :type df: pandas.DataFrame

    :param column_date: Coluna com a informação de data no formato datetime
    :type column_date: str

    :param column_to_calculate: Coluna que terá os desvios padrão dos dados calculados
    :type column_to_calculate: str

    :param years: Lista com os anos a serem considerados para o cálculo
    :type years: list

    :return: Desvios padrão dos dados de cada ano especificado
    :rtype: dict

    >>> test_data = {"ID_Doação": [111, 222, 333, 444], "Nome": ["Ana", "Bruno", "Carlos", "Daniela"], "Data": [20210523, 20210810, 20220217, 20221204], "Valor": [100, 200, 200, 500]}
    >>> df_test = pd.DataFrame(test_data)
    >>> df_test["Data"] = pd.to_datetime(df_test["Data"], format = "%Y%m%d")

    Teste normal
    >>> std_per_year(df_test, "Data", "Valor", [2021, 2022])
    {2021: 70.71067811865476, 2022: 212.13203435596427}

    Teste de coluna de data inadequada
    >>> std_per_year(df_test, "Valor", "Valor", [2021, 2022])
    "'column_date' não é do formato datetime"

    Teste de coluna inexistente
    >>> std_per_year(df_test, "Data", "Quantia", [2021, 2022])
    'Coluna(s) não encontrada(s)'

    Testes de erro de tipo
    >>> std_per_year(df_test, "Data", "Valor", 1)
    "Argumento inadequado ou 'column_to_calculate' não numérica"
    >>> std_per_year(df_test, "Data", "Nome", [2021, 2022])
    "Argumento inadequado ou 'column_to_calculate' não numérica"
    """

    try:
        stds = {}
        for each_year in years:
            # Filtra para o ano especificado, calcula o desvio padrão e adiciona ao dicionário
            stds[each_year] = df[df[column_date].dt.year == each_year][column_to_calculate].std()
        return stds
    except AttributeError:
        return "'column_date' não é do formato datetime"
    except KeyError:
        return "Coluna(s) não encontrada(s)"
    except TypeError:
        return "Argumento inadequado ou 'column_to_calculate' não numérica"
    except:
        return "Erro desconhecido"


# Função para retornar o máximo e o mínimo dos registros dos anos especificados
def max_and_min_per_year(df: pd.DataFrame, column_date: str, column_to_calculate: str, years: list) -> dict:
    """
    Entrega o máximo e o mínimo dos dados da coluna de um dataframe segmentando-os por ano com base em uma coluna com formato datetime.

    :param df: DataFrame a ser manipulado
    :type df: pandas.DataFrame

    :param column_date: Coluna com a informação de data no formato datetime
    :type column_date: str

    :param column_to_calculate: Coluna que terá os máximos e os mínimos procurados
    :type column_to_calculate: str

    :param years: Lista com os anos a serem considerados para o cálculo
    :type years: list

    :return: Máximos e mínimos em forma de uma tupla dos dados de cada ano especificado
    :rtype: dict

    >>> test_data = {"ID_Doação": [111, 222, 333, 444], "Nome": ["Ana", "Bruno", "Carlos", "Daniela"], "Data": [20210523, 20210810, 20220217, 20221204], "Valor": [100, 200, 200, 500]}
    >>> df_test = pd.DataFrame(test_data)
    >>> df_test["Data"] = pd.to_datetime(df_test["Data"], format = "%Y%m%d")

    Teste normal
    >>> max_and_min_per_year(df_test, "Data", "Valor", [2021, 2022])
    {2021: (100, 200), 2022: (200, 500)}

    Teste de coluna de data inadequada
    >>> max_and_min_per_year(df_test, "Valor", "Valor", [2021, 2022])
    "'column_date' não é do formato datetime"

    Teste de coluna inexistente
    >>> max_and_min_per_year(df_test, "Data", "Quantia", [2021, 2022])
    'Coluna(s) não encontrada(s)'

    Teste de argumento inadequado
    >>> max_and_min_per_year(df_test, "Data", "Valor", 1)
    'Argumento inadequado'
    """

    try:
        maxs_and_mins = {}
        for each_year in years:
            # Filtra para o ano especificado, encontra o máximo e o mínimo e adiciona ao dicionário como uma tupla
            maxs_and_mins[each_year] = (df[df[column_date].dt.year == each_year][column_to_calculate].min(),
                                        df[df[column_date].dt.year == each_year][column_to_calculate].max())
        return maxs_and_mins
    except AttributeError:
        return "'column_date' não é do formato datetime"
    except KeyError:
        return "Coluna(s) não encontrada(s)"
    except TypeError:
        return "Argumento inadequado"
    except:
        return "Erro desconhecido"


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
        plt.show()

    except KeyError:
        return "Coluna(s) não encontrada(s)"
    except TypeError:
        return "Argumento inadequado"
    except:
        return "Erro desconhecido"
    

if __name__ == "__main__":
    doctest.testmod(verbose = True)