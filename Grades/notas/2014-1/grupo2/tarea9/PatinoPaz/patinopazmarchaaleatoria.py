import numpy as np
import matplotlib.pyplot as plt
import sys

ruta = str(sys.argv[1])
datos = np.loadtxt(ruta)

pasos = datos[:,0]
distancia = datos[:,4]



plt.scatter(pasos, distancia)
plt.xlabel("Numero de pasos", fontsize=15)
plt.ylabel("Distancia recorrida", fontsize=15)
plt.title("Grafica Random Walk", fontsize=30)
plt.savefig("Npasos-r.png")
