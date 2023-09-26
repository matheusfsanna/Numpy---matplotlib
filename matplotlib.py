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

plt.plot(datas, Kaliningrad)

plt.plot(datas, Petersburg)

plt.plot(datas, Krasnodar)

plt.plot(datas, Ekaterinburg)