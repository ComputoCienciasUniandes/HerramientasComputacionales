import numpy as np
import sys
import math
import pylab

#Metodo que descarga archivo

archivo=sys.argv[1]
data=np.loadtxt(archivo)

#Metodo que lee el archivo
distancia=data[:,3]
pasos=data[:,4]

#Metodo que realiza el procedimiento de minimos cuadrados
fit= pylab.polyfit(distancia, pasos,1)

#Metodo que grafica lo leido en el archivo y calculado en el fit.

pylab.plot(distancia, distancia*fit[0] + fit[1], linewidth='1.5',color='red', label= "Ecuacion de la recta "'\n'+ str(fit[0])+'x+'+'('+str(fit[1])+')')
pylab.scatter(distancia, pasos,color='green')
pylab.xlim([-10,(len(distancia)+10)])
pylab.legend(loc='upper left')
pylab.xlabel("Numero de pasos", fontsize=10)
pylab.ylabel("Distancia al origen", fontsize=10)
pylab.title("Numero de pasos vs Distancia al origen", fontsize=20)

#Metodo que guarda el grafico como archivo .png

pylab.savefig('ajuste.png')