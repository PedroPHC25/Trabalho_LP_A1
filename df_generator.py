import pandas as pd
import df_generator_functions as dfgf

### CONCATENAÇÃO DOS ARQUIVOS CSV ###

data_2019 = pd.read_csv("dados/Leitos_2019.csv")
data_2020 = pd.read_csv("dados/Leitos_2020.csv")
data_2021 = pd.read_csv("dados/Leitos_2021.csv")
data_2022 = pd.read_csv("dados/Leitos_2022.csv")
data_2023 = pd.read_csv("dados/Leitos_2023.csv", encoding = "unicode_escape", engine = "python", sep = ",")

renaming_columns = {"MOTIVO DESABILITACAO": "MOTIVO_DESABILITACAO",
                  "NOME ESTABELECIMENTO": "NOME_ESTABELECIMENTO",
                  "RAZAO SOCIAL": "RAZAO_SOCIAL",
                  "LEITOS EXISTENTE": "LEITOS_EXISTENTES",
                  "LEITOS SUS": "LEITOS_SUS",
                  "UTI TOTAL - EXIST": "UTI_TOTAL_EXIST",
                  "UTI TOTAL - SUS": "UTI_TOTAL_SUS",
                  "UTI ADULTO - EXIST": "UTI_ADULTO_EXIST",
                  "UTI ADULTO - SUS": "UTI_ADULTO_SUS",
                  "UTI PEDIATRICO - EXIST": "UTI_PEDIATRICO_EXIST",
                  "UTI PEDIATRICO - SUS": "UTI_PEDIATRICO_SUS",
                  "UTI NEONATAL - EXIST": "UTI_NEONATAL_EXIST",
                  "UTI NEONATAL - SUS": "UTI_NEONATAL_SUS",
                  "UTI QUEIMADO - EXIST": "UTI_QUEIMADO_EXIST",
                  "UTI QUEIMADO - SUS": "UTI_QUEIMADO_SUS",
                  "UTI CORONARIANA - EXIST": "UTI_CORONARIANA_EXIST",
                  "UTI CORONARIANA - SUS": "UTI_CORONARIANA_SUS"}

data_2019.rename(columns = renaming_columns, inplace = True)
data_2020.rename(columns = renaming_columns, inplace = True)
data_2021.rename(columns = renaming_columns, inplace = True)
data_2022.rename(columns = renaming_columns, inplace = True)

data = pd.concat([data_2019, data_2020, data_2021, data_2022, data_2023], axis = 0)

data.set_index(["COMP", "CNES"], inplace = True)

### GERAÇÃO DO DATAFRAME PARA A ANÁLISE "BEDS X YEAR" ###

data_beds_year = dfgf.select_columns(data, ["LEITOS_EXISTENTES"])
data_beds_year = dfgf.reset_index(data_beds_year)
data_beds_year = dfgf.not_necessary_columns(data_beds_year, ["CNES"])

### GERAÇÃO DO DATAFRAME PARA ANÁLISE "LEITOS SUS"

useless = ["NATUREZA_JURIDICA", "NO_LOGRADOURO", "NU_ENDERECO", "NO_COMPLEMENTO", "NO_BAIRRO", "CO_CEP", "NU_TELEFONE", "NO_EMAIL"]
data_SUS = dfgf.not_necessary_columns(data, useless)
data_SUS = dfgf.delete_columns_na(data_SUS)
data_SUS = dfgf.formatar_df(data_SUS,202201, "UF", "DESC_NATUREZA_JURIDICA", "LEITOS_SUS")

### GERAÇÃO DO DATAFRAME PARA ANÁLISE "BEDS X MANAGEMENT"

data_management = dfgf.select_columns(data, ["LEITOS_EXISTENTES", "LEITOS_SUS", "TP_GESTAO", "NOME_ESTABELECIMENTO"])
data_management = dfgf.reset_index(data_management)
data_management = dfgf.not_necessary_columns(data_management, ["CNES", "COMP"])

### GERAÇÃO DO DATAFRAME PARA ANÁLISE "LEITOS PEDIÁTRICOS POR REGIÃO"

data_ped = dfgf.generate_bar_chart_data(data, "REGIAO", "UTI_PEDIATRICO_EXIST")
