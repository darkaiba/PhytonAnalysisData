################################################## ---> Conectando com Twitter
# Importando os módulos Tweepy, Datetime e Json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import json

# Adicione aqui sua Consumer Key
consumer_key = "xxxxxxxxx"
# Adicione aqui sua Consumer Secret 
consumer_secret = "xxxxxxxxx"
# Adicione aqui seu Access Token
access_token = "xxxxxxxxx"
# Adicione aqui seu Access Token Secret
access_token_secret = "xxxxxxxxx"
# Criando as chaves de autenticação
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Criando uma classe para capturar os stream de dados do Twitter e
# armazenar no MongoDB
class MyListener(StreamListener):
    def on_data(self, dados):
        tweet = json.loads(dados)
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        text = tweet["text"]
        obj = {"created_at":created_at,"id_str":id_str,"text":text,}
        tweetind = col.insert_one(obj).inserted_id
        print (obj)
        return True
# Criando o objeto mylistener
mylistener = MyListener()
# Criando o objeto mystream
mystream = Stream(auth, listener = mylistener)

################################################## ---> Conectando com MongoDB
# Importando do PyMongo o módulo MongoClient
from pymongo import MongoClient
# Criando a conexão ao MongoDB
client = MongoClient('localhost', 27017)
# Criando o banco de dados twitterdb
db = client.twitterdb
# Criando a collection "col"
col = db.tweets
# Criando uma lista de palavras chave para buscar nos Tweets
keywords = ['Big Data', 'Python', 'Data Mining', 'Data Science']

################################################## ---> Coleta de Twits
# Iniciando o filtro e gravando os tweets no MongoDB
mystream.filter(track=keywords)

################################################## ---> Consultando Mongo
mystream.disconnect()
# Verificando um documento no collection
col.find_one()

################################################## ---> Análise com Pandas e Scikit-Learn
# criando um dataset com dados retornados do MongoDB
dataset = [{"created_at": item["created_at"], "text": item["text"],} for item in col.find()]

# Importando o módulo Pandas para trabalhar com datasets em Python
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Criando um dataframe a partir do dataset
df = pd.DataFrame(dataset)

# Imprimindo o dataframe
print(df)

# Usando o método CountVectorizer para criar uma matriz de documentos
cv = CountVectorizer()
count_matrix = cv.fit_transform(df.text)

# Contando o número de ocorrências das principais palavras em nosso dataset
word_count = pd.DataFrame(cv.get_feature_names(), columns=["word"])
word_count["count"] = count_matrix.sum(axis=0).tolist()[0]
word_count = word_count.sort_values("count", ascending=False).reset_index(drop=True)
word_count[:50]
