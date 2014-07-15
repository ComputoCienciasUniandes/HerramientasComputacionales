import numpy as np
import sys
import math

print "Marcha Aleatoria 1er punto","\n"

R=float(sys.argv[1])  #Radio del Sol

x=[]
y=[]
z=[]
N=[]
ra=[]

i=0 #contador
r=0 #radio en el que se encuentra la particula
xo=0
yo=0
zo=0
x.append(xo)
y.append(yo)
z.append(zo)
N.append(i)
ra.append(r)

while r<=R:
    i=i+1
    p=1 # distancia de cada  paso

    #para la particula pasos de 1
    phi =np.random.rand()*math.pi
    theta=np.random.rand()*math.pi*2

    
    xi=p* np.sin(phi)* np.cos(theta) #posicion en x
    yi=p* np.sin(phi)* np.sin(theta) #posicion en y
    zi=p* np.cos(phi)#posicion en z
    
    xo=xo+xi
    yo=xo+yi
    zo=xo+zi
    r=(xo**2+yo**2+zo**2)**0.5

    x.append(xo)
    y.append(yo)
    z.append(zo)
    N.append(i)
    ra.append(r)
    
print N[-1],ra[-1], N[-2],ra[-2]

outfile = open ("datosTrayectoria.dat", "w")

#aline = outfile.write("x y z Numero pasos radioPaso \n")
for j in range (len(x)):
    xp=str(x[j])+" "
    yp=str(y[j])+" "
    zp=str(z[j])+" "
    Np=str(N[j])+" "
    rp=str(ra[j])+" "
    aline = outfile.write(xp + yp + zp + Np + rp + "\n ")

outfile.close()

