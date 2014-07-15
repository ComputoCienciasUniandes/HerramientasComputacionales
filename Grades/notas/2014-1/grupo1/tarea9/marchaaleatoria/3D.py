import math
import random
import sys 
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

a=sys.argv[1]
b=float(sys.argv[2])

data=np.loaaadtxt(a)
x=data[:,0]
y=[:,1]
z=[:,2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b', alpha=0.000005)
o=fig.gca(projection='3d')
o.plot(x,y,z)
o.set_xlabel('x')
o.set_ylabel('y')
o.set_zlabel('z')


plt.savefig('3dplot.png')
plt.show() 
