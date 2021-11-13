####################################LENDO ARQUIVOS##########################
# Abrindo o arquivo para leitura
arq1 = open("arquivos/arquivo1.txt", "r")
# Lendo o arquivo
print(arq1.read())
# Contar o número de caracteres
print(arq1.tell())
# Retornar para o iníco do arquivo
print(arq1.seek(0,0))
# Ler os primeiros 10 caracteres
print(arq1.read(10))

##################################GRAVANDO ARQUIVOS##########################
# Abrindo arquivo para gravação
arq2 = open("arquivos/arquivo1.txt", "w")
# Gravando arquivo
arq2.write("Testando gravação de arquivos em Python ")
arq2.close()
# Lendo arquivo gravado
arq2 = open("arquivos/arquivo1.txt", "r")
print(arq2.read())
# Acrescentando conteúdo
arq2 = open("arquivos/arquivo1.txt", "a")
arq2.write(" Acrescentando conteúdo")
arq2.close()
arq2 = open("arquivos/arquivo1.txt", "r")
print(arq2.read())
# Retornando ao início do arquivo para leitura
arq2.seek(0,0)
print(arq2.read())

##################################AUTOMATIZANDO O PROCESSO DE GRAVAÇÃO##########################
fileName = input("Digite o nome do arquivo: ")
fileName = fileName + ".txt"
arq3 = open(fileName, "w")
arq3.write("Incluindo texto no arquivo criado")
arq3.close()
arq3 = open(fileName, "r")
print(arq3.read())
arq3.close()

##################################ABRINDO DATASET EM UMA ÚNICA LINHA##########################
#Faça download do arquivo salarios.csv em nosso repositório no github. Este arquivo foi obtido no site de dados abertos do governo da cidade de Chicago, nos EUA: https://data.cityofchicago.org/
f = open('arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows)

##################################DIVIDINDO DATASET EM COLUNAS ##########################
f = open('arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
print(full_data)

##################################CONTANDO AS LINHAS EM UM ARQUIVO ##########################
f = open('arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
count = 0
for row in full_data:
    count += 1   # Equivalente a: count = count + 1
print(count)

##################################Contando o número de colunas de um arquivo ##########################
f = open('arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    first_row = full_data[0]
count = 0

for column in first_row:
    count = count + 1

# Outra solução possível
# for column in full_data[0]:
#     count = count + 1

print(count)

##################################Importando um dataset com Panda ##########################
import pandas as pd
file_name = "arquivos/binary.csv"
df = pd.read_csv(file_name)
df.head()
file2 = "arquivos/salarios.csv"
df2 = pd.read_csv(file2)
df2.head()
