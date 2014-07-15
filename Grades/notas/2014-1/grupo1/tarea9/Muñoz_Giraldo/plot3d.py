import math
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
import pylab
from mpl_toolkits.mplot3d import Axes3D

data=sys.argv[1]

archivo=np.loadtxt(data)

X=archivo[:,0]
Y=archivo[:,1]
Z=archivo[:,2]

fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')

a=np.linspace(0, 2*np.pi, 100)
b=np.linspace(0, np.pi, 100)

x=10*np.outer(np.cos(a), np.sin(b))
y=10*np.outer(np.sin(a), np.sin(b))
z=10*np.outer(np.ones(np.size(a)), np.cos(b))

ax.plot_surface(x, y, z, rstride=4, cstride=4)

ax.plot(X, Y, Z, label='parametric curve')
ax.legend()

pylab.savefig("plot3d.png")
plt.show()
