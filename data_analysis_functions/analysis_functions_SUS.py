"""Módulo para análise sobre presença a de Leitos SUS

Este módulo define as funções que extraem as métricas
estatísticas sobre a presença de leitos SUS em hospitais
de diversas natureza e a formatação necessária para extrair
tais informações da base original.
"""

import pandas as pd
import doctest

# Função que coloca as colunas explícitas para análise
def formatar_df(df_original: pd.DataFrame, 
                date: int, 
                coluna_group1: str, coluna_group2: str, 
                coluna_num: str) -> pd.DataFrame:
    
    """
    Formatação para extração das informações necesssárias.

    :param df_original: DataFrame original.
    :type df_original: pd.DataFrame

    :param date: Competência das análises, em formato anomês, 202001. 
    :type date: int

    :param coluna_group1: Primeira coluna para o agrupamento.  
    :type date: str

    :param coluna_group2: Segunda coluna para o agrupamento.  
    :type date: str

    :param coluna_group1: Coluna numérica.  
    :type date: str

    :return: Retorna um DataFrame com as colunas formatadas.
    :rtype: pd.DataFrame

    A função deixa explícita as colunas com as informações 
    para análise e plotagem do gráfico.

    .. warning::
       O paramêtro date precisa estar no formato 202001, anomês.
   """
    # Seleciona os dados na data requerida
    df_original = df_original.loc[date]
    # Armazena os estados presentes na tabela
    estados = df_original[coluna_group1].unique()
    # Agrupando por duas colunas e somando uma coluna numérica
    df_original = df_original.groupby([coluna_group1, coluna_group2])[coluna_num].sum()
    
    # Criando o novo df com as colunas desejadas
    df_formatado = pd.DataFrame(columns=["Estado", "Hospital Filantrópico", "Hospital Privado", "Hospital Público"])
    # Iterando para adicionar cada estado e suas estatísticas
    for estado in estados:
            try:    
                # Localizando as informações e organizando em colunas
                nova_linha = [estado, 
                            df_original.loc[estado].loc["HOSPITAL_FILANTROPICO"],
                            df_original.loc[estado].loc["HOSPITAL_PRIVADO"],
                            df_original.loc[estado].loc["HOSPITAL_PUBLICO"]]
                # Adicionando a linha criada
                df_formatado.loc[len(df_formatado)] = nova_linha 
            
            # O estado de Roraima não possui a coluna "Hospital Filatrópico"
            except KeyError:
                nova_linha = [estado, 
                            0,
                            df_original.loc[estado].loc["HOSPITAL_PRIVADO"],
                            df_original.loc[estado].loc["HOSPITAL_PUBLICO"]]
                df_formatado.loc[len(df_formatado)] = nova_linha
    return df_formatado


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
    
    Teste de máximo e mínimo
    >>> example = pd.DataFrame(columns=["a", "b", "c"], data=[[1,2,3], [7,6,8], [13,7,23]])
    
    >>> max_min_SUS(example, "a")
    (1, 13)

    >>> max_min_SUS(example, "c")
    (3, 23)

    >>> max_min_SUS(example, "d")
    'Chave fora da formatação necessária'

    >>> max_min_SUS("d", example)
    'Argumentos inadequados'
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