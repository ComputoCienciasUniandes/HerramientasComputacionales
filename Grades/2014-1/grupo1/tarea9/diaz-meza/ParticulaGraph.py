import sys
import math
import random
import numpy as np
import matplotlib as plt
import pylab

archivo=sys.argv[1]

data=np.loadtxt(archivo)

dist=data[:,4]
step=data[:,3]



pylab.scatter(step, dist)
pylab.xlabel("$Number of Steps$", fontsize=15)
pylab.ylabel("$Distance to the Center$", fontsize=15)
pylab.title("Number of Steps vs. Distance to the Center", fontsize=20)
pylab.savefig('Npasos-r.png')
