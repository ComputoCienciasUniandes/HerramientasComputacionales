import numpy as np
import math as mt
import sys
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


nombre=str(sys.argv[1])
print nombre
data=np.loadtxt(nombre)


pasos= data[:,0]
radio= data[:,4]

fit = np.polyfit(pasos, radio, 5)

print fit

plt.plot(pasos, ((pasos)**5)*fit[0] + (pasos**4)*fit[1]+ (pasos**3)*fit[2]+ (pasos**2)*fit[3]+ pasos*fit[4] , linewidth='2.0', label="Fit")
plt.scatter(pasos,radio, c='k', alpha=0.7)
plt.legend(loc='best')
plt.xlabel("$\mathrm{x}$", fontsize=25)
plt.ylabel("$\mathrm{y}$", fontsize=25)
plt.title("$\mathrm{Linear\ Regresion}$", fontsize=25)
plt.savefig("Ajuste.png")
