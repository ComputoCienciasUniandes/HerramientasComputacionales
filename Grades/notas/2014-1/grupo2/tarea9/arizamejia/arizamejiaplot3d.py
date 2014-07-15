import numpy as np
import matplotlib.pyplot as plt
import sys
from mpl_toolkits.mplot3d.axes3d import Axes3D

datos = np.loadtxt( sys.argv[1], delimiter = ' ')
x, y, z, Npasos, r = datos[0:,0], datos[0:,1], datos[0:,2], datos[0:,3], datos[0:,4]

fig = plt.figure(figsize=(14,6))

ax = fig.add_subplot(1, 2, 1, projection='3d')

p = ax.plot_surface(x, y, z, rstride=4, cstride=4, linewidth=0)

ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(x, y, z)
cb = fig.colorbar(p, shrink=0.5)

f = file("3dplot.png", "w")
plt.savefig( '3dplot.png' )
