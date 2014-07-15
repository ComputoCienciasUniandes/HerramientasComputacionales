import sys
import numpy as np
import pylab

data=sys.argv[1]

archivo=np.loadtxt(data)

x=archivo[:,4]
y=archivo[:,3]

pylab.scatter(x,y)
pylab.xlabel("$Pasos$", fontsize=35)
pylab.ylabel("$Distancia$", fontsize=35)
pylab.title("Pasos vs Distancia", fontsize=35)
pylab.savefig("nPasos-r.png")
pylab.show()
