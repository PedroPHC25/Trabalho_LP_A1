import pandas as pd
from df_concatenator import data

def del_unic_val(df):
    for column in df:
        unic = df[column].unique()
        if len(unic) == 1:
            df.drop(column, axis = 1, inplace = True)
    return df

def useless_column(df, useless):
    df.drop(useless, axis = 1, inplace = True)
    return df

# useless = ["NATUREZA_JURIDICA", "NO_LOGRADOURO", "NU_ENDERECO", "NO_COMPLEMENTO", "NO_BAIRRO", "CO_CEP", "NU_TELEFONE", "NO_EMAIL"]
