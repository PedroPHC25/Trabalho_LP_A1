import pandas as pd
from df_concatenator import data

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

    """
    try:

        df.dropna(how = "all", axis = 1, inplace = True)
        return df
    except AttributeError:
        return "Argumento 'df' não é um dataframe"
    except:
        return "Erro desconhecido"
    
