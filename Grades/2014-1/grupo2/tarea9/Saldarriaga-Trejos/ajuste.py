import matplotlib.pyplot as plt
import numpy as np
import sys


data= np.loadtxt(sys.argv[1])

x=data[:,0]
y=data[:,1]
z=data[:,2]
r=data[:,3]
pasos=data[:,4]


plt.plot(r, pasos, linewidth=2.0, c='r', label="Real")
plt.scatter(r, pasos)
plt.xlabel("$Distancia$", fontsize=30)
plt.ylabel("$Numero de Pasos$", fontsize=30)
plt.title("Pasos vs. Distancia", fontsize=30)

def R2(xexp, xteo):
    EE = sum((xteo-xexp)**2)
    mean = sum(xexp)/(len(xexp))
    variance = sum((mean-xexp)**2)
    R2 = 1 - EE/variance
    return R2

R2(pasos, pasos)
plt.savefig("ajuste.png")

