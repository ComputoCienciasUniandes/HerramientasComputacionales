import numpy as np 
import math as mt
import sys 
import matplotlib.pyplot as plt

if(len(sys.argv)!=2):
    print "debe ingresar un argumento"
    exit(1)
nombre=str(sys.argv[1])
print nombre
data=np.loadtxt(nombre)


pasos= data[:,3]
radio= data[:,5]

plt.scatter(pasos,radio)
plt.savefig("npasos-r.png")
