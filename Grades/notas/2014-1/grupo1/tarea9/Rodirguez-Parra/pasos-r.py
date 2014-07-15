import sys 
import numpy as np
import pylab

a = sys.argv[1]

data = np.loadtxt(a)

xp = data[:,3]
yr = data[:,4]

pylab.scatter(xp, yr)
pylab.xlabel("Numero de Pasos", fontsize=20)
pylab.ylabel("Distancia", fontsize=20)
pylab.title("Grafica de Numero de Pasos vs Distancia", fontsize=25)
pylab.savefig('Npasos-r.png')

pylab.show()
