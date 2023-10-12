import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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

def std_per_year(df, column_date, column_to_calculate, years):
    stds = {}
    for each_year in years:
        stds[each_year] = df[df[column_date].dt.year == each_year][column_to_calculate].std()
    return stds

def max_and_min_per_year(df, column_date, column_to_calculate, years):
    maxs_and_mins = {}
    for each_year in years:
        maxs_and_mins[each_year] = (df[df[column_date].dt.year == each_year][column_to_calculate].min(),
                                    df[df[column_date].dt.year == each_year][column_to_calculate].max())
    return maxs_and_mins

def graph_line(df, x_column, y_column, title, x_label, y_label):
    plt.figure(figsize = (10, 6))
    plt.plot(df[x_column], df[y_column], linewidth = 3, color = "black")
    plt.title(title, fontsize = 16)
    plt.xlabel(x_label, fontsize = 14)
    plt.ylabel(y_label, fontsize = 14)
    plt.tick_params(axis = "x", labelsize = 10)
    plt.tick_params(axis = "y", labelsize = 10)
    formatter = ticker.FuncFormatter(lambda x, pos: "{:,.0f}".format(x).replace(",", "."))
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.savefig("graphs/graph_line_beds_year")
    plt.show()