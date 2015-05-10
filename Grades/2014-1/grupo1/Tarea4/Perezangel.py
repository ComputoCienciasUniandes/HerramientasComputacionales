import sys
import numpy as np


l = sys.argv[1]
print "ud eligio" , l
t = np.random.randint(3)

if t==0:
    z="tijeras"
    print "la consola eligio" , z

elif t==1:
    z="papel" 
    print "la consola eligio" , z

else :
    z="piedra" 
    print "la consola eligio" , z

if z==l:
    print "hubo empate" 

elif z=="tijeras":
    if l=="piedra":
        print "gana jugador" 

elif z=="tijeras":
    if l=="papel":
        print "gana consola"

elif z=="papel":
    if l=="piedra":
        print "gana jugador"

elif z=="papel":
    if l=="tijeras":
        print "gana consola"

elif z=="piedra":
    if l=="papel":
        print "gana jugador"

elif z=="tijeras":
    if l=="papel":
        print "gana consola" 

elif z=="piedra":
    if l=="tijeras":
        print "gana consola"

else :
    print " no es valido el termino que entra, recuerde que solo se vale 'piedra' , 'papel' , o 'tijeras' " 




