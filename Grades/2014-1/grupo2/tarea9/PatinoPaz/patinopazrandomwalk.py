import numpy as np
import math as mt
import sys

R =float(sys.argv[1])
i = 0
x = 0
y = 0
z = 0
r = 0
radio = []
listax = []
listay = []
listaz = []
listaN = []
listad = []
while r<R:
    i=i+1
    listaN.append(i)
    factortheta = np.random.rand()
    factorphi = np.random.rand()
    x = x + mt.cos(2*mt.pi*factortheta)*mt.sin(np.pi*factorphi)
    listax.append(x)
    y = y + mt.sin(2*np.pi*factortheta)*mt.sin(np.pi*factorphi)
    listay.append(y)    
    z = z + mt.cos(np.pi*factorphi)
    listaz.append(z)
    r = mt.sqrt((x**2)+(y**2)+(z**2))    
    radio.append(r)


    
f = open("marcha-aleatoria.dat", "w")
for j in range(len(listax)):
    f.write(str(listaN[j])+" "+ str(listax[j])+" "+ str(listay[j])+" " +str(listaz[j])+" "+str(radio[j])+ "\n")
f.close
