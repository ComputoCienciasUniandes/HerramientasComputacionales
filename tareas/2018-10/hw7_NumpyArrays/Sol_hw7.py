import numpy as np



#Ejercicio 1
#1b
#Arreglo de 1 a 2pi con 1000 puntos
x=np.linspace(0, 2.0*np.pi, 100000)

#1c
#Funcion que recibe x y retorna sin(x)
def fun_sen(x):
	return np.sin(x)

y=fun_sen(x)

#1d
#Maximos y minimos de la funcionFuncion que recibe x y retorna sin(x)
print "El maximo de la funcion es", np.max(y), "y ocurre para un x", x[np.argmax(y)] 



#1e
#derivada en el punto maximo
derivada1=(y[np.argmax(y)+1]-y[np.argmax(y)])/(x[np.argmax(y)+1]-x[np.argmax(y)])
print "la derivada en el punto maximo es: ", derivada1 


#1f
#derivada en el intervalo
derivada=(y[1:]-y[0:-1])/(y[1]-y[0])


#1g
#diferencia entre la derivada y cos(x)
def fun_cos(x):
	return np.cos(x)
coseno=fun_cos(x)

dif=derivada - coseno[1:]
print "la maxima diferencia entre la derivada y la funcion cos(x) es: ", np.max(dif)


#1h
#el promedio de la derivada numerica es:
print"el promedio de la derivada numerica es: ", np.mean(derivada)



