import numpy as np
import math as mt
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


nombre=str(sys.argv[1])
print nombre
data=np.loadtxt(nombre)


numdatos = []
x= data[:,1]
y= data[:,2]
z= data[:,3]


 
for i in range(len(data)):    
    numdatos.append(data[i,1])
 
h = len(numdatos)



fig= plt.figure()
ax = Axes3D(fig)
ax.scatter(x,y,z )
plt.savefig("3d.png")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


##Se utiliza para graficar la esfera en la que estan contenido los puntos.
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = np.sqrt((h-1)) * np.outer(np.cos(u), np.sin(v))
y = np.sqrt((h-1)) * np.outer(np.sin(u), np.sin(v))
z = np.sqrt((h-1)) * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='g')
print "La primera de las graficas es la de los puntos en el espacio, mientras que la segunda es la esfera en la que esta contenida vista desde afuera"
plt.show()
