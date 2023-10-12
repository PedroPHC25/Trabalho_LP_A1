import pandas as pd
from df_concatenator import data

#Elimina coluna em que todas as células são na

def delete_columns_na(df):
    df.dropna(how = "all", axis = 1, inplace = True)
    return df

print(delete_columns_na(data))


