import pandas as pd
import doctest

#TODO Arrumar os doctests, que estão falhando.

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

    Teste média
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
        return mean
    except TypeError:
        print("Argumentos inadequados")
    except KeyError:
        print("Chave fora da formatação necessária")
    except:
        print("Erro desconhecido")

if __name__ == "__main__":
    doctest.testmod(verbose = True)


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
    2

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
    except AttributeError:
        return "Argumento 'df' não é um dataframe"
    except TypeError:
        print("Argumentos inadequados")
    except KeyError:
        print("Chave fora da formatação necessária")
    except:
        print("Erro desconhecido")
