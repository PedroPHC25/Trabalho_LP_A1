"""
Este módulo contém as funções necessárias para a análise
dos dados sobre o total de leitos nos hospitais do Brasil 
e os tipos de gestão dos hospitais.
"""
import pandas as pd
from df_concatenator import data

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
    
    """
    try:
        df = df[df["TP_GESTAO"] == tipo_gestao]
        desvio_padrao = df[tipo_leito].std()
        return desvio_padrao
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
    
    """
    try:
        df = df[df["TP_GESTAO"] == tipo_gestao]
        nu_distintos = df[tipo_leito].nunique()
        return nu_distintos
    except TypeError:
        print("Argumentos inadequados")
    except KeyError:
        print("Chave fora da formatação necessária")
    except:
        print("Erro desconhecido")




