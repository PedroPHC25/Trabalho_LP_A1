import df_generator as dfg
from data_analysis_functions import analysis_beds_year as aby
from data_analysis_functions import analysis_functions_SUS as afs
from graphs_functions import graph_beds_year as gby
from graphs_functions import graph_bar_SUS as gbs

### DADOS DA ANÁLISE "BEDS_YEAR" ###

# Manipulando o dataframe data_beds_year para a análise
data_beds_year = dfg.data_beds_year
data_beds_year = aby.group_and_sum(data_beds_year, "COMP", "LEITOS_EXISTENTES")
data_beds_year = aby.date_conversor(data_beds_year, "COMP", "%Y%m")

# Média do número de leitos ao longo de cada ano
mean_per_year = aby.mean_per_year(data_beds_year, "COMP", "LEITOS_EXISTENTES", [2019, 2020, 2021, 2022, 2023])
# print(mean_per_year)

# Mediana do número de leitos ao longo de cada ano
median_per_year = aby.median_per_year(data_beds_year, "COMP", "LEITOS_EXISTENTES", [2019, 2020, 2021, 2022, 2023])
# print(median_per_year)

# Desvio padrão do número de leitos ao longo de cada ano
std_per_year = aby.std_per_year(data_beds_year, "COMP", "LEITOS_EXISTENTES", [2019, 2020, 2021, 2022, 2023])
# print(std_per_year)

# Números mínimo e máximo de leitos ao longo de cada ano
max_and_min_per_year = aby.max_and_min_per_year(data_beds_year, "COMP", "LEITOS_EXISTENTES", [2019, 2020, 2021, 2022, 2023])
# print(max_and_min_per_year)

# Gerando um gráfico de linha com base nesses dados
gby.graph_line(data_beds_year, "COMP", "LEITOS_EXISTENTES",
               title = "Número de leitos nos hospitais brasileiros (2019 - 2023)",
               x_label = "Ano", y_label = "Número de leitos", image_graph_name = "graph_beds_year")

# DADOS PARA ANÁLISE DE PRESENÇA DE LEITOS SUS 

# importando os dados manipulados para análise
data_SUS = dfg.data_SUS

# Mediana de cada tipo de hospital nos estados brasileiros
median_hosp_pub = afs.median_SUS(data_SUS, "Hospital Público")
median_hosp_priv = afs.median_SUS(data_SUS, "Hospital Privado")
median_hosp_fil = afs.median_SUS(data_SUS, "Hospital Filantrópico")

# Média de cada tipo de hospital nos estados brasileiros
mean_hosp_pub = afs.mean_SUS(data_SUS, "Hospital Público")
mean_hosp_priv = afs.mean_SUS(data_SUS, "Hospital Privado")
mean_hosp_fil = afs.mean_SUS(data_SUS, "Hospital Filantrópico")

# Desvio padrão de cada tipo de hospital nos estados brasileiros
std_hosp_pub = afs.std_SUS(data_SUS, "Hospital Público")
std_hosp_priv = afs.std_SUS(data_SUS, "Hospital Privado")
std_hosp_fil = afs.std_SUS(data_SUS, "Hospital Filantrópico")

# Mínimo e máximo de cada tipo de hospital nos estados brasileiros
min_max_hosp_pub = afs.max_min_SUS(data_SUS, "Hospital Público")
min_max_hosp_priv = afs.max_min_SUS(data_SUS, "Hospital Privado")
min_max_hosp_fil = afs.max_min_SUS(data_SUS, "Hospital Filantrópico")

# Gerando o gráfico de barras agrupadas
graphbar_SUS = gbs.graph_SUS(data_SUS, "Hospital Público", "Hospital Privado", "Hospital Filantrópico")