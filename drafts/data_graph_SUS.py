"""Módulo de dados para a análise da presença de leitos SUS em janeiro de 2022

Este módulo reúne as manipulações e informações necessárias 
para a geração do gráfico de barras agrupadas, essas informações 
a partir desse módulo ficam explícitas em colunas próprias.

import pandas as pd
import sys
sys.path.append('..\Trabalho_LP_A1')


#Colocar na main ########################
from data_analysis_functions import analysis_functions_SUS as afs
from graphs_functions import graph_bar_SUS as gbs
import df_generator as dfg
from df_generator import data

# importando os dados manipulados para análise
data_SUS = dfg.data_SUS

# Mediana de cada tipo de hospital nos estados brasileiros
median_hosp_pub = afs.median_SUS(data_SUS, "Hospital Público")
median_hosp_priv = afs.median_SUS(data_SUS, "Hospital Privado")
median_hosp_fil = afs.median_SUS(data_SUS, "Hospital Filantrópico")

print("Mediana pub", median_hosp_pub)
print("Mediana priv",median_hosp_priv)
print("Mediana fil", median_hosp_fil)

# Média de cada tipo de hospital nos estados brasileiros
mean_hosp_pub = afs.mean_SUS(data_SUS, "Hospital Público")
mean_hosp_priv = afs.mean_SUS(data_SUS, "Hospital Privado")
mean_hosp_fil = afs.mean_SUS(data_SUS, "Hospital Filantrópico")

print("media pub",mean_hosp_pub)
print("media priv",mean_hosp_priv)
print("media fil",mean_hosp_fil)

# Desvio padrão de cada tipo de hospital nos estados brasileiros
std_hosp_pub = afs.std_SUS(data_SUS, "Hospital Público")
std_hosp_priv = afs.std_SUS(data_SUS, "Hospital Privado")
std_hosp_fil = afs.std_SUS(data_SUS, "Hospital Filantrópico")

print("std pub",std_hosp_pub)
print("std priv",std_hosp_priv)
print("std fil",std_hosp_fil)

# Mínimo e máximo de cada tipo de hospital nos estados brasileiros
min_max_hosp_pub = afs.max_min_SUS(data_SUS, "Hospital Público")
min_max_hosp_priv = afs.max_min_SUS(data_SUS, "Hospital Privado")
min_max_hosp_fil = afs.max_min_SUS(data_SUS, "Hospital Filantrópico")

print("pub",min_max_hosp_pub)
print("priv",min_max_hosp_priv)
print("fil",min_max_hosp_fil)

# Gerando o gráfico de barras agrupadas
graphbar_SUS = gbs.graph_SUS(data_SUS, "Hospital Público", "Hospital Privado", "Hospital Filantrópico")
#####################################################################


# mudar no df generator######################################3
import df_generator_functions as dfgf
useless = ["NATUREZA_JURIDICA", "NO_LOGRADOURO", "NU_ENDERECO", "NO_COMPLEMENTO", "NO_BAIRRO", "CO_CEP", "NU_TELEFONE", "NO_EMAIL"]
data_SUS = dfgf.not_necessary_columns(data, useless)
data_SUS = dfgf.delete_columns_na(data_SUS)
################################################################3

# DUDA 
data_ped = data.groupby("REGIAO")["TOTAL DE LEITOS PEDIÁTRICOS DE UTI POR REGIÃO"].sum()

# Código html, inserir as observações
'''
<h2>Presença de Leitos SUS em Hospitais públicos, privados e filantrópicos</h2>
        <p style="font-size: 12px;">Mariana Fernandes Rocha</p>
        
        <p style="text-align:justify">Nesta análise observaremos a presença de Leitos SUS em hospitais privados, públicos e finatrópicos, as métricas estatísticas exibidas estão de acordo com a distribuição dos leitos nas respectivas naturezas jurídicas pelos estados brasileiros.</p>

        <center>
            <figure class = "html5">
                <img src = "graphs/table_analysis_SUS.png">
                <figcaption style="font-size: 12px;">Tabela 1. Medidas de resumo dos hospitais </figcaption>
            </figure>
        </center>

        <p style="text-align:justify"> <strong>Hospitais filantrópicos</strong>: São instituições privadas, porém sem fins lucrativos, que possuem contrato com o sistema público para prestar atendimento aos pacientes do SUS. Pelo menos 60% dos atendimentos oferecidos pelos hospitais filantrópicos são destinados, obrigatoriamente, ao SUS. As organizações filantrópicas são mantidas com doações de pessoas físicas e de empresas, além de parcerias, convênios e políticas públicas pactuadas com os governos municipais, estaduais e federal.</p>
        <p style="text-align:justify"> <strong>Hospitais públicos</strong>: Todem ser regionais e locais de acordo com a área de abrangência da população a ser assistida, são financiados e mantidos pelo Estado. No Brasil graças à concepção do Sistema Único de Saúde (SUS) é completamente gratuito.</p>
        <p style="text-align:justify"> <strong>Hospitais privados</strong>: Pertencentes a iniciatica privada, essas instituições possuem fins lucrativos. Isso significa que, é preciso o pagamento direto ou ser cliente de um plano de saúde para conseguir atendimento. Apesar de ser um desejo da população, 70% alegam não ter convênio médico, fazendo do SUS a única saída.</p>

        <center>
            <figure class = "html5">
                <img src = "graphs/graph_SUS.png">
                <figcaption style="font-size: 12px;">Gráfico 1. Leitos SUS</figcaption>
            </figure>
        </center>

        <p style="text-align:justify">O Sistema Único de Saúde (SUS) foi uma grande conquista da população brasileira, sendo reconhecido como um dos maiores do mundo e usado como modelo em muitos outros países.
        Entretanto, a saúde pública no Brasil sofre desafios do mau gerenciamento e de falta de investimentos financeiros. Como resultado, temos um sistema em colapso, na maioria das vezes insuficiente e com pouca qualidade para atender a população.
        Um alívio para essa sobrecarga na saude pública são os hospitais sem fins lucrativos, há cerca de 2,6 mil instituições filantrópicas no Brasil, de acordo com dados do Cadastro Nacional de Estabelecimentos de Saúde (CNES). Essas entidades, de direito privado e sem fins lucrativos, prestam diversos serviços a 900 municípios brasileiros que não são atendidos por nenhuma esfera governamental na saúde, o que explica o número significativo dessas instituições presentes nos estados com grandes concentrações urbanas, como São Paulo, Minas Gerais e Rio Grande do Sul.</p>
'''
"""
import pandas as pd
import doctest


def formatar_df(df_original: pd.DataFrame, 
                date: int, 
                coluna_group1: str, coluna_group2: str, 
                coluna_num: str) -> pd.DataFrame:
    
    """
    Formatação para extração das informações necesssárias.

    :param df_original: DataFrame original.
    :type df_original: pd.DataFrame

    :param date: Competência das análises, em formato anomês, 202001. 
    :type date: int

    :param coluna_group1: Primeira coluna para o agrupamento.  
    :type date: str

    :param coluna_group2: Segunda coluna para o agrupamento.  
    :type date: str

    :param coluna_group1: Coluna numérica.  
    :type date: str

    :return: Retorna um DataFrame com as colunas formatadas.
    :rtype: pd.DataFrame

    A função deixa explícita as colunas com as informações 
    para análise e plotagem do gráfico.

    .. warning::
       O paramêtro date precisa estar no formato 202001, anomês.
    
    
    >>> data = {'Data': [202301, 202301, 202301, 202301, 202301, 202301],'Estado': ['SP', 'RJ', 'SP', 'RJ','SP', 'RJ'], 'Tipo_Hospital': ['HOSPITAL_FILANTROPICO', 'HOSPITAL_FILANTROPICO', 'HOSPITAL_PRIVADO', 'HOSPITAL_PRIVADO','HOSPITAL_PUBLICO', 'HOSPITAL_PUBLICO'], 'Valor': [100, 200, 150, 50, 202, 154],"Nome" : ["Hospital Santa Esperança", "Instituto Médico Vital", "Centro Hospitalar Estrela da Manhã", "Hospital São Lucas", "Clínica Médica da Esperança", "Hospital das Crianças Felizes"]}
    >>> example = pd.DataFrame(data)
    >>> example.set_index(["Data", "Nome"], inplace=True)
    >>> formatar_df(example, 202301, 'Estado', 'Tipo_Hospital', 'Valor')
      Estado  Hospital Filantrópico  Hospital Privado  Hospital Público
    0     SP                    100               150               202
    1     RJ                    200                50               154
    """
    # Seleciona os dados na data requerida
    df_original = df_original.loc[date]
    # Armazena os estados presentes na tabela
    estados = df_original[coluna_group1].unique()
    # Agrupando por duas colunas e somando uma coluna numérica
    df_original = df_original.groupby([coluna_group1, coluna_group2])[coluna_num].sum()
    
    # Criando o novo df com as colunas desejadas
    df_formatado = pd.DataFrame(columns=["Estado", "Hospital Filantrópico", "Hospital Privado", "Hospital Público"])
    # Iterando para adicionar cada estado e suas estatísticas
    for estado in estados:
            try:    
                # Localizando as informações e organizando em colunas
                nova_linha = [estado, 
                            df_original.loc[estado].loc["HOSPITAL_FILANTROPICO"],
                            df_original.loc[estado].loc["HOSPITAL_PRIVADO"],
                            df_original.loc[estado].loc["HOSPITAL_PUBLICO"]]
                # Adicionando a linha criada
                df_formatado.loc[len(df_formatado)] = nova_linha 
            
            # O estado de Roraima não possui a coluna "Hospital Filatrópico"
            except KeyError:
                nova_linha = [estado, 
                            0,
                            df_original.loc[estado].loc["HOSPITAL_PRIVADO"],
                            df_original.loc[estado].loc["HOSPITAL_PUBLICO"]]
                df_formatado.loc[len(df_formatado)] = nova_linha
    return df_formatado

if __name__ == "__main__":
    doctest.testmod(verbose = True)

import pandas as pd

# data = {'Data': [202301, 202301, 202301, 202301, 202301, 202301],'Estado': ['SP', 'RJ', 'SP', 'RJ','SP', 'RJ'],
#         'Tipo_Hospital': ['HOSPITAL_FILANTROPICO', 'HOSPITAL_FILANTROPICO', 'HOSPITAL_PRIVADO', 'HOSPITAL_PRIVADO','HOSPITAL_PUBLICO', 'HOSPITAL_PUBLICO'],
#         'Valor': [100, 200, 150, 50, 202, 154],
#         "Nome" : ["Hospital Santa Esperança", "Instituto Médico Vital", "Centro Hospitalar Estrela da Manhã", "Hospital São Lucas", "Clínica Médica da Esperança", "Hospital das Crianças Felizes"]}
# example = pd.DataFrame(data)
# example.set_index(["Data", "Nome"], inplace=True)

# print(formatar_df(example, 202301, 'Estado', 'Tipo_Hospital', 'Valor'))