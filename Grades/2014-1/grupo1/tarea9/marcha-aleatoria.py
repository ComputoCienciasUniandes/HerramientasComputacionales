import sys
import numpy as np
import pylab

docgraph = sys.argv[1]

tabla = np.loadtxt(docgraph)

Npasos = tabla[:,3]
r = tabla[:,4]

pylab.scatter(Npasos, r)
pylab.xlabel("Numero de pasos", fontsize=20)
pylab.ylabel("Distancia al centro", fontsize=20)
pylab.title("Numero de pasos vs. la distancia recorrida por la particula", fontsize=16)
pylab.savefig('Npasos-r.png')

pylab.show()



