"""Módulo do gráfico de barras "Total de leitos pediátricos X Região do Brasil"

Este módulo contém a  função que gera o gráfico de barras que permite uma
análise comparativa da quantidade total de leitos pediátricos por região 
do Brasil.
"""
def graph_bar(df, x_column, y_column, title, x_label, y_label, image_graph_name):
    """
    Gera um gráfico de barras a partir de um DataFrame.

    :param df: DataFrame contendo os dados.
    :type df: pandas.DataFrame
    :param x_column: Nome da coluna para o eixo x.
    :type x_column: str
    :param y_column: Nome da coluna para o eixo y.
    :type y_column: str
    :param title: Título do gráfico.
    :type title: str
    :param x_label: Rótulo do eixo x.
    :type x_label: str
    :param y_label: Rótulo do eixo y.
    :type y_label: str
    :param image_graph_name: Nome do arquivo de imagem para salvar.
    :type image_graph_name: str

    :return: None
    :rtype: None

    Gera um gráfico de barras a partir dos dados no DataFrame fornecido. Salva a imagem
    na pasta "graphs" com o nome especificado.

    Exemplo de uso:
    graph_bar(data, 'REGIAO', 'UTI_PEDIATRICO_EXIST',
              'TOTAL DE LEITOS PEDIÁTRICOS DE UTI POR REGIÃO',
              'Região', 'Total de leitos pediátricos',
              'uti_pediatrico_por_regiao.jpg')
    """
    

# Função para plotar um gráfico de barras
def graph_bar(df, x_column, y_column, title, x_label, y_label, image_graph_name):
    # Ajustando o tamanho do gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(df[x_column], df[y_column], color='pink')  

    # Configurando os textos
    plt.title(title, fontsize=16)
    plt.xlabel(x_label, fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.tick_params(axis="x", labelsize=10)
    plt.tick_params(axis="y", labelsize=10)

    # Adicionando ponto como separador de milhar no eixo
    formatter = ticker.FuncFormatter(lambda x, pos: "{:,.0f}".format(x).replace(",", "."))
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.savefig(f"graphs/{image_graph_name}")
    plt.show()

graph_bar(data, 'REGIAO', 'UTI_PEDIATRICO_EXIST', 'TOTAL DE LEITOS PEDIÁTRICOS DE UTI POR REGIÃO', 'Região', 'Total de leitos pediátricos', 'uti_pediatrico_por_regiao.jpg')
