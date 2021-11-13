import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import cm
from pylab import *
from mpl_toolkits.mplot3d.axes3d import Axes3D

# O método plot() define os eixos do gráfico
plt.plot([1, 3, 5], [2, 5, 7])
plt.show()

x = [1, 4, 5]
y = [3, 7, 2]
plt.plot(x, y)
plt.xlabel('Variável 1')
plt.ylabel('Variável 2')
plt.title('Teste Plot')
plt.show()

x2 = [1, 2, 3]
y2 = [11, 12, 15]

plt.plot(x2, y2, label = 'Primeira Linha')
plt.legend()
plt.show()

#### -->Gráficos Barras
x = [2,4,6,8,10]
y = [6,7,8,2,4]
plt.bar(x, y, label = 'Barras', color = 'r')
plt.legend()
plt.show()

x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]
plt.bar(x, y, label = 'Barras1', color = 'r')
plt.bar(x2, y2, label = 'Barras2', color = 'y')
plt.legend()
plt.show()

idades = [22,65,45,55,21,22,34,42,41,4,99,101,120,122,130,111,115,80,75,54,44,64,13,18,48]
ids = [x for x in range(len(idades))]
plt.bar(ids, idades)
plt.show()

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(idades, bins, histtype = 'bar', rwidth = 0.8)
plt.show()

plt.hist(idades, bins, histtype = 'stepfilled', rwidth = 0.8)
plt.show()

##### ---> ScatterPlot
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,5,6,8,4,8]

plt.scatter(x, y, label = 'Pontos', color = 'r', marker = 'o', s = 100)
plt.legend()
plt.show()

######## ---> StackPlots
dias = [1,2,3,4,5]
dormir = [7,8,6,77,7]
comer = [2,3,4,5,3]
trabalhar = [7,8,7,2,2]
passear = [8,5,7,8,13]

plt.stackplot(dias, dormir, comer, trabalhar, passear, colors = ['m','c','r','k','b'])
plt.show()

##### ---> PieChart
fatias = [7, 2, 2, 13]
atividades = ['dormir','comer','trabalhar','passear']
colunas = ['c','m','r','k']

plt.pie(fatias, labels = atividades, colors = colunas, startangle = 90, shadow = True, explode = (0,0.1,0,0))
plt.show()

##### ---> Pylab
x = linspace(0, 5, 10)
y = x ** 2

fig = plt.figure()

# Definindo os eixos
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes.plot(x, y, 'r')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Gráfico de Linha');

# Gráficos com 2 figuras
x = linspace(0, 5, 10)
y = x ** 2

fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # eixos da figura principal
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # eixos da figura secundária

# Figura principal
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('Figura Principal')

# Figura secundária
axes2.plot(y, x, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('Figura Secundária');

# Gráficos em Paralelo
fig, axes = plt.subplots(nrows = 1, ncols = 2)

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Título')

fig.tight_layout()

#### ---> Graficos com Numpy
plt.scatter(np.arange(50), np.random.randn(50))
plt.show()

# Plot e Scatter
fig = plt.figure()

ax1 = fig.add_subplot(1,2,1)
ax1.plot(np.random.randn(50), color='red')

ax2 = fig.add_subplot(1,2,2)
ax2.scatter(np.arange(50), np.random.randn(50))
plt.show()

# Plots diversos
_, ax = plt.subplots(2,3)

ax[0,1].plot(np.random.randn(50), color = 'green', linestyle = '-')
ax[1,0].hist(np.random.randn(50))
ax[1,2].scatter(np.arange(50), np.random.randn(50), color = 'red')
plt.show()

# Controle dos eixos
fig, axes = plt.subplots(1, 3, figsize = (12, 4))

axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("Eixos com range padrão")

axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("Eixos menores")

axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title("Eixos customizados");

# Escala
fig, axes = plt.subplots(1, 2, figsize=(10,4))

axes[0].plot(x, x**2, x, exp(x))
axes[0].set_title("Escala Padrão")

axes[1].plot(x, x**2, x, exp(x))
axes[1].set_yscale("log")
axes[1].set_title("Escala Logaritmica (y)");

# Grid
fig, axes = plt.subplots(1, 2, figsize=(10,3))

# Grid padrão
axes[0].plot(x, x**2, x, x**3, lw = 2)
axes[0].grid(True)

# Grid customizado
axes[1].plot(x, x**2, x, x**3, lw = 2)
axes[1].grid(color = 'b', alpha = 0.5, linestyle = 'dashed', linewidth = 0.5)

# Gráfico de Linhas Gêmeas
fig, ax1 = plt.subplots()

ax1.plot(x, x**2, lw=2, color="blue")
ax1.set_ylabel("Area", fontsize=18, color="blue")
for label in ax1.get_yticklabels():
    label.set_color("blue")

ax2 = ax1.twinx()
ax2.plot(x, x**3, lw=2, color="red")
ax2.set_ylabel("Volume", fontsize=18, color="red")
for label in ax2.get_yticklabels():
    label.set_color("red")

# Diferentes estilos de Plots
xx = np.linspace(-0.75, 1., 100)
n = np.array([0,1,2,3,4,5])

fig, axes = plt.subplots(1, 4, figsize=(12,3))

axes[0].scatter(xx, xx + 0.25*randn(len(xx)))
axes[0].set_title("scatter")

axes[1].step(n, n**2, lw=2)
axes[1].set_title("step")

axes[2].bar(n, n**2, align="center", width=0.5, alpha=0.5)
axes[2].set_title("bar")

axes[3].fill_between(x, x**2, x**3, color="green", alpha=0.5);
axes[3].set_title("fill_between");

# Histogramas
n = np.random.randn(100000)
fig, axes = plt.subplots(1, 2, figsize=(12,4))

axes[0].hist(n)
axes[0].set_title("Histograma Padrão")
axes[0].set_xlim((min(n), max(n)))

axes[1].hist(n, cumulative=True, bins=50)
axes[1].set_title("Histograma Cumulativo")
axes[1].set_xlim((min(n), max(n)));

# Color Map
alpha = 0.7
phi_ext = 2 * np.pi * 0.5

def ColorMap(phi_m, phi_p):
    return ( + alpha - 2 * np.cos(phi_p)*cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p))

phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X,Y = np.meshgrid(phi_p, phi_m)
Z = ColorMap(X, Y).T

fig, ax = plt.subplots()

p = ax.pcolor(X/(2*np.pi), Y/(2*np.pi), Z, cmap=cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max())
cb = fig.colorbar(p, ax=ax)

#### ---> Gráficos 3D
ig = plt.figure(figsize=(14,6))

ax = fig.add_subplot(1, 2, 1, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)

# Wire frame
fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(1, 1, 1, projection = '3d')

p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)

# Countour Plot com projeção
fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
cset = ax.contour(X, Y, Z, zdir='z', offset=-pi, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-pi, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=3*pi, cmap=cm.coolwarm)

ax.set_xlim3d(-pi, 2*pi);
ax.set_ylim3d(0, 3*pi);
ax.set_zlim3d(-pi, 2*pi);
