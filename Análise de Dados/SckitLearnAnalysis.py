# Importando Matplotlib e Numpy
import matplotlib.pyplot as plt
import matplotlib as mat
import numpy as np
import pandas as pd
import scipy.stats as stats
import sklearn
# Importando o módulo de Regressão Linear do scikit-learn
# O dataset boston já está disponível no scikit-learn. Precisamos apenas carregá-lo.
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from IPython.display import Image
Image('ml_map.png')

# Diâmetros (cm)
Diametros = [[7], [10], [15], [30], [45]]

# Preços (R$)
Precos = [[8], [11], [16], [38.5], [52]]

plt.figure()
plt.xlabel('Diâmetro(cm)')
plt.ylabel('Preço(R$)')
plt.title('Diâmetro x Preço')
plt.plot(Diametros, Precos, 'k.')
plt.axis([0, 60, 0, 60])
plt.grid(True)
plt.show()

##### --> Regressão Linear
# Preparando os dados de treino
# Vamos chamar de X os dados de diâmetro da Pizza.
X = [[7], [10], [15], [30], [45]]

# Vamos chamar de Y os dados de preço da Pizza.
Y = [[8], [11], [16], [38.5], [52]]

# Criando o modelo
modelo = LinearRegression()
# Treinando o modelo
modelo.fit(X, Y)
# Prevendo o preço de uma pizza de 20 cm de diâmetro
# Usamos agora esta sintaxe:
print("Uma pizza de 20 cm de diâmetro deve custar: R$%.2f" % modelo.predict([[20]]))

#### --->Construindo um ScatterPlot
# Coeficientes
print('Coeficiente: \n', modelo.coef_)

# MSE (mean square error)
print("MSE: %.2f" % np.mean((modelo.predict(X) - Y) ** 2))

# Score de variação: 1 representa predição perfeita
print('Score de variação: %.2f' % modelo.score(X, Y))

# Scatter Plot representando a regressão linear
plt.scatter(X, Y,  color = 'black')
plt.plot(X, modelo.predict(X), color = 'blue', linewidth = 3)
plt.xlabel('X')
plt.ylabel('Y')
plt.xticks(())
plt.yticks(())

plt.show()

###### ---> Explorando o Dataset Boston Housing
boston = load_boston()
# Visualizando o shape do dataset, neste caso 506 instâncias (linhas) e 13 atributos (colunas)
print(boston.data.shape)
# Descrição do Dataset
print(boston.DESCR)
print(boston.feature_names)

# Convertendo o dataset em um DataFrame pandas
df = pd.DataFrame(boston.data)
print(df.head())

# Convertendo o título das colunas
df.columns = boston.feature_names
print(df.head())

# boston.target é uma array com o preço das casas
print(boston.target)

# Adicionando o preço da casa ao DataFrame
df['PRICE'] = boston.target
print(df.head())

########## ---> Prevendo o Preço das Casas em Boston
# Não queremos o preço da casa como variável dependente
X = df.drop('PRICE', axis = 1)
# Definindo Y
Y = df.PRICE

plt.scatter(df.RM, Y)
plt.xlabel("Média do Número de Quartos por Casa")
plt.ylabel("Preço da Casa")
plt.title("Relação entre Número de Quartos e Preço")
plt.show()

# Criando o objeto de regressão linear
regr = LinearRegression()
# Treinando o modelo
print(regr.fit(X, Y))

# Coeficientes
print("Coeficiente: ", regr.intercept_)
print("Número de Coeficientes: ", len(regr.coef_))

# Prevendo o preço da casa
print(regr.predict(X))

# Comparando preços originais x preços previstos
plt.scatter(df.PRICE, regr.predict(X))
plt.xlabel("Preço Original")
plt.ylabel("Preço Previsto")
plt.title("Preço Original x Preço Previsto")
plt.show()

####### ---> Podemos ver que existem alguns erros na predição do preço das casas
# Vamos calcular o MSE (Mean Squared Error)
mse1 = np.mean((df.PRICE - regr.predict(X)) ** 2)
print(mse1)

# Aplicando regressão linear para apenas uma variável e calculando o MSE
regr = LinearRegression()
regr.fit(X[['PTRATIO']], df.PRICE)
mse2 = np.mean((df.PRICE - regr.predict(X[['PTRATIO']])) ** 2)
print(mse2)

######## ---> O MSE aumentou, indicando que uma única característica não é um bom predictor para o preço das casas
# Dividindo X em dados de treino e de teste
X_treino = X[:-50]
X_teste = X[-50:]

# Dividindo Y em dados de treino e de teste
Y_treino = df.PRICE[:-50]
Y_teste = df.PRICE[-50:]

# Imprimindo o shape dos datasets
print(X_treino.shape, X_teste.shape, Y_treino.shape, Y_teste.shape)

# Dividindo X e Y em dados de treino e de teste
X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, df.PRICE, test_size = 0.33, random_state = 5)
# Imprimindo o shape dos datasets
print(X_treino.shape, X_teste.shape, Y_treino.shape, Y_teste.shape)

# Construindo um modelo de regressão
regr = LinearRegression()

# Treinando o modelo
regr.fit(X_treino, Y_treino)

# Definindo os dados de treino e teste
pred_treino = regr.predict(X_treino)
pred_teste = regr.predict(X_teste)

# Comparando preços originais x preços previstos
plt.scatter(regr.predict(X_treino), regr.predict(X_treino) - Y_treino, c = 'b', s = 40, alpha = 0.5)
plt.scatter(regr.predict(X_teste), regr.predict(X_teste) - Y_teste, c = 'g', s = 40, alpha = 0.5)
plt.hlines(y = 0, xmin = 0, xmax = 50)
plt.ylabel("Resíduo")
plt.title("Residual Plot - Treino(Azul), Teste(Verde)")
plt.show()
