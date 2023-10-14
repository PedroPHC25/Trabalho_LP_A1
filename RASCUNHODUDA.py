import pandas as pd
from df_generator import data

def generate_bar_chart_data(data, group_column, value_column):
    """
    Gera os dados para um gráfico de barras a partir de um DataFrame agrupado.

    :param data: DataFrame contendo os dados.
    :type data: pandas.DataFrame
    :param group_column: Nome da coluna para agrupamento.
    :type group_column: str
    :param value_column: Nome da coluna para os valores.
    :type value_column: str
    
    :return: DataFrame com rótulos e valores para o gráfico de barras.
    :rtype: pandas.DataFrame
    """
    grouped_data = data.groupby(group_column)[value_column].sum()
    df = pd.DataFrame({'Labels': grouped_data.index, 'Values': grouped_data.values})
    return df

a = generate_bar_chart_data(data, "REGIAO", "UTI_PEDIATRICO_EXIST")
print(a)