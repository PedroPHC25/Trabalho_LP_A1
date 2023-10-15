"""
Este módulo contém as funções necessárias para a análise
dos dados sobre o total de leitos nos hospitais do Brasil 
e os tipos de gestão dos hospitais.
"""
import pandas as pd
import doctest

# Função recebe o df e retorna a média do número de leitos correspondente ao tipo de gestão recebido
def mean_by_management(df: pd.DataFrame, tipo_gestao:str, tipo_leito: str) -> float:
    """
    Média do número de leitos, que pode ser LEITOS_SUS ou LEITOS_EXISTENTES, presentes em hospitais de diferentes tipos de gestão.

    :param df: DataFrame.
    :type df: pd.DataFrame

    :param tipo_gestao: especiicação do tipo de gestão a ser calculada a média (Municipal, Estadual, Dupla, Sem Gestã).
    :type tipo_gestao: str
    
    :return: Retorna a média em float.
    :rtype: float

    .. warning::
    O parâmetro tipo_gestao e tipo_leito deve exister e estar ecrito corretamente
    para encontrar a coluna dentro do df inserido.

    Teste média 

    >>> test_data ={"TP_GESTAO":["M", "E", "D", "S", "M", "M", "E", "E"], "LEITOS_SUS":[2, 3, 6, 4, 2, 4, 3, 1], "LEITOS_EXISTENTES":[4, 5, 7, 5, 3, 6, 2, 1]}
    >>> df_test = pd.DataFrame(test_data, index = ["A", "B", "C", "D", "E", "F", "G", "H"]) 

    Teste normal
    >>> mean_by_management(df_test, "M", "LEITOS_SUS")
    2.6666666666666665

    Teste argumentos inadequados
    >>> mean_by_management(1, "M", "LEITOS_SUS")
    Argumentos inadequados

    Teste chave fora da formação
    >>> mean_by_management(df_test, 1, 2)
    Chave fora da formatação necessária

    """
    
    try:
        df = df[df["TP_GESTAO"] == tipo_gestao]
        mean = df[tipo_leito].mean()
        if mean != None:
            return mean
    
    except TypeError:
        print("Argumentos inadequados")
    except KeyError:
        print("Chave fora da formatação necessária")
    except:
        print("Erro desconhecido")


# Função recebe o df e retorna a mediana do número de leitos correspondente ao tipo de gestão recebido
def median_by_management(df: pd.DataFrame, tipo_gestao:str, tipo_leito: str) -> float:
    """
    Mediana do número de leitos, que podem ser LEITOS_SUS ou LEITOS_EXISTENTES, presentes em hospitais de diferentes tipos de gestão.

    :param df: DataFrame.
    :type df: pd.DataFrame

    :param tipo_gestao: especiicação do tipo de gestão a ser calculada a mediana (Municipal, Estadual, Dupla, Sem Gestã).
    :type tipo_gestao: str
    
    :return: Retorna a mediana em float.
    :rtype: float

    .. warning::
    O parâmetro tipo_gestao e tipo_leito deve exister e estar ecrito corretamente
    para encontrar a coluna dentro do df inserido.

    Teste mediana

    >>> test_data ={"TP_GESTAO":["M", "E", "D", "S", "M", "M", "E", "E"], "LEITOS_SUS":[2, 3, 6, 4, 2, 4, 3, 1], "LEITOS_EXISTENTES":[4, 5, 7, 5, 3, 6, 2, 1]}
    >>> df_test = pd.DataFrame(test_data, index = ["A", "B", "C", "D", "E", "F", "G", "H"]) 

    Teste normal
    >>> median_by_management(df_test, "M", "LEITOS_SUS")
    2.0

    Teste argumentos inadequados
    >>> median_by_management(1, "M", "LEITOS_SUS")
    Argumentos inadequados

    Teste chave fora da formação
    >>> median_by_management(df_test, 1, 2)
    Chave fora da formatação necessária
    """
    try:
        df = df[df["TP_GESTAO"] == tipo_gestao]
        median = df[tipo_leito].median()
        return median
    except TypeError:
        print("Argumentos inadequados")
    except KeyError:
        print("Chave fora da formatação necessária")
    except:
        print("Erro desconhecido")


# Função recebe o df e retorna o desvio padrão do número de leitos correspondente ao tipo de gestão recebido
def std_by_management(df: pd.DataFrame, tipo_gestao:str, tipo_leito: str) -> float:
    """
    Desvio padrão do número de leitos, que podem ser LEITOS_SUS ou LEITOS_EXISTENTES, presentes em hospitais de diferentes tipos de gestão.

    :param df: DataFrame.
    :type df: pd.DataFrame

    :param tipo_gestao: especiicação do tipo de gestão a ser calculada o desvio padrão (Municipal, Estadual, Dupla, Sem Gestã).
    :type tipo_gestao: str
    
    :return: Retorna o desvio padrão em float.
    :rtype: float

    .. warning::
    O parâmetro tipo_gestao e tipo_leito deve exister e estar ecrito corretamente
    para encontrar a coluna dentro do df inserido.
    
    Teste desvio padrão

    >>> test_data ={"TP_GESTAO":["M", "E", "D", "S", "M", "M", "E", "E"], "LEITOS_SUS":[2, 3, 6, 4, 1, 3, 3, 1], "LEITOS_EXISTENTES":[4, 5, 7, 5, 3, 6, 2, 1]}
    >>> df_test = pd.DataFrame(test_data, index = ["A", "B", "C", "D", "E", "F", "G", "H"]) 

    Teste normal
    >>> std_by_management(df_test, "M", "LEITOS_SUS")
    1.0

    Teste argumentos inadequados
    >>> std_by_management(1, "M", "LEITOS_SUS")
    Argumentos inadequados

    Teste chave fora da formação
    >>> std_by_management(df_test, 1, 2)
    Chave fora da formatação necessária
    
    """
    try:
        df = df[df["TP_GESTAO"] == tipo_gestao]
        desvio_padrao = df[tipo_leito].std()
        return desvio_padrao
    
    except AttributeError:
        return "Argumento 'df' não é um dataframe"
    except TypeError:
        print("Argumentos inadequados")
    except KeyError:
        print("Chave fora da formatação necessária")
    except:
        print("Erro desconhecido")

#Função recebe o df e retorna a quantidade de elementos distintos do número de leitos correspondente ao tipo de gestão recebido
def unique_by_management(df: pd.DataFrame, tipo_gestao:str, tipo_leito: str) -> int:
    """
    Quantidade de elementos distintos do número de leitos, que podem ser LEITOS_SUS ou LEITOS_EXISTENTES, presentes em hospitais de
    diferentes tipos de gestão.

    :param df: DataFrame.
    :type df: pd.DataFrame

    :param tipo_gestao: especiicação do tipo de gestão a ser calculada os valores únicos (Municipal, Estadual, Dupla, Sem Gestã).
    :type tipo_gestao: str
    
    :return: Retorna os valores único.
    :rtype: int

    .. warning::
    O parâmetro tipo_gestao e tipo_leito deve exister e estar ecrito corretamente
    para encontrar a coluna dentro do df inserido.

    Teste valores únicos

    >>> test_data ={"TP_GESTAO":["M", "E", "D", "S", "M", "M", "E", "E"], "LEITOS_SUS":[2, 3, 6, 4, 1, 3, 3, 1], "LEITOS_EXISTENTES":[4, 5, 7, 5, 3, 6, 2, 1]}
    >>> df_test = pd.DataFrame(test_data, index = ["A", "B", "C", "D", "E", "F", "G", "H"]) 

    Teste normal
    >>> unique_by_management(df_test, "M", "LEITOS_SUS")
    3

    Teste argumentos inadequados
    >>> unique_by_management(1, "M", "LEITOS_SUS")
    Argumentos inadequados

    Teste chave fora da formação
    >>> unique_by_management(df_test, 1, 2)
    Chave fora da formatação necessária
    
    
    """
    try:
        df = df[df["TP_GESTAO"] == tipo_gestao]
        nu_distintos = df[tipo_leito].nunique()
        return nu_distintos
    
    except AttributeError:
        return "Argumento 'df' não é um dataframe"
    except TypeError:
        print("Argumentos inadequados")
    except KeyError:
        print("Chave fora da formatação necessária")
    except:
        print("Erro desconhecido")

if __name__ == "__main__":
    doctest.testmod(verbose = True)


