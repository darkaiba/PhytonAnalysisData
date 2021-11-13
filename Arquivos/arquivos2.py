"""
Manipulação de Arquivos
Arquivos TXT
Arquivos CSV
Arquivos JSON
"""
# Importando o módulo os
import os
# Importando o módulo csv
import csv
# Importando o módulo Json
import json
#####################################Manipulando Arquivos TXT###################################
texto = "Cientista de Dados é a profissão que mais tem crescido em todo mundo.\n"
texto = texto + "Esses profissionais precisam se especializar em Programação, Estatística e Machine Learning.\n"
texto += "E claro, em Big Data."
print(texto)
# Criando um arquivo
arquivo = open(os.path.join('arquivos/cientista.txt'),'w')
# Gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra+' ')
# Fechando o arquivo
arquivo.close()
# Lendo o arquivo
arquivo = open('arquivos/cientista.txt','r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)
#####################################Usando a expressão with###################################
with open('arquivos/cientista.txt','r') as arquivo:
    conteudo = arquivo.read()
print(len(conteudo))
print(conteudo)
with open('arquivos/cientista.txt','w') as arquivo:
    arquivo.write(texto[:21])
    arquivo.write('\n')
    arquivo.write(texto[:33])

# Lendo o arquivo
arquivo = open('arquivos/cientista.txt','r')
conteudo = arquivo.read()
arquivo.close()

print (conteudo)

#####################################Manipulando Arquivos CSV (comma-separated values )###################################
with open('arquivos/numeros.csv','w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('primeira','segunda','terceira'))
    writer.writerow((55,93,76))
    writer.writerow((62,14,86))

# Leitura de arquivos csv
with open('arquivos/numeros.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print ('Número de colunas:', len(x))
        print(x)
# Código alternativo para eventuais problemas com linhas em branco no arquivo
with open('arquivos/numeros.csv','r', encoding='utf8', newline = '\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print ('Número de colunas:', len(x))
        print(x)

# Código alternativo para eventuais problemas com linhas em branco no arquivo
with open('arquivos/numeros.csv','r', encoding='utf8', newline = '\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print ('Número de colunas:', len(x))
        print(x)

#####################################Manipulando Arquivos JSON (Java Script Object Notation )###################################
# Criando um dicionário
dict = {'nome': 'Guido van Rossum',
        'linguagem': 'Python',
        'similar': ['c','Modula-3','lisp'],
        'users': 1000000}

for k,v in dict.items():
    print (k,v)

# Convertendo o dicionário para um objeto json
json.dumps(dict)
# Criando um arquivo Json
with open('arquivos/dados.json','w') as arquivo:
    arquivo.write(json.dumps(dict))
# Leitura de arquivos Json
with open('arquivos/dados.json','r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)
print (data)
print (data['nome'])
# Imprimindo um arquivo Json copiado da internet
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response)[0]
print ('Título: ', data['title'])
print ('URL: ', data['url'])
print ('Duração: ', data['duration'])
print ('Número de Visualizações: ', data['stats_number_of_plays'])

# Copiando o conteúdo de um arquivo para outro
import os
arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/json_data.txt'

# Método 1
with open(arquivo_fonte,'r') as infile:
    text = infile.read()
    with open(arquivo_destino,'w') as outfile:
        outfile.write(text)
# Método 2
open(arquivo_destino,'w').write(open(arquivo_fonte,'r').read())
# Leitura de arquivos Json
with open('arquivos/json_data.txt','r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)
print(data)
