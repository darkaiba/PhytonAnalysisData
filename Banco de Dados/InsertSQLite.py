###################################################### SEM VARIAVEIS ###################################################
# Reemove o arquivo com o banco de dados SQLite (caso exista)
import os
os.remove("dsa.db") if os.path.exists("dsa.db") else None

import sqlite3

# Criando uma conexão
conn = sqlite3.connect('dsa.db')

# Criando um cursor
c = conn.cursor()

# Função para criar uma tabela
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
              'prod_name TEXT, valor REAL)')

# Função para inserir uma linha
def data_insert():
    c.execute("INSERT INTO produtos VALUES(10, '2018-05-02 14:32:11', 'Teclado', 90 )")
    conn.commit()
    c.close()
    conn.close()

# Criar tabela
create_table()

# Inserir dados
data_insert()

###################################################### COM VARIAVEIS ###################################################
import sqlite3
import random
import time
import datetime

# Criando uma conexão
conn = sqlite3.connect('dsa.db')

# Criando um cursor
c = conn.cursor()

# Função para criar uma tabela
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, '\
              'prod_name TEXT, valor REAL)')

# Função para inserir uma linha
def data_insert():
    c.execute("INSERT INTO produtos VALUES('2018-05-02 12:34:45', 'Teclado', 130.00 )")
    conn.commit()
    c.close()
    conn.close()

# Usando variáveis para inserir dados
def data_insert_var():
    new_date = datetime.datetime.now()
    new_prod_name = 'Monitor'
    new_valor = random.randrange(50,100)
    c.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?)", (new_date, new_prod_name, new_valor))
    conn.commit()

# Gerando valores e inserindo na tabela
for i in range(10):
    data_insert_var()
    time.sleep(1)

# Encerrando a conexão
c.close()
conn.close()
