import matplotlib.pyplot as plt
from df_concatenator import data

data = data.loc[202201]
data = data.groupby(["UF", "DESC_NATUREZA_JURIDICA"])["LEITOS_SUS"].sum()
print(data)