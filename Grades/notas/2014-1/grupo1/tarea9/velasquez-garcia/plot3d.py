import pylab as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
data = np.loadtxt('marcha-aleatoria.dat')
x = data [:,0]
y = data [:,1]
z = data [:,2]
R = data[9:,4]


u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
X = 10 * np.outer(np.cos(u), np.sin(v))
Y = 10 * np.outer(np.sin(u), np.sin(v))
Z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
fig1 = plt.figure()
cir = fig1.add_subplot(111,projection='3d')
cir.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
fig = plt.figure()
pro = fig.gca(projection='3d')
pro.plot(x,y,z)
plt.savefig("plot3d.png")
