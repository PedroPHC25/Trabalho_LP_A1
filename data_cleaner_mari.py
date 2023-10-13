# Deleta uma coluna com um valor só para todas as células
def del_unic_val(df):
    for column in df:
        unic = df[column].unique()
        if len(unic) == 1:
            df.drop(column, axis = 1, inplace = True)
    return df

# Deleta as colunas não necessárias para a análise
def useless_column(df, useless):
    df.drop(useless, axis = 1, inplace = True)
    return df

# useless = ["NATUREZA_JURIDICA", "NO_LOGRADOURO", "NU_ENDERECO", "NO_COMPLEMENTO", "NO_BAIRRO", "CO_CEP", "NU_TELEFONE", "NO_EMAIL"]

# Identifica e deleta valores atípicos
def treat_outliers(df, column):
    for value in df[column]:
        if value > 9999:
            df.drop(value, axis = 0, inplace = True)
    return df