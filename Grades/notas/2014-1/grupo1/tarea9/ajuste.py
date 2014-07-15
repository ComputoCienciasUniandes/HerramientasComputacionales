import sys
import numpy as np
import pylab as pl

tabajust = sys.argv[1]

tabla = np.loadtxt(tabajust)

Npasos = tabla[:, 3]
r = tabla[:, 4]

fit = pl.polyfit(Npasos, r, 1)


pl.plot(Npasos, Npasos*fit[0] + fit[1], linewidth='2.0', label="y="+str(fit[0])+"x+"+"("+str(fit[1])+")")
pl.scatter(Npasos, r, c='k')
pl.legend(loc='best')
pl.xlabel("Numero de pasos", fontsize=20)
pl.ylabel("Distancia al centro", fontsize=20)
pl.title("Distancia al centro de la particula vs. Numero de pasos", fontsize=18)

pl.savefig('ajuste.png')

pl.show()




