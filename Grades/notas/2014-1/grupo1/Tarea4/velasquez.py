
import numpy as np
import sys
a=1
b=2
c=3
d=0
e=0

w = sys.argv[1]
if (w == "piedra"):
    e=a
    print "juagador juega piedra"
if (w == "papel"):
    e=b
    print "juador juega papel"
if (w == "tijeras"):
    e=c
    print "juagador juega tijeras"

if(e==a):
    d= np.random.randint(1,4)
    if(d==a):
        print "PC juega piedra"
        print "piedra vs piedra, empate"
    if(d==b):
        print "PC juega papel"
        print "piedra vs papel, gana computador, pierda toda esperanza"
    if(d==c):
        print "PC juega tijeras"
        print "piedra vs tijeras, gana juagador"
if(e==b):
    d= np.random.randint(1,4)
    if(d==a):
        print "PC juega piedra"
        print "papel vs piedra, gana jugador"
    if(d==b):
        print "PC juega papel"
        print "papel vs papel, empate"
    if(d==c):
        print "PC juega tijeras"
        print "papel vs tijeras, gana computado pierda toda esperanzar"

if(e==c):
    d= np.random.randint(1,4)
    if(d==a):
        print "PC juega piedra"
        print "tijera vs piedra, gana computador, pierda toda esperanza"
    if(d==b):
        print "PC juega papel"
        print "tijera vs papel, gana jugador"
    if(d==c):
        print "PC juega tijeras"
        print "tijeras vs tijeras, empate"
 



