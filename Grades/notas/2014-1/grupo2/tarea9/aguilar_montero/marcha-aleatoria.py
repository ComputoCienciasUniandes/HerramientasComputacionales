import matplotlib.pyplot as plt
import sys
import numpy as np

f=np.loadtxt(sys.argv[1])
numpasos = f[:,3]
radios = f[:,4]

plt.scatter(numpasos,radios)
plt.xlabel("$Numero\ de\ pasos$", fontsize=30)
plt.ylabel("$r$", fontsize=30)
plt.title("$Numero\ de\ pasos\ vs.\ r$", fontsize=30)
fi = open("Npasos-r.png","w")
plt.savefig("Npasos-r.png")
