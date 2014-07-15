import numpy as np
import sys

usuario = sys.argv[1]
pc = ""
numeropc = np.random.randint(0,3)

if numeropc==0:
    pc ="piedra"
if numeropc == 1:
    pc ="papel"
if numeropc == 2:
    pc ="tijera"
print "Usted escogio:"
print usuario
print "El PC escogio:"
print pc
print "Resultado:"
if usuario == pc:
    print "Ha empatado con el PC"
    
if usuario == "piedra" and pc=="papel":
    print "PC gana la partida"

if usuario== "piedra" and pc=="tijera":
    print "Usted gana la partida"

if usuario== "papel" and pc=="piedra":
    print "Usted gana la partida"

if usuario== "papel" and pc=="tijera":
    print "PC gana la partida"

if usuario == "tijera" and pc == "piedra":
    print "PC gana la partida"

if usuario == "tijera" and pc == "papel":
    print "Usted gana la partida"


 






