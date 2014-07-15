import numpy as np
import matplotlib.pyplot as plt
import sys

datos = np.loadtxt( sys.argv[1], delimiter = ' ')
x, y, z, Npasos, r = datos[0:,0], datos[0:,1], datos[0:,2], datos[0:,3], datos[0:,4]

plt.scatter(Npasos, r)
plt.title( 'Numero pasos vs. distancia' )
plt.xlabel( 'Numero pasos' )
plt.ylabel( 'Distancia' )

f = file("Npasos-r.png", "w")
plt.savefig( 'Npasos-r.png' )
