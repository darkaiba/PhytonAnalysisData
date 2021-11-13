# Exercício 1
# Crie um array NumPy com 1000000 e uma lista com 1000000.
# Multiplique cada elemento do array e da lista por 2 e calcule o tempo de execução com cada um dos objetos (use %time).
# Qual objeto oferece melhor performance, array NumPy ou lista?
import numpy as np
my_arr = np.arange(1000000)
my_list = list(range(1000000))

time = []
for y in range(10):
    time.append(my_arr * 2)
print(time)
for y in range(10):
    my_list2 = [x * 2 for x in my_list]
print(my_list2)

# Exercício 2
# Crie um array de 10 elementos
# Altere o valores de todos os elementos dos índices 5 a 8 para 0
import numpy as np
arr = np.arange(10)
print(arr)
arr[5:8] = 0
print(arr)

#Exercicio 3
# Crie um array de 3 dimensões e imprima a dimensão 1
import numpy as np
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[0])

#Exercicio 4
# Crie um array de duas dimensões (matriz).
# Imprima os elementos da terceira linha da matriz
# Imprima todos os elementos da primeira e segunda linhas e segunda e terceira colunas
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
# Imprima os elementos da terceira linha da matriz
print(arr2d[2])
# Imprima todos os elementos da primeira e segunda linhas e segunda e terceira colunas
print(arr2d[:2, 1:])

#Exercicio 5
# Calcule a transposta da matriz abaixo
arr = np.arange(15).reshape((3, 5))
print(arr)
print(arr.T)

#Exercicio 6
# Considere os 3 arrays abaixo
# Retorne o valor do array xarr se o valor for True no array cond. Caso contrário, retorne o valor do array yarr.
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

for x, y, c in zip(xarr, yarr, cond):
    print(x, y, c)

resultado = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print(resultado)

#Exercicio 7
# Crie um array A com 10 elementos e salve o array em disco com a extensão npy
# Depois carregue o array do disco no array B
A = np.arange(10)
print(A)
np.save('array_a', A)
B = np.load('array_a.npy')
print(B)

#Exercicio 8
# Considerando a série abaixo, imprima os valores únicos na série
import pandas as pd
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'a', 'b'])
uniques = obj.unique()
print(uniques)

#Exercicio 9
# Considerando o trecho de código que conecta em uma url na internet, imprima o dataframe conforme abaixo.
import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
print(resp)

data = resp.json()
data[0]['title']
issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
print(issues)

#Exercicio 10
# Crie um banco de dados no SQLite, crie uma tabela, insira registros,
# consulte a tabela e retorne os dados em dataframe do Pandas
import sqlite3
import pandas as pd
query = """
CREATE TABLE TESTE
(Cidade VARCHAR(20), 
 Estado VARCHAR(20),
 taxa REAL,        
 Impostos INTEGER
);"""
con = sqlite3.connect('dsa.db')
con.execute(query)
con.commit()

data = [('Natal', 'Rio Grande do Norte', 1.25, 6),
        ('Recife', 'Pernambuco', 2.6, 3),
        ('Londrina', 'Paraná', 1.7, 5)]
stmt = "INSERT INTO TESTE VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)
con.commit()

cursor = con.execute('select * from teste')
rows = cursor.fetchall()
print(rows)

cursor.description
pd.DataFrame(rows, columns=[x[0] for x in cursor.description])
