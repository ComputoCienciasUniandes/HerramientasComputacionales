import numpy as np 
import matplotlib.pyplot as plt
import sys
puntos= np.loadtxt(sys.argv[1], delimiter= ' ')
Npuntos, r = puntos[0:, 3] , puntos[0:, 4]
plt.scatter(Npuntos, r)
plt.title('Numero de pasos vs distancia')
plt.xlabel('Numero de pasos')
plt.ylabel('Distancia del centro')
f=file('Npuntos-r.png', 'w')
plt.savefig('Npuntos-r.png')
