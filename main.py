import df_generator as dfg
from data_analysis_functions import analysis_beds_year as aby
from graphs_functions import graph_beds_year as gby


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