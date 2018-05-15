import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#data download
datos=np.genfromtxt("Velocidades.txt", skip_header=1)
Rkm=datos[:,0]
Vkms=datos[:,1]

#parte 1
def planetas(R,MG):
    return np.sqrt((MG)/(R))

popt, covar = curve_fit(planetas, Rkm, Vkms)
V_opt = planetas(Rkm, popt[0])

print V_opt
print "el producto MG es", popt[0]

plt.figure
plt.plot(Rkm,V_opt, c="r")
plt.scatter(Rkm,Vkms)
plt.show()
plt.close()

#parte 2
#conversion de unidades
AU=1.496e8#km
RAU=Rkm/AU
VAUyr=Vkms*((60*60*24*365)/AU)

def planetasG(R,M):
    G= 0.000118
    return np.sqrt((G*M)/(R))

poptG, covarG = curve_fit(planetasG, RAU, VAUyr)
V_optG = planetasG(RAU, poptG[0])

print V_optG
print "La masa del Sol es:", poptG[0], "en unidades de masas terrestres"

plt.figure
plt.plot(RAU,V_optG, c="green")
plt.scatter(RAU,VAUyr)
plt.show()
plt.close()

