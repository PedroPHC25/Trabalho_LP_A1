import pandas as pd

# Função para filtrar apenas as colunas necessárias para a análise e visualização
def select_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Filtra colunas desejadas do dataframe e entrega um dataframe apenas com essas colunas.

    :param df: DataFrame a ser filtrado
    :type df: pandas.DataFrame

    :param columns: Lista com os nomes das colunas a serem mantidas
    :type columns: list

    :return: DataFrame apenas com as colunas especificadas
    :rtype: pandas.DataFrame
    """
    try:
        selected_columns = df[columns]
        return selected_columns
    except TypeError or IndexError:
        return "Argumento(s) inadequado(s)"
    except KeyError:
        return "Coluna(s) não encontrada(s)"
    except:
        return "Erro desconhecido"


# Função para resetar o index do dataframe
def reset_index(df: pd.DataFrame) -> pd.DataFrame:
    """
    Torna o(s) índice(s) do dataframe colunas e atribui ao índice o numérico padrão.

    :param df: DataFrame a ter o índice resetado
    :type df: pandas.DataFrame

    :return: DataFrame com o índice resetado
    :rtype: pandas.DataFrame
    """
    try:
        df.reset_index(inplace = True)
        return df
    except AttributeError:
        return "Argumento não é um dataframe"
    except:
        return "Erro desconhecido"


# Função para excluir colunas desnecessárias do dataframe
def not_necessary_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Exclui colunas especificadas de um dataframe.

    :param df: DataFrame a ser reduzido
    :type df: pandas.DataFrame

    :param columns: Lista com os nomes das colunas a serem removidas
    :type columns: list

    :return: DataFrame sem as colunas especificadas
    :rtype: pandas.DataFrame
    """
    try:
        df.drop(columns, axis = 1, inplace = True)
        return df
    except AttributeError:
        return "Argumento 'df' não é um dataframe"
    except KeyError:
        return "Coluna(s) não encontrada(s)"
    except:
        return "Erro desconhecido"