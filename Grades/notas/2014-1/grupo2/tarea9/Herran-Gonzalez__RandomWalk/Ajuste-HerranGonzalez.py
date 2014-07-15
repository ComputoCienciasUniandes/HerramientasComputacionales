import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.optimize import curve_fit as cf

archivo = str(sys.argv[1])
datos = np.loadtxt(archivo)

def func(x,a,b,c):
    return a*x**2+b*x+c


def R2(xexp, xteo):
    EE = sum((xteo-xexp)**2)
    np.mean = sum(xexp)/(len(xexp))
    np.variance = sum((mean-xexp)**2)
    R2 = 1 - EE/variance
    return R2

x2 = datos[:,0]
y2 = datos[:,4]
fit =  cf.polyfit(x2, y2, 2)
yteo  = cf.fit[0]*x**2 + cf.fit[1]*x + cf.fit[2]

plt.plot(x, func(x, cf.fit[0], cf.fit[1],cf.fit[2]), 'r-', label=R2(y2, yteo))
plt.xlabel("Numero de Pasos", fontsize=25)
plt.ylabel("Distancia recorrida", fontsize=25)
plt.title("Regresion(minimos cuadrados)", fontsize=25)
plt.legend(loc="best")
plt.scatter(x2,y2)
plt.savefig("ajuste.png")
