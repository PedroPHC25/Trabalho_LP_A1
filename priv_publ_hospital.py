from df_concatenator import data
import pandas as pd

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
print(df_formatado)    