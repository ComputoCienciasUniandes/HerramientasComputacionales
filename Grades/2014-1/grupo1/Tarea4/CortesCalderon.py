import sys
import numpy as np


a = sys.argv[1]
c = 0
d = 0

print ""
print ""
print "Para jugar piedra, papel o tijera, debe ingresar alguna de las siguientes tres opciones tal cual aparecen: piedra o papel o tijera..."
print ""
print ""
print "USTED ESCOGIO:" , a


if a == "tijera":
    d += 1
elif a == "piedra":
    d += 2
elif a == "papel" :
    d += 3
else :
    d += 4
    print "no escribio el argumento de entrada como debia, el juego no funciona asi"

b = np.random.randint (3)

if d == 4:
    print "vuelva a ingresar adecuadamente su eleccion"
elif b == 0:
    c += 1 
    print "el ordenador escogio: tijeras"
elif b == 1:
    c += 2
    print "el ordenador escogio: piedra"
else :
    c += 3
    print "el ordenador escogio: papel"


if d == 4:
    print "vuelva a ingresar adecuadamente su eleccion" 
elif d == c:
    print "hubo empate"
elif c == d+1:
    print "gana ordenador"
elif d == c+2:
    print "gana ordenador"
elif d == 4 :
    print "vulva a escribir el argumento correctamente"
else :
    print "gana jugador"


