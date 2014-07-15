import math as mt
import numpy as np
import sys

R = float(sys.argv[1])
x = 0
y = 0
z = 0
r = 0
pasos = 0
Npasos = []
radio = []
puntosX = []
puntosY = []
puntosZ = []

while r<R:
      
     pasos +=1 
     Npasos.append(pasos)

     angulotheta = np.random.rand()
     angulophi = np.random.rand()

     x = x + (mt.cos(2*np.pi*angulotheta))*np.sin(np.pi*angulophi)
     puntosX.append(x)

     y = y + (mt.sin(2*np.pi*angulotheta))*np.sin(np.pi*angulophi)
     puntosY.append(y)

     z = z + mt.cos(np.pi*angulophi)
     puntosZ.append(z)

     r =  mt.sqrt(x**2+y**2+z**2)
     radio.append(r)



f = open ("marcha-aleatoria.dat", "w")
for i in range(len(puntosX)):
    f.write(str(Npasos[i])+ " " + str(puntosX[i])+ " " + str(puntosY[i]) +" "+ str(puntosZ[i]) + " " + str(radio[i]) + "\n")
f.close


 
