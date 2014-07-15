import sys
import random

x = 0

if sys.argv[1]==str("piedra"):
    x=0

if  sys.argv[1]==str("papel"):
    x=1

if sys.argv[1]==str("tijera"):
    x=2

y = random.randint(0, 2)


if x == 0:
    print "Has escogido: Piedra"
if x == 1:
    print "Has escogido: Papel"
if x == 2:
    print "Has escogido: Tijera"


if y == 0:
    print "El computador ha escogido: Piedra"
if y == 1:
    print "El computador ha escogido: Papel"
if y == 2:
    print "El computador ha escogido: Tijera"


if y==x:
    print "Es un empate -_-"


if (y==2 and x==0) or (y==0 and x==1) or (y==1 and x==2):
    print "Felicitaciones!"
    print "Has ganado :)"


if (y==1 and x==0) or (y==2 and x==1) or (y==0 and x==2):
    print "Has perdido :("
    print "Vuelva a intentarlo"








