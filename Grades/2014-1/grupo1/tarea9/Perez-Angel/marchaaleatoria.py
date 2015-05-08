import math
import random
import sys
import numpy as np

R=float(sys.argv[1])
x1=0.0
y1=0.0
z1=0.0
radio=[]
Xm=[]
Ym=[]
Zm=[]
pasos=0.0
mango=0.0
Pasosm=[]
radiosacumulados=[]

def angulos():
    tetha=random.random()*2*math.pi
    return tetha

while mango < R:
    teta=angulos()
    phi=angulos()
    x=math.sin(teta)*math.cos(phi)
    y=math.sin(teta)*math.sin(phi)
    z=math.cos(teta)
    x1+=x
    y1+=y
    z1+=z
    pasos+=1
    mango=math.sqrt(x1**2+y1**2+z1**2)
    Xm.append(x1)
    Ym.append(y1)
    Zm.append(z1)
    Pasosm.append(pasos)
    radiosacumulados.append(mango)

file=open('marcha-aleatoria.dat' , 'w' )
for i in range(len(Xm)):
    file.write(str(Xm[i])+ ' ' +str(Ym[i])+ ' ' +str(Zm[i])+ ' '+str(Pasosm[i])+ ' ' +str(radiosacumulados[i])+'\n')
file.close()




