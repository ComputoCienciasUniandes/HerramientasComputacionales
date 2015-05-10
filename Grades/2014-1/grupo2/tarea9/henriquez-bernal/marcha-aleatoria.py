import sys
import numpy as np
teta=0
phi=0
x=0
y=0
z=0
x1 = 0  
y1 = 0 
z1 = 0
r=1
radio=0
step =0
R = float(sys.argv[1])
archivoX=[]
archivoY=[]
archivoZ=[]
archivoR=[]
archivoN=[]
while radio<R :
    step +=1
    teta = np.random.randint(0,np.pi*2)
    phi = np.random.randint(0,np.pi)
    x = r*np.cos(teta)*np.sin(phi) 
    y = r*np.sin(teta)*np.sin(phi)
    z = r*np.cos(teta)
    x1 = x1 + x
    y1 = y1 + y
    z1 = z1 + z
    radio = np.sqrt(x1**2+y1**2+z1**2)
    archivoX.append(x1)
    archivoY.append(y1)
    archivoZ.append(z1)
    archivoR.append(radio)
    archivoN.append(step)
#print archivoX
a = open("marcha-aleatoria.dat","w")
for i in range(len(archivoN)):
    a.write(str(archivoX[i])+" "+str(archivoY[i])+" "+str(archivoZ[i])+" "+str(archivoR[i])+" "+str(archivoN[i])+"\n")
a.close
