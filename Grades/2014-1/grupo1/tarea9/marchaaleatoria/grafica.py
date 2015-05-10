import sys 
import math
import numpy as np
import matplotlib.pyplot as plt
a=sys.argv[1]
data=np.loadtxt(a)
x=data[:,3]
y=data[:,4]
plt.scatter(x,y)
plt.xlabel("$x$", fontsize=30)
plt.ylabel("$y$", fontsize=30)
plt.title("Distancia VS Numero de Pasos", fontsize=30)
plt.savefig("Npasos-r.png")
plt.show()
