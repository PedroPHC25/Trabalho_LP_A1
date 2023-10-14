"""Módulo de dados para a análise da presença de leitos SUS em janeiro de 2022

Este módulo reúne as manipulações e informações necessárias 
para a geração do gráfico de barras agrupadas, essas informações 
a partir desse módulo ficam explícitas em colunas próprias.
"""

import pandas as pd
import sys
sys.path.append('..\Trabalho_LP_A1')


#Colocar na main ########################
from data_analysis_functions import analysis_functions_SUS as afs
from graphs_functions import graph_bar_SUS as gbs
import df_generator as dfg
from df_generator import data

# importando os dados manipulados para análise
data_SUS = dfg.data_SUS

# Mediana de cada tipo de hospital nos estados brasileiros
median_hosp_pub = afs.median_SUS(data_SUS, "Hospital Público")
median_hosp_priv = afs.median_SUS(data_SUS, "Hospital Privado")
median_hosp_fil = afs.median_SUS(data_SUS, "Hospital Filantrópico")

print("Mediana pub", median_hosp_pub)
print("Mediana priv",median_hosp_priv)
print("Mediana fil", median_hosp_fil)

# Média de cada tipo de hospital nos estados brasileiros
mean_hosp_pub = afs.mean_SUS(data_SUS, "Hospital Público")
mean_hosp_priv = afs.mean_SUS(data_SUS, "Hospital Privado")
mean_hosp_fil = afs.mean_SUS(data_SUS, "Hospital Filantrópico")

print("media pub",mean_hosp_pub)
print("media priv",mean_hosp_priv)
print("media fil",mean_hosp_fil)

# Desvio padrão de cada tipo de hospital nos estados brasileiros
std_hosp_pub = afs.std_SUS(data_SUS, "Hospital Público")
std_hosp_priv = afs.std_SUS(data_SUS, "Hospital Privado")
std_hosp_fil = afs.std_SUS(data_SUS, "Hospital Filantrópico")

print("std pub",std_hosp_pub)
print("std priv",std_hosp_priv)
print("std fil",std_hosp_fil)

# Mínimo e máximo de cada tipo de hospital nos estados brasileiros
min_max_hosp_pub = afs.max_min_SUS(data_SUS, "Hospital Público")
min_max_hosp_priv = afs.max_min_SUS(data_SUS, "Hospital Privado")
min_max_hosp_fil = afs.max_min_SUS(data_SUS, "Hospital Filantrópico")

print("pub",min_max_hosp_pub)
print("priv",min_max_hosp_priv)
print("fil",min_max_hosp_fil)

# Gerando o gráfico de barras agrupadas
graphbar_SUS = gbs.graph_SUS(data_SUS, "Hospital Público", "Hospital Privado", "Hospital Filantrópico")
#####################################################################


# mudar no df generator######################################3
import df_generator_functions as dfgf
useless = ["NATUREZA_JURIDICA", "NO_LOGRADOURO", "NU_ENDERECO", "NO_COMPLEMENTO", "NO_BAIRRO", "CO_CEP", "NU_TELEFONE", "NO_EMAIL"]
data_SUS = dfgf.not_necessary_columns(data, useless)
data_SUS = dfgf.delete_columns_na(data_SUS)
################################################################3

# DUDA 
data_ped = data.groupby("REGIAO")["TOTAL DE LEITOS PEDIÁTRICOS DE UTI POR REGIÃO"].sum()

# Código html, inserir as observações
'''
<h2>Presença de Leitos SUS em Hospitais públicos, privados e filantrópicos</h2>
        <p style="font-size: 12px;">Mariana Fernandes Rocha</p>
        
        <p style="text-align:justify">Nesta análise observaremos a presença de Leitos SUS em hospitais privados, públicos e finatrópicos, as métricas estatísticas exibidas estão de acordo com a distribuição dos leitos nas respectivas naturezas jurídicas pelos estados brasileiros</p>

        <center>
            <figure class = "html5">
                <img src = "graphs/table_analysis_SUS.png">
                <figcaption style="font-size: 12px;">Tabela 1. Medidas de resumo dos hospitais </figcaption>
            </figure>
        </center>

        <p style="text-align:justify">Hospitais filantrópicos: São instituições privadas, porém sem fins lucrativos, que possuem contrato com o sistema público para prestar atendimento aos pacientes do SUS. Pelo menos 60% dos atendimentos oferecidos pelos hospitais filantrópicos são destinados, obrigatoriamente, ao SUS. As organizações filantrópicas são mantidas com doações de pessoas físicas e de empresas, além de parcerias, convênios e políticas públicas pactuadas com os governos municipais, estaduais e federal.</p>
        <p style="text-align:justify">TEXTO TEXTO TEXTO</p>
        <p style="text-align:justify">TEXTO TEXTO TEXTO</p>

        <center>
            <figure class = "html5">
                <img src = "graphs/graph_SUS.png">
                <figcaption style="font-size: 12px;">Gráfico 1. Leitos SUS</figcaption>
            </figure>
        </center>

        <p style="text-align:justify">CONCLUSÃO</p>
'''
