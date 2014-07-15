import sys
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

archivo= sys.argv[1]
data=np.loadtxt(archivo)

r=data[:,3]
n=data[:,4]

pl.scatter(n,r)
pl.xlabel("$Pasos$", fontsize=30)
pl.ylabel("$Radio$", fontsize=30)
pl.title("Pasos vs Radio", fontsize=30)
pl.savefig("marcha.png")
