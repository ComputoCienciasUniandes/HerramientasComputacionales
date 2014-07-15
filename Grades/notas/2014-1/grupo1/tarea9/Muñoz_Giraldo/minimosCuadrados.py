import numpy as np
import matplotlib as plt
import sys
import math
import pylab

data=sys.argv[1]

archivo=np.loadtxt(data)

x=archivo[:,4]
y=archivo[:,3]

fit=pylab.polyfit(x,y,2)
pylab.plot(x, fit[0]*x**2 + fit[1]*x + fit[2],label=str(fit[0]) +"*x**2" + str(fit[1])+"*x"+str(fit[2]))
pylab.scatter(x,y)
pylab.legend(loc='best')
pylab.xlabel("$Pasos$", fontsize=35)
pylab.ylabel("$Distancia$", fontsize=35)
pylab.title("$Pasos vs distancia (fit)$")
pylab.savefig("ajuste.png")
pylab.show()
