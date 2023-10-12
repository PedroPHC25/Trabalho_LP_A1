import pandas as pd

# Função para filtrar apenas as colunas necessárias para a análise e visualização
def select_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    selected_columns = df[columns]
    return selected_columns

# Função para resetar o index do dataframe
def reset_index(df: pd.DataFrame) -> pd.DataFrame:
    df.reset_index(inplace = True)
    return df

# Função para excluir colunas desnecessárias do dataframe
def not_necessary_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    df.drop(columns, axis = 1, inplace = True)
    return df