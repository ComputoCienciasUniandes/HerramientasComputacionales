import matplotlib.pyplot as plt
import numpy as np
import sys

data= np.loadtxt(sys.argv[1])

x=data[:,0]
y=data[:,1]
z=data[:,2]
r=data[:,3]
pasos=data[:,4]

plt.scatter(r, pasos)
plt.xlabel("$Distancia$", fontsize=30)
plt.ylabel("$Numero de Pasos$", fontsize=30)
plt.title("Pasos vs. Distancia", fontsize=30)
plt.savefig("grafica.png")
