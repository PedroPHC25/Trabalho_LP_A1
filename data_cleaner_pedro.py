import pandas as pd

# Função para filtrar apenas as colunas necessárias para a análise e visualização
def select_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Filtra colunas desejadas do dataframe e entrega um dataframe apenas com essas colunas.

    :param df: Dataframe a ser filtrado
    :type df: pandas.Dataframe

    :param columns: Lista com os nomes das colunas a serem mantidas
    :type columns: list

    :return: Dataframe apenas com as colunas especificadas
    :rtype: pandas.Dataframe
    """
    selected_columns = df[columns]
    return selected_columns

# Função para resetar o index do dataframe
def reset_index(df: pd.DataFrame) -> pd.DataFrame:
    """
    Torna o(s) índice(s) do dataframe colunas e atribui ao índice o numérico padrão.

    :param df: Dataframe a ter o índice resetado
    :type df: pandas.Dataframe

    :return: Dataframe com o índice resetado
    :rtype: pandas.Dataframe
    """
    df.reset_index(inplace = True)
    return df

# Função para excluir colunas desnecessárias do dataframe
def not_necessary_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Exclui colunas especificadas de um dataframe.

    :param df: Dataframe a ser reduzido
    :type df: pandas.Dataframe

    :param columns: Lista com os nomes das colunas a serem removidas
    :type columns: list

    :return: Dataframe sem as colunas especificadas
    :rtype: pandas.Dataframe
    """
    df.drop(columns, axis = 1, inplace = True)
    return df