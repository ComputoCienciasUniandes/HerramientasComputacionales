import numpy as np
import math as mt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import sys

ruta = str(sys.argv[1])
datos = np.loadtxt(ruta)

fig = plt.figure()
ax = Axes3D(fig)

x = datos[:,1]
y = datos[:,2]
z = datos[:,3]



ax.scatter(x,y,z)
ax.set_xlabel('Posicion en x')
ax.set_ylabel('Posicion en y')
ax.set_zlabel('Posicion en z')
ax.set_xlim((min(x),max(x)))
ax.set_ylim((min(y),max(y)))
ax.set_zlim((min(z),max(z)))
plt.title("Grafica Random Walk", fontsize=30)
plt.savefig("3dplot.png")
