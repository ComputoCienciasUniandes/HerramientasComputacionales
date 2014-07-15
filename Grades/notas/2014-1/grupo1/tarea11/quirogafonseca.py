# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%pylab inline
import math

# <codecell>

def func(x):
    y = (exp(-(x)**2))/(((x-3)**2) + (0.01**2)) 
    return y        
   

# <codecell>

X = linspace(-1.5, 4, 1000)
Y = func(X)
plot(X, Y)

# <codecell>

caminata = []
x = random.random()*60
caminata.append(x)

# <codecell>

for i in range(200000):
    x = random.random()*2-1 
    alpha = func(x + caminata[-1])/func(caminata[-1])

    if alpha>=1.0:
        caminata.append(caminata[-1]+x)
    else:
        beta = random.random()
        if(beta<=alpha):
            caminata.append(caminata[-1]+x)
        else:
            caminata.append(caminata[-1])

# <codecell>

histo = hist(caminata, bins=2000, normed=True)
f = func(X)
norm = sum(f*(X[1]-X[0]))
plot(X,f/norm, linewidth=1)

# <codecell>


