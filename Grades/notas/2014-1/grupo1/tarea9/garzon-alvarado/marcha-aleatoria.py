import numpy as np
import matplotlib as plt
import pylab
import sys

#Metodo que carga el archivo
archivo=sys.argv[1]
data=np.loadtxt(archivo)

#Metodo que lee el archivo
distancia=data[:,3]
pasos=data[:,4]

#Metodo que grafica los datos leidos del archivo

pylab.scatter(distancia, pasos,color='green')
pylab.xlim([-10,(len(distancia)+10)])
pylab.xlabel("Numero de pasos", fontsize=10)
pylab.ylabel("Distancia al origen", fontsize=10)
pylab.title("Numero de pasos vs Distancia al origen", fontsize=20,color="red")

#Metodo que guarda el grafico como archivo .png

pylab.savefig('Npasos-r.png')

