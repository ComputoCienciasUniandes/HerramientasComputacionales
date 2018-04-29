#! /usr/bin/python 

# Empezando n = 27, la sucesion tiene 112 pasos, llegando hasta 9232 antes de 
# descender a 1. Definimos el numero inicial y un contador que inicia en 1, de 
# manera que no cuente el numero de pasos sino los elementos es la secuencia.

x=27
counter=1

print "Los numeros en la sucesion empezando en ",x," son:"
print x        

# Nuestro ciclo para cuando el numero alcance 1, el numero mas pequenho posible.
# Si es par, lo divide entre dos. De lo contrario, es decir, si es impar, lo 
# multiplica por tres y le suma uno. Luego lo imprime y continua el proceso. 
# Cada vez que entra al ciclo, suma uno al contador.

while x!=1:
    if x%2 == 0 :
        x=x/2
    else:
        x=3*x+1
    print x
    counter+=1
print "Asi, el tiempo de orbita es de ",counter," elementos en la sucesion"

