import pandas as pd

#Elimina coluna em que todas as células são NA
def delete_columns_na(df: pd.DataFrame)-> pd.DataFrame:
    """
    Recebe um dataframe e elimina as colunas em que todos
    os valores são NA.

    :param df: DataFrame fornecido.

    :type df: DataFrame  
    
    :return: Retorna outro DataFrame.
    
    A função recebrá um DataFrame e as colunas que tiverem 
    TODOS os valores com NA serão removidas.

    ..warning::
    A mudança ocorre 'inplace', ou seja, modifica o dataframe 
    original.

    >>> test_data = {"Nome": ["Ana", "Ana", "Bruno", "Bruno", "Ana"],
                     "N° de produtos comprados": [3, 1, 4, 1, 5]}
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

        df.dropna(how = "all", axis = 1, inplace = True)
        return df
    except AttributeError:
        return "Argumento 'df' não é um dataframe"
    except:
        return "Erro desconhecido"
    
print("a")