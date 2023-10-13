import pandas as pd
import doctest

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
    
    Teste de mediana
    >>> example = pd.DataFrame(columns=["a", "b", "c"], data=[[1,2,3], [5,6,8], [14,12,23]])
    
    >>> median_SUS(example, "a")
    5.0

    >>> median_SUS(example, "b")
    6.0

    >>> median_SUS(example, "d")
    'Chave fora da formatação necessária'

    >>> median_SUS("d", example)
    'Argumentos inadequados'
    """
    try:
        return df[tipo_hospital].median()
    except TypeError:
        return "Argumentos inadequados"
    except KeyError:
        return "Chave fora da formatação necessária"
    except:
        return "Erro desconhecido"


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
    
    Teste de média
    >>> example = pd.DataFrame(columns=["a", "b", "c"], data=[[1,2,3], [7,6,8], [13,7,23]])
    
    >>> mean_SUS(example, "a")
    7.0

    >>> mean_SUS(example, "b")
    5.0

    >>> mean_SUS(example, "d")
    'Chave fora da formatação necessária'

    >>> mean_SUS("d", example)
    'Argumentos inadequados'
    """
    try:
        return df[tipo_hospital].mean()
    except TypeError:
        return "Argumentos inadequados"
    except KeyError:
        return "Chave fora da formatação necessária" 
    except:
        return "Erro desconhecido"

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

    Teste de desvio padrão
    >>> example = pd.DataFrame(columns=["a", "b", "c"], data=[[1,2,3], [7,6,8], [13,7,23]])
    
    >>> std_SUS(example, "a")
    6.0

    >>> std_SUS(example, "b")
    2.6457513110645907

    >>> std_SUS(example, "d")
    'Chave fora da formatação necessária'

    >>> std_SUS("d", example)
    'Argumentos inadequados'
    """
    try:
        return df[tipo_hospital].std()
    except TypeError:
        return "Argumentos inadequados"
    except KeyError:
        return "Chave fora da formatação necessária"
    except:
        return "Erro desconhecido"

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
        return "Argumentos inadequados" 
    except KeyError:
        return "Chave fora da formatação necessária" 
    except:
        return "Erro desconhecido"
    
if __name__ == "__main__":
    doctest.testmod(verbose = True)