import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.optimize import curve_fit

datos = np.loadtxt(sys.argv[1], delimiter = ' ')
Npasos, r = datos[0:, 3], datos[0:, 4]

fit = np.polyfit(Npasos, r, 15)
plt.plot(Npasos, np.polyval(fit, Npasos), 'r-')

plt.scatter(Npasos, r)
plt.title('Numero de pasos vs distancia')
plt.xlabel('Numero de pasos')
plt.ylabel('Distancia del centro')



x = "La ecuacion de la curva es: " + str(np.polyval(fit, Npasos)[0])+ " x**15 + " +  str(np.polyval(fit, Npasos)[1])+ " x**14 + " +  str(np.polyval(fit, Npasos)[2])+ " x**13 + " + str(np.polyval(fit, Npasos)[3])+ " x**12 + " + str(np.polyval(fit, Npasos)[4])+ " x**11 "

y = str(np.polyval(fit, Npasos)[5])+ " x**10 + " + str(np.polyval(fit, Npasos)[6])+ " x**9 + " + str(np.polyval(fit, Npasos)[7])+ " x**8 + " + str(np.polyval(fit, Npasos)[8])+ " x**7 + " + str(np.polyval(fit, Npasos)[9])+ " x**6 + " + str(np.polyval(fit, Npasos)[10])+ " x**5 + "

z = str(np.polyval(fit, Npasos)[11])+ " x**4 + " + str(np.polyval(fit, Npasos)[12])+ " x**3 + " + str(np.polyval(fit, Npasos)[13])+ " x**2 + " + str(np.polyval(fit, Npasos)[14])+ " x + " + str(np.polyval(fit, Npasos)[15])

plt.figtext(0.03, 0.15, x, fontsize=7)
plt.figtext(0.03, 0.13, y, fontsize=7)
plt.figtext(0.03, 0.11, z, fontsize=7)


f = file('ajuste.png', 'w')
plt.savefig('ajuste.png')
