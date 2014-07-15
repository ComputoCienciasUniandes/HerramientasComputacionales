import numpy as np
import matplotlib as plt
import pylab as pl
import sys

archivo=sys.argv[1]
data=np.loadtxt(archivo)

x=data[:,3]
y=data[:,4]

pl.scatter(x, y)
pl.legend(loc='best')
pl.xlabel("$\mathrm{Numero\ Pasos}$", fontsize=25)
pl.ylabel("$\mathrm{Radios}$", fontsize=25)
pl.title("$\mathrm{Recorrido\ Foton}$", fontsize=25)
pl.savefig('Npasos-r.png')
 
pl.show()
