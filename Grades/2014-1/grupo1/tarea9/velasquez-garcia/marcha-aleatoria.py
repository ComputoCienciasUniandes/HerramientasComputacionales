import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt ('marcha-aleatoria.dat')
R = data[:,4]
N = data[:,3]
plt.scatter(N,R)
plt.title("$Radio\ vs\ cantidad\ de\ movimientos$")
plt.xlabel("$Numero\ de\ movimientos$")
plt.ylabel("$Distancia\ del\ nucleo$")
plt.savefig("Npasos-r.png")
