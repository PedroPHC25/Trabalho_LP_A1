"""Módulo do gráfico "Leitos x Ano"

Este módulo contém as funções necessárias para a análise e para a geração da visualização dos dados sobre o total de leitos nos hospitais do Brasil por ano de 2019 a 2023.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Função para somar dados de uma coluna de acordo com o agrupamento de outra
def group_and_sum(df, column_group, column_sum):
    df = df.groupby(column_group)[column_sum].sum().reset_index()
    return df

# Função para converter uma coluna do dataframe para o formato de data
def date_conversor(df, column, date_format):
    df[column] = pd.to_datetime(df[column], format = date_format)
    return df

# Função para calcular a média dos registros dos anos especificados
def mean_per_year(df, column_date, column_to_calculate, years):
    means = {}
    for each_year in years:
        # Filtra para o ano especificado, calcula a média e adiciona ao dicionário
        means[each_year] = df[df[column_date].dt.year == each_year][column_to_calculate].mean()
    return means

# Função para calcular a mediana dos registros dos anos especificados
def median_per_year(df, column_date, column_to_calculate, years):
    medians = {}
    for each_year in years:
        # Filtra para o ano especificado, calcula a mediana e adiciona ao dicionário
        medians[each_year] = df[df[column_date].dt.year == each_year][column_to_calculate].median()
    return medians

# Função para calcular o desvio padrão dos registros dos anos especificados
def std_per_year(df, column_date, column_to_calculate, years):
    stds = {}
    for each_year in years:
        # Filtra para o ano especificado, calcula o desvio padrão e adiciona ao dicionário
        stds[each_year] = df[df[column_date].dt.year == each_year][column_to_calculate].std()
    return stds

# Função para retornar o máximo e o mínimo dos registros dos anos especificados
def max_and_min_per_year(df, column_date, column_to_calculate, years):
    maxs_and_mins = {}
    for each_year in years:
        # Filtra para o ano especificado, encontra o máximo e o mínimo e adiciona ao dicionário como uma tupla
        maxs_and_mins[each_year] = (df[df[column_date].dt.year == each_year][column_to_calculate].min(),
                                    df[df[column_date].dt.year == each_year][column_to_calculate].max())
    return maxs_and_mins

# Função para plotar um gráfico de linha
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