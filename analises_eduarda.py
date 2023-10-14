import numpy as np
import matplotlib.pyplot as plt

def calculate_statistics(df, y_column):
    """
    Calcula a média, mediana, desvio padrão, valor máximo e valor mínimo de uma coluna em um DataFrame.

    :param df: DataFrame contendo os dados.
    :type df: pandas.DataFrame
    :param y_column: Nome da coluna para análise.
    :type y_column: str

    :return: Dicionário contendo as estatísticas calculadas.
    :rtype: dict
    """
    try:
        # Verifica se a coluna fornecida existe no DataFrame
        assert y_column in df.columns, f"A coluna {y_column} não existe no DataFrame."
    except AssertionError as e:
        print(e)
        return
    
    # Calcula as estatísticas
    statistics = {
        'Média': np.mean(df[y_column]),
        'Mediana': np.median(df[y_column]),
        'Desvio Padrão': np.std(df[y_column]),
        'Máximo': np.max(df[y_column]),
        'Mínimo': np.min(df[y_column])
    }
    
    return statistics

def plot_statistics(statistics):
    """
    Plota as estatísticas calculadas.

    :param statistics: Dicionário contendo as estatísticas.
    :type statistics: dict

    :return: None
    :rtype: None
    """
    labels = statistics.keys()
    values = statistics.values()

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='skyblue')
    plt.title('Estatísticas dos Leitos Pediátricos por Região')
    plt.xlabel('Estatística')
    plt.ylabel('Valor')
    plt.show()

# Teste das funções
statistics = calculate_statistics(data, 'UTI_PEDIATRICO_EXIST')
plot_statistics(statistics)

data_ped = data.groupby("REGIAO")["UTI_PEDIATRICO_EXIST"].sum()
# Teste do exemplo de uso
graph_bar(data_ped, 'REGIAO', 'UTI_PEDIATRICO_EXIST', 'TOTAL DE LEITOS PEDIÁTRICOS DE UTI POR REGIÃO', 'Região', 'Total de leitos pediátricos', 'uti_pediatrico_por_regiao.png')

