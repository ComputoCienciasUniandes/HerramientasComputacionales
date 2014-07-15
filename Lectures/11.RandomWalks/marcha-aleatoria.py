import numpy as np
import matplotlib.pyplot as plt
import sys 

R = float(sys.argv[1])

j = []
rad = []
i=0
x=([0])
y=([0])
X = 0
Y = 0
r = 0
R = 10
while r < R:
    i+=1
    j.append(i)
    theta = np.random.rand()*2*180
    X += np.cos(theta) 
    Y += np.sin(theta) 
    x.append(X)
    y.append(Y)
    r = np.sqrt(X**2 + Y**2)
    rad.append(r)

f = open("marcha-aleatoria.dat", "w")
for i in range(len(x)):
	f.write(str(x[i]) + "  " +  str(y[i]) + "\n")
f.close


