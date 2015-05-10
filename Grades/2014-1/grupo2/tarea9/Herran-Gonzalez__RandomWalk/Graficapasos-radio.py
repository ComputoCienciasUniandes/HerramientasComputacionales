import numpy as np
import sys
import matplotlib.pyplot as plt

archivo = str(sys.argv[1])
datos = np.loadtxt(archivo)

x = datos[:,0]
y = datos[:,4]

plt.figure(figsize=(9, 9))
plt.scatter(x, y, c= 'g',s=80)
plt.xlabel("$Numero de pasos$", fontsize=20)
plt.ylabel("$Distancia Recorrida$", fontsize=20) 
plt.title("$\mathrm{Pasos\ VS\ Distancia}$", fontsize=30)
plt.savefig("Npasos-r.png")

