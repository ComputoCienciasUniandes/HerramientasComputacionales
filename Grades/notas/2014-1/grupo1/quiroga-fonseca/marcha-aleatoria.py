# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import matplotlib.pyplot as plt
import numpy
import sys
filename = sys.argv[1]
data = numpy.loadtxt(filename).T

N_points = data[3]
r = data[4]

fig = plt.figure()
plt.plot(N_points,r)
plt.title('Grafica numero de pasos vs distancia')
plt.xlabel('Num Pasos')
plt.ylabel('Distancia recorrida')
plt.show()
fig.savefig('Npasos-r.png')

# <codecell>


