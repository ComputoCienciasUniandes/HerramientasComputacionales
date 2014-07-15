import numpy as np
import sys
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


data =np.loadtxt("datos.dat")



x=data[:,3]
print x
y=data[:,4]
plt.plot(x,y, '-r', c='g',label="Datos")
plt.title("$Grafica\ de\ pasos\ Vs\ distancia$", fontsize=20)
plt.xlabel("$Pasos$", fontsize= 20)
plt.ylabel("$Distancia\ particula$", fontsize=20)
ex=math.e
def expfunc(x, a, b, c ,d, e,f):
    #return a*ex**(x-b)+c
    return a*x**(5)+b*x**(4)+c*x**(3)+d*x**2 +e*x+f
fitpars, covmat = curve_fit(expfunc, x, y)

plt.plot(x, expfunc(x, fitpars[0], fitpars[1], fitpars[2],fitpars[3], fitpars[4], fitpars[5]), 'b-', label="Ajuste")
plt.legend(loc=2)
plt.text(5 , 8, "$Eq=$"+str(fitpars[0])+"$x^5+$"+str(fitpars[1])+"$x^4+$"+"\n"+str(fitpars[2])+"$x^3+$"+str(fitpars[3])+"$x^2 +$"+"\n"+str(fitpars[4])+"$x+$"+str(fitpars[5]), fontsize=10)
plt.show()
plt.savefig("ajustes-r.png")


