import pandas as pd

def clean_data(df):
    """
    Limpa os dados do DataFrame.

    :param df: DataFrame a ser limpo.
    :type df: pandas.DataFrame

    :return: DataFrame limpo.
    :rtype: pandas.DataFrame
    """
    # Remover linhas duplicadas
    df = df.drop_duplicates()

    # Preencher valores ausentes (NaN)
    df = df.fillna(0)  # Substitua 0 pelo valor desejado

    # Renomear colunas (se necessário)
    df = df.rename(columns={'coluna_antiga': 'nova_coluna'})

    return df

# Exemplo de uso
data = pd.DataFrame({
    'coluna1': [1, 2, 3, 4, 5, 6],
    'coluna2': [None, 2, None, 4, None, 6]
})

# Chamando a função para limpar os dados
data_limpo = clean_data(data)
