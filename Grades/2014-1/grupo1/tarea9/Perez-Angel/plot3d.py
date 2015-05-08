from mpl_toolkits.mplot3d import Axes3D
import pylab as py
import numpy as np
import sys

archivo=sys.argv[1]

data=np.loadtxt(archivo)

x=data[:,0]
y=data[:,1]
z=data[:,2]
r=data[:,4]

R = max(r)



fig=py.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z, label="foton")

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = R * np.outer(np.cos(u), np.sin(v))
y = R * np.outer(np.sin(u), np.sin(v))
z = R * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='r', alpha=0.1)
ax.set_title('Recorrido Foton en la Esfera')
ax.set_xlabel('X ')
ax.set_ylabel('Y ')
ax.set_zlabel('Z ')

py.show()
