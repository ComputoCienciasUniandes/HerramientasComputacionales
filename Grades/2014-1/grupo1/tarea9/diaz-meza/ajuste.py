import numpy as np
import matplotlib as plt
import sys
import math
import pylab

archivo=sys.argv[1]

data=np.loadtxt(archivo)

dist=data[:,4]
step=data[:,3]


fit= pylab.polyfit(dist, step, 1)
pylab.plot(dist, dist*fit[0] + fit[1], linewidth='2.0', label=str(fit[0])+'x+'+'('+str(fit[1])+')')
pylab.scatter(dist, step)
pylab.legend(loc='best')
pylab.xlabel("$Number of Steps$", fontsize=10)
pylab.ylabel("$Distance to the Center$", fontsize=10)
pylab.title("Number of Steps vs. Distance to the Center (With Regresion)", fontsize=15)
pylab.savefig('ajuste.png')
