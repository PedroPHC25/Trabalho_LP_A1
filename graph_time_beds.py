from data_cleaner_pedro import select_columns, reset_index, not_necessary_columns
from df_concatenator import data
import pandas as pd
import matplotlib.pyplot as plt

def group_and_sum(df, column_group, column_sum):
    df = df.groupby(column_group)[column_sum].sum().reset_index()
    return df

def date_conversor(df, column, date_format):
    df[column] = pd.to_datetime(df[column], format = date_format)
    return df

def mean_per_year(df, column_date, column_to_calculate, years):
    means = {}
    for each_year in years:
        means[each_year] = df[df[column_date].dt.year == each_year][column_to_calculate].mean()
    return means

def median_per_year(df, column_date, column_to_calculate, years):
    medians = {}
    for each_year in years:
        medians[each_year] = df[df[column_date].dt.year == each_year][column_to_calculate].median()
    return medians