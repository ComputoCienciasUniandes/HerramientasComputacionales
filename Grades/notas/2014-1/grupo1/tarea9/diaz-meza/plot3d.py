import numpy as np
import math
import pylab as pl
import sys
from mpl_toolkits.mplot3d import Axes3D


archivo=sys.argv[1]
R=float(sys.argv[2])


data=np.loadtxt(archivo)
X=data[:,0]
Y=data[:,1]
Z=data[:,2]

fig = pl.figure()
ax = fig.add_subplot(111, projection='3d')
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
xi = R * np.outer(np.cos(u), np.sin(v))
yi = R * np.outer(np.sin(u), np.sin(v))
zi = R * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(xi, yi, zi, rstride=4, alpha=0.1,  cstride=4, color='r')

ay = fig.gca(projection='3d')
ay.plot(X, Y, Z)
ay.legend()
ay.set_title('Particle Track in the Sphere')
ay.set_xlabel('x')
ay.set_ylabel('y')
ay.set_zlabel('z')

pl.savefig('3dplot.png') 
