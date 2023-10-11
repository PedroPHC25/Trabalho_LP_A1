import pandas as pd
from df_concatenator import data

def del_unic_val(df):
    for column in df:
        unic = df[column].unique()
        if len(unic) == 1:
            df.drop(column, axis = 1, inplace = True)
    return df