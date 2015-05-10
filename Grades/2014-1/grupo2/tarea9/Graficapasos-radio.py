import numpy as np
import math as mt
import sys
import matplotlib.pyplot as plt



archivo = str(sys.argv[1])
datos = np.loadtxt(archivo)

pos1 = datos[:,0]
pos2 = datos[:,4]



plt.figure(figsize=(9, 9))
plt.scatter(pos1, pos2, c= 'g',s=80)
plt.xlabel("$Numero de pasos$", fontsize=20)
plt.ylabel("$Distancia Recorrida$", fontsize=20) 
plt.title("$\mathrm{Pasos\ VS\ Distancia}$", fontsize=30)
plt.savefig("Npasos-r.png")

