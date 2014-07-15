import sys
import matplotlib.pyplot as plt
import numpy as np
import math
a= sys.argv[1]
data=np.loadtxt(a)

pasos=data[:,3]
radio=data[:,4]
plt.scatter(pasos,radio)
plt.xlabel("$x$", fontsize=30)
plt.ylabel("$y$", fontsize=30)
plt.title("Distancia VS Numero de Pasos", fontsize=30)
plt.savefig("Npasos-r.png")
plt.show()

