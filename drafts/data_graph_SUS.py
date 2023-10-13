"""Módulo de dados para a análise da presença de leitos SUS em janeiro de 2022

Este módulo reúne as manipulações e informações necessárias 
para a geração do gráfico de barras agrupadas, essas informações 
a partir desse módulo ficam explícitas em colunas próprias.
"""

from df_generator import data
import pandas as pd


print(formatar_df(data,202201, "UF", "DESC_NATUREZA_JURIDICA", "LEITOS_SUS" ))
