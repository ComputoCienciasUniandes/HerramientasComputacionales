import numpy as np
import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
import sys

datos = np.loadtxt(sys.argv[1], delimiter = ' ')
x, y, z = datos[0:, 0], datos[0:, 1], datos[0:, 2]

fig = plt.figure()
ax  = fig.add_subplot(111, projection = '3d')

ax.plot(x, y, z, color = 'b')


ax.scatter(x, y, z, color = 'g')

plt.title('Movimiento de la particula dentro de la esfera')
plt.xlabel('x')
plt.ylabel('y')


f = file('3dplot.png', 'w')
plt.savefig('3dplot.png')
