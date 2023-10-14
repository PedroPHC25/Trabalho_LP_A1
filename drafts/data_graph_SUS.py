"""Módulo de dados para a análise da presença de leitos SUS em janeiro de 2022

Este módulo reúne as manipulações e informações necessárias 
para a geração do gráfico de barras agrupadas, essas informações 
a partir desse módulo ficam explícitas em colunas próprias.
"""

import pandas as pd
import sys
sys.path.append('..\Trabalho_LP_A1')

from df_generator import data
from data_analysis_functions.analysis_functions_SUS import formatar_df
from graphs_functions.graph_bar_SUS import graph_SUS

df_formatado = formatar_df(data,202201, "UF", "DESC_NATUREZA_JURIDICA", "LEITOS_SUS")

# print(df_formatado)
graph_SUS(df_formatado, "Hospital Público", "Hospital Filantrópico", "Hospital Privado")
