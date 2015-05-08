import sys
import numpy as np

p=sys.argv[1]
print p, "eleccion del jugador"
numero=np.random.random()*3
aleatorio="ni idea"
#piedra entre 0 y 1 
#papel entre 1 y 2
#tijeras entre 2 y 3

if(numero<1):
    aleatorio="piedra"

if(2<=numero and numero<3):
    aleatorio="tijera"

if(1<=numero and numero<2):
    aleatorio="papel"

print aleatorio, " eleccion de la terminal"

if(p==aleatorio):
    print "empate de ", p
    
#faltan los duales 
if(p=="piedra" and aleatorio=="tijera"):

    print "jugador gana"

if(p=="tijera" and aleatorio=="piedra"):

    print "jugador pierde"

if(p=="piedra" and aleatorio=="papel"):
    print "jugador pierde"

if(p=="papel" and aleatorio=="piedra"):
    print "jugador gana"


if(p=="papel" and aleatorio=="tijera"):
    print "jugador pierde"

if(p=="tijera" and aleatorio=="papel"):
    print "jugador gana"






