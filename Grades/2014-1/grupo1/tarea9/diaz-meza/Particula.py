import sys
import random
import math

X=0.0
Y=0.0
Z=0.0
x=0.0
y=0.0
z=0.0
R=float(sys.argv[1])
Npasos=0.0
Rhecho=0.0
Rtotal=0.0
fi=0.0
teta=0.0
listaX=[]
listaY=[]
listaZ=[]
listaN=[]
listaR=[]

def RandomAngulos():
  angle=random.random()*(2*math.pi)
  return angle

while (Rtotal<R):
  fi=RandomAngulos()
  theta=RandomAngulos()
  x=(math.sin(fi))*(math.cos(theta))
  y=(math.sin(fi))*(math.sin(theta))
  z=(math.cos(fi))
  X+=x
  Y+=y
  Z+=z
  Rtotal=math.sqrt(math.pow(X, 2)+math.pow(Y, 2)+math.pow(Z, 2))
  Npasos+=1
  listaX.append(X)
  listaY.append(Y)
  listaZ.append(Z)
  listaN.append(Npasos)
  listaR.append(Rtotal)

f=open('marcha-aleatoria.dat', 'w')

for i in range (len(listaX)):
  f.write(str(listaX[i])+" "+str(listaY[i])+" "+str(listaZ[i])+" "+str(listaN[i])+" "+str(listaR[i])+"\n")
f.close()


  
  
  
  
