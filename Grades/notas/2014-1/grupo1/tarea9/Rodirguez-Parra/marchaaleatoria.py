import sys 
import random 
import math 

r = float(sys.argv[1])

x = 0.0
y = 0.0 
z = 0.0

X = 0.0
Y = 0.0
Z = 0.0

p = 0.0
R = 0.0

angulo1 = 0.0
angulo2 = 0.0

lx = []
ly = []
lz = []
lp = []
lr = []

def anguloaleatorio():
    an = random.random()*(2*math.pi)
    return an

while (R<r):
    angulo1 = anguloaleatorio()
    angulo2 = anguloaleatorio()
    
    x = (math.sin(angulo1))*(math.cos(angulo2))
    y = (math.sin(angulo1))*(math.sin(angulo2))
    z = (math.cos(angulo1))

    X+=x
    Y+=y
    Z+=z

    p+=1
    R = math.sqrt(math.pow(X, 2)+math.pow(Y, 2)+math.pow(Z, 2))

    lx.append(X)
    ly.append(Y)
    lz.append(Z)
    lp.append(p)
    lr.append(R)


q = open('marcha-aleatoria.dat', 'w')

for i in range (len(lx)):
    q.write(str(lx[i])+" "+str(ly[i])+" "+str(lz[i])+" "+str(lp[i])+" "+str(lr[i])+"\n")
q.close()
    
