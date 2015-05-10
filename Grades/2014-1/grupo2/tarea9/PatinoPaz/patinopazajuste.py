import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.optimize import curve_fit

ruta = str(sys.argv[1])
datos = np.loadtxt(ruta)

def func(x,a,b,c,d,e,f):
    return a*x**5+b*x**4+c*x**3+d*x**2+e*x+f
def R2(xexp, xteo):
    EE = sum((xteo-xexp)**2)
    np.mean = sum(xexp)/(len(xexp))
    np.variance = sum((mean-xexp)**2)
    R2 = 1 - EE/variance
    return R2

pasos = datos[:,0]
distancia = datos[:,4]
fit =  np.polyfit(pasos,distancia, 5)


plt.plot(pasos, func(pasos, fit[0], fit[1],fit[2], fit[3],fit[4], fit[5]), 'r-', label= "y=a*x**5+b*x**4+c*x**3+d*x**2+e*x+f")
plt.xlabel("Pasos", fontsize=25)
plt.ylabel("Distancia al centro", fontsize=25)
plt.title("Regresion Movimiento", fontsize=25)
plt.legend(loc="best")
plt.scatter(pasos , distancia)
plt.savefig("ajuste.png")
