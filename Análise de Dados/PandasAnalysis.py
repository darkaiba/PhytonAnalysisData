import pandas as pd
from pandas import Series
from pandas import DataFrame
import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mat

# Criando uma série sem especificar os índices
Obj = Series([67, 78, -56, 13])
print(Obj)
print(Obj.values)
print(Obj.index)

# Criando uma série e especificando os índices
Obj2 = Series([67, 78, -56, 13], index = ['a', 'b', 'c', 'd'])
print(Obj2[Obj2 > 3])
print(Obj2['b'])
print('d' in Obj2)

# Criando uma série de dados passando um dicionário como parâmetro
dict = {'Futebol':5200, 'Tenis': 120, 'Natação':698, 'Volleyball':1550}

# Criando uma série a partir de um dicionário
Obj3 = Series(dict)
print(Obj3)

# Criando uma lista
esportes = ['Futebol', 'Tenis', 'Natação', 'Basktetball']

# Criando uma serie e usando uma lista como índice
Obj4 = Series(dict, index=esportes)
print(Obj4)
print(pd.isnull(Obj4))
print(pd.notnull(Obj4))
print(Obj4.isnull())
# Concatenando Series
Obj3 + Obj4

Obj4.name = 'população'
Obj4.index.name = 'esporte'
print(Obj4)

####### ---> DataFrames
data = {'Estado': ['Santa Catarina', 'Paraná', 'Goiás', 'Bahia', 'Minas Gerais'],
        'Ano': [2002, 2003, 2004, 2005, 2006],
        'População': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print(frame)

DataFrame(data, columns = ['Ano', 'Estado', 'População'])
# Criando outro dataframe com os mesmo dados anteriores mas adicionando uma coluna
frame2 = DataFrame(data, columns = ['Ano', 'Estado', 'População', 'Débito'],
                   index = ['um', 'dois', 'três', 'quatro', 'cinco'])
# Imprimindo o Dataframe
print(frame2)

# Imprimindo apenas uma coluna do Dataframe
frame2['Estado']
print(frame2.index)
print(frame2.columns)
print(frame2.values)
print(frame2.dtypes)
print(frame2['Ano'])
print(frame2.Ano)
print(frame2[:2])

######## ----> Pandas + Numpy
# Usando o NumPy para alimentar uma das colunas do dataframe
frame2['Débito'] = np.arange(5.)
print(frame2)
print(frame2.values)
print(frame2.describe())
print(frame2['dois':'quatro'])
print(frame2[frame2['População'] < 5])

####### ---> Localizando Registro
print(frame2.loc['quatro'])
print(frame2.iloc[2])

###### ---> Invertendo Colunas e Indices
# Criando um dicionário
web_stats = {'Dias':[1, 2, 3, 4, 5, 6, 7],
             'Visitantes':[45, 23, 67, 78, 23, 12, 14],
             'Taxas':[11, 22, 33, 44, 55, 66, 77]}
df = pd.DataFrame(web_stats)
print(df)
print(df.set_index('Dias'))
print(df.head())
print(df['Visitantes'])
print(df[['Visitantes', 'Taxas']])

######### ---> Dataframes e Arquivos Csv
df = pd.read_csv('salarios.csv')
print(df)
df = pd.read_table('salarios.csv', sep = ',')
print(df)
df = pd.read_csv('salarios.csv', names = ['a', 'b', 'c', 'd'])
print(df)

data = pd.read_csv('salarios.csv')
data.to_csv(sys.stdout, sep = '|')

# Criando um Dataframe
dates = pd.date_range('20180101', periods = 10)
df = pd.DataFrame(np.random.randn(10,4), index = dates, columns = list('ABCD'))
print(df)
print(df.head())
print(df.describe())
print(df.mean())
print(df.mean(1))
print(df.apply(np.cumsum))
# Merge de Dataframes
left = pd.DataFrame({'chave': ['chave1', 'chave2'], 'coluna1': [1, 2]})
right = pd.DataFrame({'chave': ['chave1', 'chave2'], 'coluna2': [4, 5]})
pd.merge(left, right, on='chave')

# Adicionando um elemento ao Dataframe
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print(df)
s = df.iloc[3]
# Adicionando um elemento ao Dataframe
df.append(s, ignore_index=True)
#### ---> Time Series
# Criando um range de datas com frequência de segundos
rng = pd.date_range('1/1/2020', periods = 50, freq = 'S')

ts = pd.Series(np.random.randint(0, 500, len(rng)), index = rng)
print(ts)

# Criando um range de datas com frequência de meses
rng = pd.date_range('1/1/2020', periods = 5, freq = 'M')
ts = pd.Series(np.random.randn(len(rng)), index = rng)
print(ts)

####### ---> Plotting
# Time Series Plot
ts = pd.Series(np.random.randn(500), index=pd.date_range('1/1/2020', periods = 500))
ts = ts.cumsum()
ts.plot()


# DataFrame Plot
df = pd.DataFrame(np.random.randn(500, 4), index = ts.index, columns = ['A', 'B', 'C', 'D'])
df = df.cumsum()
plt.figure(); df.plot(); plt.legend(loc = 'best')

######## ----> Outuput
# Gerando um arquivo excel a partir de um Dataframe
df.to_excel('teste-df-output.xlsx', sheet_name='Sheet1')
# Lendo o arquivo excel para um Dataframe
newDf2 = pd.read_excel('teste-df-output.xlsx', 'Sheet1', index_col = None, na_values = ['NA'])
print(newDf2.head())

os.remove('teste-df-output.xlsx')
