import math
import random
import sys 
import numpy as np
def angulos ():
    ang=np.random.random()*2*np.pi
    return ang
RP=float(sys.argv[1])
xt=0.0
yt=0.0
zt=0.0
x=0.0
y=0.0
z=0.0
listax=[]
listay=[]
listaz=[]
pasos=0.0
distancia=[]
p = []
r=0.0

while (r<RP):
    t=angulos()
    f=angulos()
    x+=math.sin(t)* math.cos(f)
    y+=math.sin(f)* math.cos(f)
    z+=math.cos(t)
    r=np.sqrt(x**2+y**2+z**2)
    listax.append(xt)
    listay.append(yt)
    listaz.append(zt)
    distancia.append(r)
    pasos=+1
    p.append(pasos)
    xt=+x
    yt=+y
    zt=+z

    
data=open('marcha-aleatoria.dat','w')

for i in range(len(listax)):
    data.write(str(listax[i])+"  "+str(listay[i])+"  "+str(listaz[i])+"  "+str(p[i])+" "+str(distancia[i])+"\n")
data.close()


    




