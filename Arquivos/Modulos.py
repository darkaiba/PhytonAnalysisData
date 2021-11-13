###############################Módulos e Pacotes###############################
# Importando um módulo em Python
import math
# Verificando todos os métodos disponíveis no módulo
dir(math)
# Usando um dos métodos do módulo math
math.sqrt(25)
# Importando apenas um dos métodos do módulo math
from math import sqrt
import random
import statistics
import os
import sys
# Importando o módulo request do pacote urllib, usado para trazer url's
# para dentro do nosso ambiente Python
import urllib.request

# Usando o método
sqrt(9)
# Imprimindo todos os métodos do módulo math
print(dir(math))
# Help do método sqrt do módulo math
help(sqrt)

random.choice(['Maça', 'Banana', 'Laranja'])
random.sample(range(100), 10)

dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(dados)
statistics.median(dados)

os.getcwd()
print(dir(os))

sys.stdout.write('Teste')
sys.version
print(dir(sys))

# Variável resposta armazena o objeto de conexão à url passada como
# parâmetro
resposta = urllib.request.urlopen('http://python.org')
# Objeto resposta
print(resposta)
# Chamando o método read() do objeto resposta e armazenando o código
# html na variável html
html = resposta.read()
# Imprimindo html
print(html)
