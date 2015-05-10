import random
import sys

piedra=0
papel=1
tijeras=2

opcionCompu = random.randint(0, 2)
if (opcionCompu==0):
    print "El compu eligio piedra"
if (opcionCompu==1):
    print "El compu eligio papel"
if (opcionCompu==2):
    print "El compu eligio tijeras"

opcionUsu=0
if sys.argv[1]==str("piedra"):
    opcionUsu=0
    print "Elegiste piedra"
if sys.argv[1]==str("tijeras"):
    opcionUsu=1
    print "Elegiste tijeras"
if sys.argv[1]==str("papel"):
    opcionUsu=2
    print "Elegiste papel"



if (opcionCompu==opcionUsu):
    print "Ninguno de los dos gana"
if(opcionCompu ==piedra) and (opcionUsu==1):
    print "El compu gana"
if(opcionCompu==piedra) and (opcionUsu==2):
    print "El compu gana"
if(opcionCompu==papel) and (opcionUsu==0):
    print "El compu gana"
if(opcionCompu==papel) and (opcionUsu==1):
    print "El usuario gana"
if (opcionCompu==tijeras) and (opcionUsu==0):
    print "El usuario gana"
if(opcionCompu==tijeras) and (opcionUsu==2):
    print "El compu gana"


