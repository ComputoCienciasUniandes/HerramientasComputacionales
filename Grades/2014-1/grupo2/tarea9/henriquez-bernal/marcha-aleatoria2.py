import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt ('marcha-aleatoria.dat')
R = data[:,4]
N = data[:,3]
plt.scatter(N,R)
plt.title("Distancia\ del\ nucleo\ vs\ numero\ de\ pasos$")
plt.xlabel("$Numero\ de\ pasos$")
plt.ylabel("$Distancia\ del\ nucleo$")
plt.show()
plt.savefig("Npasos-r.png")
