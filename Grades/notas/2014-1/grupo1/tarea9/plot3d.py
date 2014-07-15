import sys
import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D

archtab = sys.argv[1]
tabla = np.loadtxt(archtab)

x = tabla[:,0]
y = tabla[:,1]
z = tabla[:,2]

graph = pl.figure()

circle = graph.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

X = 10 * np.outer(np.cos(u), np.sin(v))
Y = 10 * np.outer(np.sin(u), np.sin(v))
Z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
circle.plot_surface(X, Y, Z,  rstride=4, cstride=4, color='b', alpha=0.1)

grafica = graph.gca(projection='3d')

grafica.plot(x, y, z)
grafica.set_title("Trayectoria de la particula", fontsize=20)

pl.savefig('3dplot.png')

pl.show()


