import matplotlib.pyplot as plt
import sys
import numpy as np

f=np.loadtxt(sys.argv[1])
numpasos = f[:,3]
radios = f[:,4]

plt.scatter(numpasos,radios)
plt.xlabel("$Numero\ de\ pasos$", fontsize=30)
plt.ylabel("$r$", fontsize=30)
plt.title("$Numero\ de\ pasos\ vs.\ r\ con\ ajuste\$", fontsize=30)
fit=np.polyfit(numpasos, radios,1)
plt.plot(numpasos, fit[0]*numpasos + fit[1], linewidth=2.5)
fi = open("ajuste.png","w")
plt.savefig("ajuste.png")
