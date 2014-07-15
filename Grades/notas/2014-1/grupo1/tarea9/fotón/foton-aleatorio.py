import numpy 
import sys
import math
import matplotlib.pyplot as plt



a = sys.argv[1]

data = numpy.loadtxt(a)

plt.plot(data[:,3], data[:,4])
plt.title("$Grafica\ de\ pasos\ Vs\ distancia$", fontsize=20)
plt.xlabel("$Distancia\ particula$", fontsize=20)
plt.ylabel("$Pasos$", fontsize= 20)



plt.show()
plt.savefig("grafica pasos vs distancia.png")
