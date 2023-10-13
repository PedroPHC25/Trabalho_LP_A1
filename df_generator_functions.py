"""Módulo das funções do "df_generator"

Este módulo contém todas as funções que são chamadas no módulo "df_generator" para a limpeza, manipulação e geração de dataframes para as análises e visualizações.
"""

import pandas as pd
import doctest

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

    >>> test_data = {"Nome": ["Ana", "Beatriz", "Carlos"], "Idade": [33, 41, 19], "Estado natal": ["Rio de Janeiro", "São Paulo", "Rio Grande do Sul"]}
    >>> df_test = pd.DataFrame(test_data, index = ["A", "B", "C"])

    Teste normal
    >>> select_columns(df_test, ["Nome", "Estado natal"])
          Nome       Estado natal
    A      Ana     Rio de Janeiro
    B  Beatriz          São Paulo
    C   Carlos  Rio Grande do Sul

    Testes de argumento inválido
    >>> select_columns(1, ["Nome", "Estado natal"])
    'Argumento(s) inadequado(s)'
    >>> select_columns("A", ["Nome", "Estado natal"])
    'Argumento(s) inadequado(s)'
    
    Teste de coluna inexistente
    >>> select_columns(df_test, ["Nome", "Cidade"])
    'Coluna(s) não encontrada(s)'
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
    
    >>> test_data = {"Nome": ["Ana", "Beatriz", "Carlos"], "Idade": [33, 41, 19], "Estado natal": ["Rio de Janeiro", "São Paulo", "Rio Grande do Sul"]}
    >>> df_test = pd.DataFrame(test_data, index = ["A", "B", "C"])

    Teste normal
    >>> reset_index(df_test)
      index     Nome  Idade       Estado natal
    0     A      Ana     33     Rio de Janeiro
    1     B  Beatriz     41          São Paulo
    2     C   Carlos     19  Rio Grande do Sul

    Teste de argumento não dataframe
    >>> reset_index(1)
    'Argumento não é um dataframe'
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

    >>> test_data = {"Nome": ["Ana", "Beatriz", "Carlos"], "Idade": [33, 41, 19], "Estado natal": ["Rio de Janeiro", "São Paulo", "Rio Grande do Sul"]}
    >>> df_test = pd.DataFrame(test_data, index = ["A", "B", "C"])

    Teste normal
    >>> not_necessary_columns(df_test, ["Estado natal"])
          Nome  Idade
    A      Ana     33
    B  Beatriz     41
    C   Carlos     19

    Teste de argumento 'df' não dataframe
    >>> not_necessary_columns("A", ["Estado natal"])
    "Argumento 'df' não é um dataframe"

    Teste de coluna inexistente
    >>> not_necessary_columns(df_test, ["Cidade"])
    'Coluna(s) não encontrada(s)'
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
    

if __name__ == "__main__":
    doctest.testmod(verbose = True)