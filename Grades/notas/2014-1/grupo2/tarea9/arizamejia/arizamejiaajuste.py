import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.optimize import curve_fit

datos = np.loadtxt( sys.argv[1], delimiter = ' ')
x, y, z, Npasos, r = datos[0:,0], datos[0:,1], datos[0:,2], datos[0:,3], datos[0:,4]

plt.scatter(Npasos, r)
plt.title( 'Numero pasos vs. distancia' )
plt.xlabel( 'Numero pasos' )
plt.ylabel( 'Distancia' )

fitpars = np.polyfit(Npasos,r,15)
plt.plot(Npasos,np.polyval(fitpars,Npasos),'r-')

f = file("ajuste.png", "w")
plt.savefig( 'ajuste.png' )
