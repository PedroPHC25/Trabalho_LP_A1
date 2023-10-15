import df_generator as dfg
from data_analysis_functions import analysis_beds_year as aby
from data_analysis_functions import analysis_functions_SUS as afs
from data_analysis_functions import analysis_management_beds as amb
# from data_analysis_functions import analysis_pediatric_regions as apr
from graphs_functions import graph_beds_year as gby
from graphs_functions import graph_bar_SUS as gbs
from graphs_functions import graph_bar_management_beds as gbm
# from graphs_functions import graph_bar_pediatric_region as gbpr
'''
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

# # Gerando um gráfico de linha com base nesses dados
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


### DADOS DA ANÁLISE "BEDS X MANAGEMENT" ###

# importando os dados manipulados para análise
data_management = dfg.data_management

# Média dos leitos existente de cada gestão 
mean_beds_municipal = amb.mean_by_management(data_management, "M", "LEITOS_EXISTENTES")
mean_beds_estadual = amb.mean_by_management(data_management, "E", "LEITOS_EXISTENTES")
mean_beds_dupla = amb.mean_by_management(data_management, "D", "LEITOS_EXISTENTES")
mean_beds_sem_gestao = amb.mean_by_management(data_management, "S", "LEITOS_EXISTENTES")

# print("média:", mean_beds_dupla, mean_beds_estadual, mean_beds_municipal, mean_beds_sem_gestao)

# Mediana dos leitos existentes de cada gestão
median_beds_municipal = amb.median_by_management(data_management, "M", "LEITOS_EXISTENTES")
median_beds_estadual = amb.median_by_management(data_management, "E", "LEITOS_EXISTENTES")
median_beds_dupla = amb.median_by_management(data_management, "D", "LEITOS_EXISTENTES")

# Desvio padrão dos leitos existentes de cada gestão
std_beds_municipal = amb.std_by_management(data_management, "M", "LEITOS_EXISTENTES")
std_beds_estadual = amb.std_by_management(data_management, "E", "LEITOS_EXISTENTES")
std_beds_dupla = amb.std_by_management(data_management, "D", "LEITOS_EXISTENTES")

# Quantidade de valores distintos de leitos em cada gestão
unique_beds_municipal = amb.unique_by_management(data_management, "M", "LEITOS_EXISTENTES")
unique_beds_estadual = amb.unique_by_management(data_management, "E", "LEITOS_EXISTENTES")
unique_beds_dupla = amb.unique_by_management(data_management, "D", "LEITOS_EXISTENTES")

# Média dos leitos SUS de cada gestão 
mean_beds_sus_municipal = amb.mean_by_management(data_management, "M", "LEITOS_SUS")
mean_beds_sus_estadual = amb.mean_by_management(data_management, "E", "LEITOS_SUS")
mean_beds_sus_dupla = amb.mean_by_management(data_management, "D", "LEITOS_SUS")
mean_beds_sus_sem_gestao = amb.mean_by_management(data_management, "S", "LEITOS_SUS")
# print("média SUS:", mean_beds_sus_dupla, mean_beds_sus_estadual, mean_beds_sus_municipal)
# Mediana dos leitos SUS existentes de cada gestão
median_beds_sus_municipal = amb.median_by_management(data_management, "M", "LEITOS_SUS")
median_beds_sus_estadual = amb.median_by_management(data_management, "E", "LEITOS_SUS")
median_beds_sus_dupla = amb.median_by_management(data_management, "D", "LEITOS_SUS")
# print("mediana SUS:", median_beds_sus_dupla, median_beds_sus_estadual, median_beds_sus_municipal)

# Desvio padrão dos leitos SUS existentes de cada gestão
std_beds_sus_municipal = amb.std_by_management(data_management, "M", "LEITOS_SUS")
std_beds_sus_estadual = amb.std_by_management(data_management, "E", "LEITOS_SUS")
std_beds_sus_dupla = amb.std_by_management(data_management, "D", "LEITOS_SUS")
# print("Desvio padrão SUS:", std_beds_sus_dupla, std_beds_sus_estadual, std_beds_sus_municipal)

# Quantidade de valores distintos de leitos SUS em cada gestão
unique_beds_sus_municipal = amb.unique_by_management(data_management, "M", "LEITOS_SUS")
unique_beds_sus_estadual = amb.unique_by_management(data_management, "E", "LEITOS_SUS")
unique_beds_sus_dupla = amb.unique_by_management(data_management, "D", "LEITOS_SUS")
# print("Valores únicos SUS:", unique_beds_sus_dupla, unique_beds_sus_estadual, unique_beds_sus_municipal)

# Gerando o gráfico de barras 
data_management = gbm.replacement(data_management, "TP_GESTAO", "D", "Dupla")
data_management = gbm.replacement(data_management, "TP_GESTAO", "M", "Municipal")
data_management = gbm.replacement(data_management, "TP_GESTAO", "E", "Estadual")
# graph_bar_management = gbm.graph_bar(data_management, "TP_GESTAO", "LEITOS_SUS", 
#                                      title ="Leitos existentes por tipo de gestão (Julho de 2019)", y_label = "Tipo de gestão atuante",
#                                      x_label = "Quantidade de leitos SUS", image_graph_name = "graph_management_horizontal")
'''

"""
### DADOS DA ANÁLISE "LEITOS PEDIÁTRICOS EXISTENTES X REGIÃO BRASILEIRA" ###

#importanto os dados
data_pediatric_regions = dfg.data_ped

#fazendo uma análise de estatística descritiva a partir desses dados
analysis_pediatric_regions_text = apr.calcular_estatisticas(data_pediatric_regions)

#mostrando os dados graficamente no formato de barras
graph_bar_pediatric_region_image = gbpr.plot_bar_chart_from_tuples(data_pediatric_regions[0],data_pediatric_regions[1])
"""