import sys
import random

x=0

if sys.argv[1]==str("piedra"):
    x=0
if sys.argv[1]==str("papel"):
    x=1
if sys.argv[1]==str("tijera"):
    x=2

y=random.randint(0,2)

if y==0:
    print "El computador escogio piedra"
if y==1:
    print "El computador escogio papel"
if y==2:
    print "El computador escogio tijera"

if x==0:
    print "Escogiste piedra"
if x==1:
    print "Escogiste papel"
if x==2:
    print "Escogiste tijera"

if y==x:
    print "Empate"
if (y==0 and x==1)or(y==1 and x==2)or(y==2 and x==0):
    print "Ganaste"
if (y==0 and x==2)or(y==1 and x==0)or(y==3 and x==1):
    print "Perdiste"




