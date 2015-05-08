import sys
import numpy as np
import matplotlib as plt
import math

a=sys.argv[1]
data=np.loadtxt(a)

x=data[:,3]
y=data[:,4]

figura=plt.polyfit(x,y,1)
plt.scatter(x,y)
plt.plot(x,y*figura[0]*(y**4) + figura[i]*(y**3), figura[2]*(y**2), figura[3]*y + fit[4])
plt.xlabel("Pasos (x)", frontsize=20)
plt.ylabel("Distancia (y)", frontsize =20)
plt.tittle("Numero de Pasos VS Distancia con la Regresion", frontsize =15)
plt.savefig('ajuste.png')



