import sys 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pylab

a = sys.argv[1]

data = np.loadtxt(a)

X = data[:,0]
Y = data[:,1]
Z = data[:,2]

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b', alpha=0.05)

ay = fig.gca(projection='3d')
ay.plot(X, Y, Z, label='Trayectoria de la Particula')
ay.legend()
ay.set_title("Movimiento de la particula dentro de la Esfera", fontsize=20)

plt.savefig('3dplot.png')

plt.show()
