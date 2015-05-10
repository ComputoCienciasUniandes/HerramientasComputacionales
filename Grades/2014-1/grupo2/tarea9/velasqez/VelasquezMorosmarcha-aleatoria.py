import numpy as np
import matplotlib.pyplot as plt
import sys

datos = np.loadtxt(sys.argv[1], delimiter = ' ')

Npasos, r = datos[0:, 3], datos[0:, 4]

plt.scatter(Npasos, r)
plt.title('Numero de pasos vs distancia')
plt.xlabel('Numero de pasos')
plt.ylabel('Distancia del centro')

f = file('Npasos-r.png', 'w')
plt.savefig('Npasos-r.png')

