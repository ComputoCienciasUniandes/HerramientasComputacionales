import sys 
import numpy as np
import pylab

a = sys.argv[1]

data = np.loadtxt(a)

xp = data[:,3]
yr = data[:,4]

fit =  pylab.polyfit(xp, yr, 1)

pylab.plot(xp, xp*fit[0] + fit[1], linewidth='2.0', label="y="+str(fit[0])+"x+"+"("+str(fit[1])+")")
pylab.scatter(xp, yr, c='k', alpha=0.7)
pylab.legend(loc='best')
pylab.xlabel("NUmero de Pasos", fontsize=20)
pylab.ylabel("Distancia", fontsize=20)
pylab.title("Grafica de Regresion", fontsize=25)
pylab.savefig('ajuste.png')

pylab.show()
