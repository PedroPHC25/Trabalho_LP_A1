import matplotlib.pyplot as plt
import pandas as pd
from df_concatenator import data

def select_columns(df, columns):
    selected_columns = df[columns]
    return selected_columns

subdata = select_columns(data, ["REGIAO", "LEITOS_EXISTENTES"])

subdata.reset_index(inplace = True)
subdata.drop("CNES", axis = 1, inplace = True)
subdata = subdata.groupby(["COMP", "REGIAO"])["LEITOS_EXISTENTES"].sum().reset_index()
subdata["COMP"] = pd.to_datetime(subdata["COMP"], format = "%Y%m")

data_centrooeste = subdata[subdata["REGIAO"] == "CENTRO-OESTE"]
data_nordeste = subdata[subdata["REGIAO"] == "NORDESTE"]
data_norte = subdata[subdata["REGIAO"] == "NORTE"]
data_sudeste = subdata[subdata["REGIAO"] == "SUDESTE"]
data_sul = subdata[subdata["REGIAO"] == "SUL"]

# plt.figure(figsize = (15, 5))
plt.plot(data_centrooeste["COMP"], data_centrooeste["LEITOS_EXISTENTES"],
         data_nordeste["COMP"], data_nordeste["LEITOS_EXISTENTES"],
         data_norte["COMP"], data_norte["LEITOS_EXISTENTES"],
         data_sudeste["COMP"], data_sudeste["LEITOS_EXISTENTES"],
         data_sul["COMP"], data_sul["LEITOS_EXISTENTES"])
plt.show()

print(data_centrooeste)