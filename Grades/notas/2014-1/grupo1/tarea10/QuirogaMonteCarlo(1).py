# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import matplotlib.pyplot as plt
import numpy as np

def lafunc(x):
    return np.exp(-(x**2))
minx = -5.0
maxx = 5.0
x = np.linspace(minx,maxx,1000)
gausiana = lafunc(x)
plt(x,gausiana)

# <codecell>

miny = 0.0
maxy = amax(gausiana)
print miny, maxy

# <codecell>

nrandom = 10000
randomx = random.rand(nrandom) * (maxx - minx) + minx
randomy = random.rand(nrandom) * (maxy - miny) + miny

# <codecell>

delta = lafunc(randomx) - randomy
below  = where(delta>0.0)
scatter(randomx[below], randomy[below])

# <codecell>

intervalo = (maxy-miny) * (maxx - minx)
integral  = intervalo * (size(below)/(1.0*size(randomy)))

# <codecell>

print 'adentro:', size(below), 'total:', size(randomy)

# <codecell>


