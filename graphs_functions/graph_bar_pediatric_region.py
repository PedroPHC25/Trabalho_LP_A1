"""Módulo do gráfico de barras "Total de leitos pediátricos X Região do Brasil"

Este módulo contém a função que gera o gráfico de barras da quantidade total de leitos pediátricos por região 
do Brasil."""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
# from df_generator import data_ped

def plot_bar_chart_from_tuples(labels, values, color='pink'):
    """
    Cria um gráfico de barras a partir de tuplas de rótulos e valores.

    :param labels: Os rótulos do eixo x.
    :type labels: list
    :param values: Os valores correspondentes no eixo y.
    :type values: list
    :param color: A cor das barras (opcional, padrão é 'pink').
    :type color: str
    :raises ValueError: Se as listas de rótulos e valores tiverem tamanhos diferentes.
    """
    if len(labels) != len(values):
        raise ValueError("As listas de rótulos e valores devem ter o mesmo tamanho.")
    
    # Convertendo todos os valores para inteiros
    values = [int(value) for value in values]
    
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color=color)
    plt.title('Quantidade de leitos pediátricos existentes X Região brasileira')
    plt.xlabel('Região')
    plt.ylabel('Quantidade de leitos')
    plt.xticks(rotation=45)
   

if __name__ == "__main__":
    # Exemplo de uso
    data_ped = (['CENTRO-OESTE', 'NORDESTE', 'NORTE', 'SUDESTE', 'SUL'], [30450, 55476, 22550, 150046, 35870])
    plot_bar_chart_from_tuples(data_ped[0], data_ped[1])
    plt.show()


def test_plot_bar_chart_from_tuples():
    """
    Testa a função plot_bar_chart_from_tuples.
    """
    labels = ['A', 'B', 'C']
    values = [10, 20, 30]

    # Verifica se a função não lança exceções
    plot_bar_chart_from_tuples(labels, values)

    # Verifica se a função aceita uma cor personalizada
    plot_bar_chart_from_tuples(labels, values, color='green')

    # Verifica se a função aceita listas vazias
    plot_bar_chart_from_tuples([], [])

    # Verifica se a função aceita uma única barra
    plot_bar_chart_from_tuples(['A'], [10])

    # Verifica se a função aceita rótulos e valores de tipos diferentes (int e str)
    plot_bar_chart_from_tuples(['A', 'B', 'C'], [10, '20', 30])

def test_exceptions():
    """
    Testa se a função lança exceções corretamente.
    """
    labels = ['A', 'B', 'C']
    values = [10, 20]
    
    try:
        plot_bar_chart_from_tuples(labels, values)
    except ValueError as e:
        assert str(e) == "As listas de rótulos e valores devem ter o mesmo tamanho."

if __name__ == "__main__":
    test_plot_bar_chart_from_tuples()
    test_exceptions()
    print("Todos os testes passaram.")

