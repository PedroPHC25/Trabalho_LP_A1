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



subdata = select_columns(data, ["LEITOS_EXISTENTES"])
subdata = reset_index(subdata)
subdata = not_necessary_columns(subdata, "CNES")
subdata = group_and_sum(subdata, ["COMP"], "LEITOS_EXISTENTES")
subdata = date_conversor(subdata, "COMP", "%Y%m")

# print(subdata)

# print(subdata[subdata["COMP"].dt.year == 2019]["LEITOS_EXISTENTES"].mean())
# print(subdata[subdata["COMP"].dt.year == 2020]["LEITOS_EXISTENTES"].mean())
# print(subdata[subdata["COMP"].dt.year == 2021]["LEITOS_EXISTENTES"].mean())
# print(subdata[subdata["COMP"].dt.year == 2022]["LEITOS_EXISTENTES"].mean())
# print(subdata[subdata["COMP"].dt.year == 2023]["LEITOS_EXISTENTES"].mean())

# print(subdata[subdata["COMP"].dt.year == 2019]["LEITOS_EXISTENTES"].median())
# print(subdata[subdata["COMP"].dt.year == 2020]["LEITOS_EXISTENTES"].median())
# print(subdata[subdata["COMP"].dt.year == 2021]["LEITOS_EXISTENTES"].median())
# print(subdata[subdata["COMP"].dt.year == 2022]["LEITOS_EXISTENTES"].median())
# print(subdata[subdata["COMP"].dt.year == 2023]["LEITOS_EXISTENTES"].median())

# print(subdata[subdata["COMP"].dt.year == 2019]["LEITOS_EXISTENTES"].std())
# print(subdata[subdata["COMP"].dt.year == 2020]["LEITOS_EXISTENTES"].std())
# print(subdata[subdata["COMP"].dt.year == 2021]["LEITOS_EXISTENTES"].std())
# print(subdata[subdata["COMP"].dt.year == 2022]["LEITOS_EXISTENTES"].std())
# print(subdata[subdata["COMP"].dt.year == 2023]["LEITOS_EXISTENTES"].std())

# print(subdata[subdata["COMP"].dt.year == 2019]["LEITOS_EXISTENTES"].max())
# print(subdata[subdata["COMP"].dt.year == 2020]["LEITOS_EXISTENTES"].max())
# print(subdata[subdata["COMP"].dt.year == 2021]["LEITOS_EXISTENTES"].max())
# print(subdata[subdata["COMP"].dt.year == 2022]["LEITOS_EXISTENTES"].max())
# print(subdata[subdata["COMP"].dt.year == 2023]["LEITOS_EXISTENTES"].max())

# print(subdata[subdata["COMP"].dt.year == 2019]["LEITOS_EXISTENTES"].min())
# print(subdata[subdata["COMP"].dt.year == 2020]["LEITOS_EXISTENTES"].min())
# print(subdata[subdata["COMP"].dt.year == 2021]["LEITOS_EXISTENTES"].min())
# print(subdata[subdata["COMP"].dt.year == 2022]["LEITOS_EXISTENTES"].min())
# print(subdata[subdata["COMP"].dt.year == 2023]["LEITOS_EXISTENTES"].min())

# print(subdata)

# print(data_2019)


# plt.plot(subdata["COMP"], subdata["LEITOS_EXISTENTES"])


# plt.show()