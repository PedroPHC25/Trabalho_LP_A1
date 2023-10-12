import pandas as pd
from df_concatenator import data

#Elimina coluna em que todas as células são na

def delete_columns_na(df):
    """
    Recebe um dataframe e elimina as colunas em que todos os valores são NA.

    Parameters
    ----------
    df : DataFrame
        Tipo do pandas. 
    
    Returns
    -------
    df
    
    Notes
    -----
    A função funciona "inplace", ou seja, modifica diretamente o DataFrame original.
    
    """
    df.dropna(how = "all", axis = 1, inplace = True)
    return df