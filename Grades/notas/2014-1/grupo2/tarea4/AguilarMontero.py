import numpy as np
import sys

a=1
b=2
c=3
d=0
e=0

x = sys.argv[1]
if (x == "piedra"):
    d=a
    print "jugador juega piedra"
if (x == "papel"):
    d=b
    print "jugador juega papel"
if (x == "tijeras"):
    d=c
    print "jugador juega tijeras"


if (d==a):
    e=np.random.randint(1,4)
    if(e==a):
       print "computador juega piedra"
       print "empate"
    if(e==b):
       print "computador juega papel"
       print "computador gana"
    if(e==c):
       print "computador juega tijeras"
       print "jugador gana"

if (d==b):
    e=np.random.randint(1,4)
    if(e==a):
       print "computador juega piedra"
       print "jugador gana"
    if(e==b):
       print "computador juega papel"
       print "empate"
    if(e==c):
       print "computador juega tijeras"
       print "computador gana"

if (d==c):
    e=np.random.randint(1,4)
    if(e==a):
       print "computador juega piedra"
       print "computador gana"
    if(e==b):
       print "computador juega papel"
       print "jugador gana"
    if(e==c):
       print "computador juega tijeras"
       print "empate"

