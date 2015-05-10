import matplotlib.pyplot as plt
import sys
import numpy as np

x=0
y=0
z=0
r=0
radio=float(sys.argv[1])
Npasos=0
pasos=[]
radios=[]
xx=[]
yy=[]
zz=[]



while(r<radio):
 a=np.random.rand()
 b = np.random.rand()
 theta=(np.pi)*a*2
 phi=(np.pi)*b
 Npasos+=1
 x+=np.cos(theta)*np.sin(phi)
 y+=np.sin(theta)*np.sin(phi)
 z+=np.cos(phi)
 r=np.sqrt((x**2)+(y**2)+(z**2))
 pasos.append(Npasos)
 radios.append(r)
 xx.append(x)
 yy.append(y)
 zz.append(z)

f = open("marcha-aleatoria.dat", "w")
for i in range(len(xx)):
    f.write(str(xx[i]) + " " + str(yy[i]) + " " + str(zz[i]) + " " + str(pasos[i]) + " " + str(radios[i]) + "\n")
f.close




