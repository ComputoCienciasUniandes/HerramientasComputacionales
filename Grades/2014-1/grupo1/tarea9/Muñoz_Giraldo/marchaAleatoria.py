import sys
import random
import math
import numpy as np

R=float(sys.argv[1])

x=0.0
y=0.0
z=0.0

X=0.0
Y=0.0
Z=0.0

a1=0
a2=0

r=0.0
p=0.0

xLista=[]
yLista=[]
zLista=[]
rLista=[]
pasos=[]

def generarA():
    angulo=np.random.random()*2*math.pi
    return angulo

while(R>r):
    a1=generarA()
    a2=generarA()

    x=(math.sin(a1))*(math.cos(a2))
    y=(math.sin(a2))*(math.cos(a2))
    z=(math.cos(a1))
 
    X+=x
    Y+=y
    Z+=z

    p+=1
    r=math.sqrt((math.pow(X,2))+(math.pow(Y,2))+(math.pow(Z,2)))

    pasos.append(p)
    xLista.append(X)
    yLista.append(Y)
    zLista.append(Z)
    rLista.append(r)

archivo=open('marcha-aleatoria.dat','w')

for i in range (len(xLista)):
    archivo.write(str(xLista[i])+" "+str(yLista[i])+" "+str(zLista[i])+" "+str(pasos[i])+" "+str(rLista[i])+"\n")
archivo.close()
