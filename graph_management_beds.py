import pandas as pd
# import matplotlib.pyplot as plt
from df_concatenator import data

def select_columns(df, column1, column2, *args):
    """
    Recebe um dataframe e seleciona as colunas desejadas, retorna outro df com essas colunas.

    Parameters
    ----------
    df : DataFrame
        Tipo do pandas.

    column1 : coluna do DataFrame fornecido.

    column2 : coluna do DataFrame fornecido 

    *args : parametros opcional, para o caso
    em que o número de colunas desejadas seja 
    maior que 2. 
    
    Returns
    -------
    df : DataFrame contendo as coluas selecionadas.
    
    """
    new_df = df[[column1, column2, *args]]
    return new_df


# dataframe = select_columns(data, "MUNICIPIO", "REGIAO", "TP_GESTAO", "LEITOS_SUS")

# print(dataframe)
