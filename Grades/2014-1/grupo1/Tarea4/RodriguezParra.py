import sys 
import numpy as np


x = sys.argv[1]

y = np.random.randint(3) 

w = 0 

a = "piedra"
b = "papel"
c = "tijera"

if x == "piedra":
    w = 0
if x == "papel":
    w = 1
if x == "tijera":
    w = 2

print "usted escogio : " , x 

if y == 0:
    print "El compu escogio :" , a
if y == 1:
    print "El compu escogio :" ,  b
if y == 2:
    print "El compu escogio :" ,  c 


if y == w:
    print "Resultado: Hay empate"

if y == 0 and w == 1:
    print "Resultado: Gana el jugador"
if y == 1 and w == 2:
    print "Resultado: Gana el jugador"
if y == 2 and w == 0:
    print "Resultado: Gana el jugador"
if y == 0  and w == 2:
    print "Resultado: Gana el compu"
if y == 1  and w == 0:
    print "Resultado: Gana el compu"
if y == 2  and w == 1:
    print "Resultado: Gana el compu"

print "SI EL JUEGO NO LE FUNCIONO ES PORQUE USTED NO COLOCO TODAS LAS PALABRAS BIEN; TIENE QUE ESCRIBIR piedra, papel O tijera, RECUERDE  QUE TIENE QUE SER EN MINUSCULAS SIEMPRE"
