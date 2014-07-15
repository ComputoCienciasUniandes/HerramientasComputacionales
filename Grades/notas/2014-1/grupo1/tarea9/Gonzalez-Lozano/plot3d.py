import numpy as np 
import math as mt
import sys 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

if(len(sys.argv)!=2):
    print "debe ingresar un argumento"
    exit(1)
nombre=str(sys.argv[1])
print nombre
data=np.loadtxt(nombre)


x= data[:,0]
y= data[:,1]
z= data[:,2]

fig= plt.figure()
ax = Axes3D(fig)
ax.scatter(x,y,z )
plt.savefig("3d.png")
