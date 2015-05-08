import sys
import random
import math
radio=float(sys.argv[1])
x=0.0
y=0.0
z=0.0
pasos=0.0
r=0.0
listax=[0]
listay=[0]
listaz=[0]
listaPasos=[0]
listaDistancia=[0]
#Metodo que realiza el movimiento aleatorio
while r<radio:
    teta=random.random()*2*math.pi
    phi= random.random()*2*math.pi
    x= x+(math.sin(teta)*math.cos(phi))
    y= y+(math.sin(teta)*math.sin(phi))
    z= z+(math.cos(teta))
    r=math.sqrt((x**2)+(y**2)+(z**2))
    pasos+=1
    listaDistancia.append(r)
    listaPasos.append(pasos)
    listax.append(x)
    listay.append(y)
    listaz.append(z)

#Metodo que crea el archivo .dat

archivo=open('marcha-aleatoria.dat','w')
for i in range (len(listax)):
    archivo.write(str(listax[i])+" "+str(listay[i])+" "+str(listaz[i])+" "+str(listaPasos[i])+" "+str(listaDistancia[i])+'\n')