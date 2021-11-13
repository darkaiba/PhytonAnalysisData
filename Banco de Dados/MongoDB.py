########################################################## CREATE ######################################################
#!pip install pymongo
# Importamos o MongoClient para conectar nossa aplicação ao MongoDB
from pymongo import MongoClient
import datetime

# Estabelecemos a conexão ao Banco de Dados
conn = MongoClient('localhost', 27017)

print(type(conn))

# Uma única instância do MongoDB pode suportar diversos bancos de dados.
# Vamos criar o banco de dados cadastrodb
db = conn.cadastrodb
print(type(db))

# Uma coleção é um grupo de documentos armazenados no MongoDB
# (relativamente parecido com o conceito de tabelas em bancos relacionais)
collection = db.cadastrodb

print(type(collection))

post1 = {"codigo": "ID-9987725",
        "prod_name": "Geladeira",
        "marcas": ["brastemp", "consul", "elecrolux"],
        "data_cadastro": datetime.datetime.utcnow()}

print(type(post1))

collection = db.posts
post_id = collection.insert_one(post1)
print(post_id.inserted_id)

# Quando um documento é inserido uma chave especial, "_id", é adicionada
# automaticamente se o documento ainda não contém uma chave "_id".
print(post_id)

post2 = {"codigo": "ID-2209876",
        "prod_name": "Televisor",
        "marcas": ["samsung", "panasonic", "lg"],
        "data_cadastro": datetime.datetime.utcnow()}

collection = db.posts
post_id = collection.insert_one(post2).inserted_id
print(post_id)
collection.find_one({"prod_name": "Televisor"})

# A função find() retorna um cursor e podemos então navegar pelos dados
for post in collection.find():
    print(post)

# Verificando o nome do banco de dados
print(db.name)

# Listando as coleções disponíveis
db.collection_names()

########################################################## DATAS #######################################################
# Importamos o Módulo PyMongo
import pymongo

# Criando a conexão com o MongoDB (neste caso, conexão padrão)
client_con = pymongo.MongoClient()

# Listando os bancos de dados disponíveis
client_con.database_names()

# Definindo o objeto db
db = client_con.cadastrodb

# Listando as coleções disponíveis
db.collection_names()

# Criando uma coleção
db.create_collection("mycollection")

# Listando as coleções disponíveis
db.collection_names()

# Inserindo um documento na coleção criada
db.mycollection.insert_one({
   'titulo': 'MongoDB com Python',
   'descricao': 'MongoDB é um Banco de Dados NoSQL',
   'by': 'Data Science Academy',
   'url': 'http://www.datascienceacademy.com.br',
   'tags': ['mongodb', 'database', 'NoSQL'],
   'likes': 100
})

# Retornando o documento criado
db.mycollection.find_one()

# Preparando um documento
doc1 = {"Nome":"Donald","sobrenome":"Trump","twitter":"@POTUS"}

# Inserindo um documento
db.mycollection.insert_one(doc1)

# Preparando um documento
doc2 = {"Site":"http://www.datascienceacademy.com.br",
        "facebook":"facebook.com/dsacademybr"}

# Inserindo um documento
db.mycollection.insert_one(doc2)

# Retornando os documentos na coleção
for rec in db.mycollection.find():
    print(rec)

# Conectando a uma coleção
col = db["mycollection"]

print(type(col))
print(col.count())

# Encontrando um único documento
redoc = col.find_one()
print(redoc)
