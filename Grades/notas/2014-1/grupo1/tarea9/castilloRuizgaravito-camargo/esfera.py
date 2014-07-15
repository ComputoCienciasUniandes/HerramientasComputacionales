import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]

a=np.cos(u)*np.sin(v)
b=np.sin(u)*np.sin(v)
c=np.cos(v)

ax.plot_wireframe(a, b, c, color="k")

R = np.random.random(100)
S = np.random.random(100)
T = np.random.random(100)
ax.plot(R,S,T,'or')



plt.show()
