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
    

# Função que elimina coluna em que todas as células são NA
def delete_columns_na(df: pd.DataFrame)-> pd.DataFrame:
    """
    Recebe um dataframe e elimina as colunas em que todos
    os valores são NA.

    :param df: DataFrame fornecido.

    :type df: DataFrame  
    
    :return: Retorna outro DataFrame.
    
    A função recebrá um DataFrame e as colunas que tiverem 
    TODOS os valores com NA serão removidas.

    .. warning:: A mudança ocorre `inplace`, ou seja, modifica o dataframe original.

    >>> test_data = {"Aluno": ["João", "Maria", "José"],"Curso": ["Economia", "Biologia", "Pedagogia"],"Trancamento do curso": [None, None , None ]}
    >>> df_test = pd.DataFrame(test_data, index = ["1", "2", "3"])

    Teste normal

    >>> delete_columns_na(df_test)
       Aluno      Curso
    1   João   Economia
    2  Maria   Biologia
    3   José  Pedagogia

    >>> delete_columns_na("A")
    "Argumento 'df' não é um dataframe"

    """
    try:

        df.dropna(how = "all", axis = 1, inplace = True)
        return df
    except AttributeError:
        return "Argumento 'df' não é um dataframe"
    except:
        return "Erro desconhecido"
    

# Função que coloca as colunas explícitas para análise sobre hospitais públicos, privados e filantrópicos
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

    .. warning:: O paramêtro date precisa estar no formato 202001, anomês.
    
    Teste para função formatar

    >>> data = {'Data': [202301, 202301, 202301, 202301, 202301, 202301],'Estado': ['SP', 'RJ', 'SP', 'RJ','SP', 'RJ'], 'Tipo_Hospital': ['HOSPITAL_FILANTROPICO', 'HOSPITAL_FILANTROPICO', 'HOSPITAL_PRIVADO', 'HOSPITAL_PRIVADO','HOSPITAL_PUBLICO', 'HOSPITAL_PUBLICO'], 'Valor': [100, 200, 150, 50, 202, 154],"Nome" : ["Hospital Santa Esperança", "Instituto Médico Vital", "Centro Hospitalar Estrela da Manhã", "Hospital São Lucas", "Clínica Médica da Esperança", "Hospital das Crianças Felizes"]}
    >>> example = pd.DataFrame(data)
    >>> example.set_index(["Data", "Nome"], inplace=True)
    >>> formatar_df(example, 202301, 'Estado', 'Tipo_Hospital', 'Valor')
      Estado  Hospital Filantrópico  Hospital Privado  Hospital Público
    0     SP                    100               150               202
    1     RJ                    200                50               154
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


def filtra_year(df: pd.DataFrame, período: int )-> pd.DataFrame:
    """
    Formatação para extração das informações necesssárias.

    :param df: DataFrame original.
    :type df: pd.DataFrame

    :param período: Competência das análises, em formato anomês, 202001. 
    :type date: int

    :return: Retorna um DataFrame com os dados filtrados pelo período especificado.
    :rtype: pd.DataFrame

    .. warning:: O paramêtro date precisa estar no formato 202001, anomês.
    """
    try:
        df_filtrado = df[df["COMP"] == período]
        return  df_filtrado
    
    except AttributeError:
        return "Argumento 'df' não é um dataframe"
    except KeyError:
        return "Coluna não encontrada"
    except:
        return "Erro desconhecido"


    

##GRÁFICO DE BARRAS - LEITOS PEDIÁTRICOS
# Gerando um novo data frame a partir do data
def generate_bar_chart_data(data, group_column, value_column):
    """
    Gera os dados para um gráfico de barras a partir de um DataFrame agrupado.

    :param data: DataFrame contendo os dados.
    :type data: pandas.DataFrame
    :param group_column: Nome da coluna para agrupamento.
    :type group_column: str
    :param value_column: Nome da coluna para os valores.
    :type value_column: str
    
    :return: Rótulos e valores para o gráfico de barras.
    :rtype: tuple
    """
    grouped_data = data.groupby(group_column)[value_column].sum()
    labels = grouped_data.index.tolist()
    values = grouped_data.values.tolist()
    return labels, values


def clean_data(df):
    """
    Limpa os dados do DataFrame.

    :param df: DataFrame a ser limpo.
    :type df: pandas.DataFrame

    :return: DataFrame limpo.
    :rtype: pandas.DataFrame

    # Doctests

    >>> data = pd.DataFrame({
    ...    'coluna1': [1, 2, 3, 4, 5, 6],
    ...    'coluna2': [None, 2, None, 4, None, 6]
    ... })
    >>> data_limpo = clean_data(data)
    >>> data_limpo
       coluna1  coluna2
    0        1      0.0
    1        2      2.0
    2        3      0.0
    3        4      4.0
    4        5      0.0
    5        6      6.0

    """
    try:
        # Remover linhas duplicadas
        df = df.drop_duplicates()

        # Preencher valores ausentes (NaN)
        df = df.fillna(0)  # Substitua 0 pelo valor desejado

        # Renomear colunas (se necessário)
        df = df.rename(columns={'coluna_antiga': 'nova_coluna'})

        return df
    except Exception as e:
        raise e

if __name__ == "__main__":
    doctest.testmod(verbose = True)