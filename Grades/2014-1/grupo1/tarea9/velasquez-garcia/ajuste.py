import pylab as plt
import numpy as np
data = np.loadtxt('marcha-aleatoria.dat')
N = data[:,3]
R = data[:,4]
fit =np.polyfit(N,R,1)
plt.plot(N,fit[0]*N+fit[1],label="ajuste",linewidth=2 ,color='b')
plt.scatter(N,R)
plt.title("$Radio\ vs\ cantidad\ de\ movimientos$", fontsize=30)
plt.xlabel("$Numero\ de\ movimientos$")
plt.ylabel("$Distancia\ del\ nucleo$")
plt.savefig("ajuste.png")
plt.legend(loc="upper left")

