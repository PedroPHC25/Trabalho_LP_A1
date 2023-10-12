import matplotlib.pyplot as plt
import pandas as pd
from df_concatenator import data

def select_columns(df, columns):
    selected_columns = df[columns]
    return selected_columns

def reset_index(df):
    df.reset_index(inplace = True)
    return df

def not_necessary_columns(df, columns):
    df.drop(columns, axis = 1, inplace = True)
    return df

def group_and_sum(df, column_group, column_sum):
    df = df.groupby(column_group)[column_sum].sum().reset_index()
    return df

def date_conversor(df, column, date_format):
    df[column] = pd.to_datetime(df[column], format = date_format)
    return df