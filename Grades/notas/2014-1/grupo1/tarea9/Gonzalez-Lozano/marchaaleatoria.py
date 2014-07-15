import numpy as np 
import math as mt
import sys 

if(len(sys.argv)!=2):
    print "debe ingresar un argumento"
    exit(1)
R=float(sys.argv[1])

pi= np.pi
x=0
y=0
z=0
n=0
columnaX=[]
columnaY=[]
columnaZ=[]
columnaPasos=[]
columnar=[]
columnad=[]

r= (x**2+y**2+z**2)**0.5
d=r

while(r<R):    
    n=n+1
    A= np.random.rand()
    B= np.random.rand()
    teta=2*pi*A
    gamma=2*pi*B
    x=x+mt.sin(teta)*mt.sin(gamma)
    y=y+mt.sin(teta)*mt.cos(gamma)
    z=z+mt.cos(teta)
    d= r + (x**2+y**2+z**2)**0.5
    r= (x**2+y**2+z**2)**0.5
    columnaX.append(x)
    columnaY.append(y)
    columnaZ.append(z)
    columnaPasos.append(n)
    columnar.append(r)
    columnad.append(d)
    

f= open ("marcha-aleatoria.dat","w")
for i in range (len(columnaX)):
       f.write(str(columnaX[i]) + " " + str(columnaY[i]) + " " + str(columnaZ[i])+ " " + str(columnaPasos[i]) + " " + str(columnar[i])+ " " + str(columnad[i]) +  "\n") 
       f.close 
      

          
