# Função para filtrar apenas as colunas necessárias para a análise e visualização
def select_columns(df, columns):
    selected_columns = df[columns]
    return selected_columns

# Função para resetar o index do dataframe
def reset_index(df):
    df.reset_index(inplace = True)
    return df

# Função para excluir colunas desnecessárias do dataframe
def not_necessary_columns(df, columns):
    df.drop(columns, axis = 1, inplace = True)
    return df