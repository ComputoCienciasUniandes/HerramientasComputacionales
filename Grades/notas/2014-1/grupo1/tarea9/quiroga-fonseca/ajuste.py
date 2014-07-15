# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import numpy
import matplotlib.pyplot as plt
import sys
from scipy.optimize import curve_fit

filename = sys.argv[1]
data = numpy.loadtxt(filename).T

N_points = data[3]
r = data[4]

def plfunc(x,a,b,c,d,e,f,g,h):
    return a+b*x+c*x**2+d*x**3+e*x**4+f*x**5+g*x**6+h*x**8
    
fitpars, covmat = curve_fit(plfunc,N_points,r)

fig = plt.figure()
plt.plot(N_points,r)
plt.plot(N_points, plfunc(N_points, fitpars[0], fitpars[1], fitpars[2], fitpars[3], fitpars[4], fitpars[5], fitpars[6], fitpars[7]), 'r-')
plt.title('Fitting')
plt.xlabel('Num pasos')
plt.ylabel('Distancia recorrida')
plt.show()
fig.savefig('ajuste.png')

# <codecell>


