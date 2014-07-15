import sys
import random

Piedra =0
Papel=1
Tijeras=2
Jugador=-1
Numero=random.randint(0,2)


def Jugar(b,a):

 if a==Piedra:
  if b==Piedra:
   print "El jugador eligio Piedra, El Computador eligio piedra, Nadie gana" 
 
  if b==Papel:
   print "El jugador eligio Piedra, el computador eligio Papel, Gana el computador"

  if b==Tijeras:
   print "El jugador eligio Piedra, el computador eligio Tijeras, Gana el Jugador"

 if a==Papel:
  if b==Piedra:
   print "El jugador eligio Papel, El Computador eligio piedra, Gana el Jugador" 
 
  if b==Papel:
   print "El jugador eligio Papel, el computador eligio Papel, Nadie gana"

  if b==Tijeras:
   print "El jugador eligio Papel, el computador eligio Tijeras, Gana el Computador"

 if a==Tijeras:
  if b==Piedra:
   print "El jugador eligio Tijeras, El Computador eligio piedra, Gana el Computador" 
 
  if b==Papel:
   print "El jugador eligio Tijeras, el computador eligio Papel, Gana el Jugador"

  if b==Tijeras:
   print "El jugador eligio Tijeras, el computador eligio Tijeras, Nadie gana"



if sys.argv[1] == "Piedra":
 Jugar(Numero,0)

if sys.argv[1] == "Papel":
 Jugar(Numero,1)

if sys.argv[1] == "Tijeras":
 Jugar(Numero,2)
