import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'
dado = np.loadtxt(url,delimiter=',',usecols=np.arange(1,88,1))


dado_transposto = dado.T

precos = dado_transposto[:,1:6]
datas = np.arange(1,88,1)

plt.plot(datas, precos[:,0])

Moscow = precos[:,0]
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]

plt.plot(datas, Moscow)

Kaliningrad[4]=np.mean([Kaliningrad[3],Kaliningrad[5]])
#plt.plot(datas, Kaliningrad)

Y = Moscow
X = datas
n = np.size(Moscow)

a = (n*np.sum(X*Y)-np.sum(X)*np.sum(Y))/(n*np.sum(X**2)-np.sum(X)**2) #coeficiente angular
b = np.mean(Y) - a*np.mean(X) # coeficiente linear
y = a*X+b
z = np.linalg.norm(Moscow-y) #correspondência
plt.plot(X,y)

