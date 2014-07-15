import sys
import numpy as np
s=0
t=0
x=0
y=0
z=0
X = 0  
Y = 0 
Z = 0
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
    s = np.random.randint(0,np.pi*2)
    t = np.random.randint(0,np.pi)
    x = r*np.sin(t)*np.sin(s) 
    y = r*np.sin(t)*np.cos(s)
    z = r*np.cos(t)
    X += x
    Y += y
    Z += z
    radio = np.sqrt(X**2+Y**2+Z**2)
    archivoX.append(X)
    archivoY.append(Y)
    archivoZ.append(Z)
    archivoR.append(radio)
    archivoN.append(step)
#print archivoX
a = open("marcha-aleatoria.dat","w")
for i in range(len(archivoN)):
    a.write(str(archivoX[i])+" "+str(archivoY[i])+" "+str(archivoZ[i])+" "+str(archivoR[i])+" "+str(archivoN[i])+"\n")
a.close

