"""Módulo de dados para o gráfico de Leitos pertencentes ao SUS

Este módulo reúne as manipulações e informações necessárias 
para a geração do gráfico de barras agrupadas, essas informações 
a partir desse módulo ficam explícitas em colunas próprias.
"""

from df_concatenator import data
import pandas as pd

# Selecionando a data e reunindo somente as colunas necessárias
data = data.loc[202201]
estados = data["UF"].unique()
data = data.groupby(["UF", "DESC_NATUREZA_JURIDICA"])["LEITOS_SUS"].sum()

# Criando um novo df com a formatação correta
df_formatado = pd.DataFrame(columns=["Estado", "Hospital Filantrópico", "Hospital Privado", "Hospital Público"])

# Cria-se uma linha para cada estado
for estado in estados:
        try:    
            # Localizando as informações e organizando em colunas
            nova_linha = [estado, 
                        data.loc[estado].loc["HOSPITAL_FILANTROPICO"],
                        data.loc[estado].loc["HOSPITAL_PRIVADO"],
                        data.loc[estado].loc["HOSPITAL_PUBLICO"]]
            # Adicionando a linha criada
            df_formatado.loc[len(df_formatado)] = nova_linha 
        
        # o estado de Roraima não possui a coluna "Hospital Filatrópico"
        except KeyError:
            nova_linha = [estado, 
                        0,
                        data.loc[estado].loc["HOSPITAL_PRIVADO"],
                        data.loc[estado].loc["HOSPITAL_PUBLICO"]]
            df_formatado.loc[len(df_formatado)] = nova_linha