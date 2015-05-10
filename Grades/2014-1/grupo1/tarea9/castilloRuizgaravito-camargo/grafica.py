import numpy as np
import sys
import math
import matplotlib as plt
import pylab as py 

data = np.loadtxt("datosTrayectoria.dat")

x = data[:,3]#datos de Numero de pasos
y = data[:,4]# Distancias 

py.plot (x, y, '-r', c='g', label="Datos")
py.title("$Grafica\ de\ pasos\ Vs\ distancia\ de\ la\ particula\ al\ centro$", fontsize=20)
py.xlabel("$Pasos$", fontsize= 20)
py.ylabel("$Distancia\ particula$", fontsize=20)
py.legend(loc=2)

py.show()
py.savefig("Npasos-r.png")


