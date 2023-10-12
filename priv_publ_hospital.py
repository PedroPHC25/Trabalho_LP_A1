from df_concatenator import data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = data.loc[202201]
estados = data["UF"].unique()
data = data.groupby(["UF", "DESC_NATUREZA_JURIDICA"])["LEITOS_SUS"].sum()

df_formatado = pd.DataFrame(columns=["Estado", "Hospital Filantrópico", "Hospital Privado", "Hospital Público"])

for estado in estados:
        try:    
            nova_linha = [estado, 
                        data.loc[estado].loc["HOSPITAL_FILANTROPICO"],
                        data.loc[estado].loc["HOSPITAL_PRIVADO"],
                        data.loc[estado].loc["HOSPITAL_PUBLICO"]]
            df_formatado.loc[len(df_formatado)] = nova_linha 
        except KeyError:
            nova_linha = [estado, 
                        0,
                        data.loc[estado].loc["HOSPITAL_PRIVADO"],
                        data.loc[estado].loc["HOSPITAL_PUBLICO"]]
            df_formatado.loc[len(df_formatado)] = nova_linha

x = np.arange(27)
y1 = df_formatado["Hospital Filantrópico"]
y2 = df_formatado["Hospital Privado"]
y3 = df_formatado["Hospital Público"]
width = 0.2

# Plot com barras agrupadas 
plt.bar(x-0.2, y1, width, color='cyan') 
plt.bar(x, y2, width, color='orange') 
plt.bar(x+0.2, y3, width, color='green') 
plt.xticks(x, list(df_formatado["Estado"])) 
plt.legend(["Hospital Filantrópico", "Hospital Privado", "Hospital Público"]) 
plt.show() 