import numpy as np
import sys
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D

arc=sys.argv[1]
R=float(sys.argv[2])

data = np.loadtxt(arc)
x=data[:,0]
y=data[:,1]
z=data[:,2]

fig=pl.figure()
ax =fig.add_subplot(111, projection= "3d")
u=np.linspace(0,2*np.pi,100)
v=np.linspace(0,np.pi,100)
xi=R*np.outer(np.cos(u), np.sin(v))
yi=R*np.outer(np.sin(u), np.sin(v))
zi=R*np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(xi,yi,zi,reside=4,alpha=0.1,cstride=4)

ay=fig.gca(projection="3d")
ay.plot(x,y,z)
ay.legend()
ay.set_title("Particula en un sol")

pl.savefig("3D")
