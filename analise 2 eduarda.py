import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
from df_generator import data
import numpy as np

data_ped = data.groupby("REGIAO")["UTI_PEDIATRICO_EXIST"].sum()
print(data_ped)

# Média
media = data_ped.mean()

# Moda
moda = data_ped.mode()[0]  # A moda pode ter múltiplos valores, pegamos o primeiro

# Mediana
mediana = data_ped.median()

# Desvio Padrão
desvio_padrao = data_ped.std()

# Variância
variancia = data_ped.var()

# Valor Mínimo e Máximo
minimo = data_ped.min()
maximo = data_ped.max()

print(f'Média: {media}')
print(f'Moda: {moda}')
print(f'Mediana: {mediana}')
print(f'Desvio Padrão: {desvio_padrao}')
print(f'Variância: {variancia}')
print(f'Valor Mínimo: {minimo}')
print(f'Valor Máximo: {maximo}')
