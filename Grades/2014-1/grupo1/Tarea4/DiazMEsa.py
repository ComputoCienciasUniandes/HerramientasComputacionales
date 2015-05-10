import sys
import random


prieda=0
papel=1
tijera=2
var=0

a=sys.argv[1]

if a=="piedra":
   var=0
   x= random.randrange(3)
   if x==var:
       print "Hay un empate:"
       print "Jugador: piedra"
       print "Computadora: piedra"
   if x==1:
       print "La Computadora es la Ganadora"
       print "Jugador: piedra"
       print "Computadora: papel"
   if x==2:
       print "El Jugador es el Ganador"
       print "Jugador: piedra"
       print "Computadora: tijera"
if a=="papel":
    var=1
    x= random.randrange(3)
    if x==0:
       print "El Jugador es el Ganador"
       print "Jugador: papel"
       print "Computadora: piedra"
    if x==var:
       print "Hay un empate:"
       print "Jugador: papel"
       print "Computadora: papel"
    if x==2:
       print "La Computadora es la Ganadora"
       print "Jugador: papel"
       print "Computadora: tijera"
if a=="tijera":
    var=2
    x=random.randrange(3)
    if x==0:
       print "La Computadora es la Ganadora"
       print "Jugador: tijera"
       print "Computadora: piedra"
    if x==1:
       print "El jugador es el Ganador"
       print "Jugador: tijera"
       print "Computadora: papel"
    if x==var:
       print "Hay un empate:"
       print "Jugador: tijera"
       print "Computadora: tijera"

print ""
print "Gracias por jugar con el Programa"
print ""
print "Desarrollador:"
print "Sergio Diaz"
print "Codigo: 201224162"



