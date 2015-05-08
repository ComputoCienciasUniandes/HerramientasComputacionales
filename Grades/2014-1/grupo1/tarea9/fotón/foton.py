# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>


import numpy 
import sys
import math
import matplotlib.pyplot as plt


# <codecell>

u = numpy.random.random()*2*math.pi
v = numpy.random.random()*math.pi

# <codecell>

x = math.sin(u)*math.cos(v)
y = math.sin(u)*math.sin(v)
z = math.cos(u)

# <codecell>

r = 0
R = float(sys.argv[1])

a = 0
b = 0
c = 0
i = 0

X=[]
Y=[]
Z=[]
RA=[]
I=[]
X.append(a)
Y.append(b)
Z.append(c)
RA.append(r)
I.append(0)
while r <= R:
    
    i=i+1
    u = numpy.random.random()*2*math.pi
    v = numpy.random.random()*math.pi
    
    x = math.sin(u)*math.cos(v)
    y = math.sin(u)*math.sin(v)
    z = math.cos(v)
    a = a+x
    b = b+y
    c = c+z
    
    X.append(a)
    Y.append(b)
    Z.append(c)
    
    I.append(i)

    
    r = math.sqrt((X[-1]**2)+(Y[-1]**2)+(Z[-1]**2))
    RA.append(r)
    

# <codecell>

print r

# <codecell>

print RA

# <codecell>

plt.plot(I,RA)
plt.show()

# <codecell>

datos = open("datos.dat","w")

# <codecell>

for i in range(len(X)):
    xim = str(X[i])
    yim = str(Y[i])
    zim = str(Z[i])
    Iim = str(I[i])
    RAim = str(RA[i])
    datos.write(xim+" "+yim+" "+zim+" "+Iim+" "+RAim+"\n")

# <codecell>


