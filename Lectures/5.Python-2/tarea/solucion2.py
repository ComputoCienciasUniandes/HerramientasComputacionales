import numpy as np
import sys

def player_number(sys.argv[1]):
    if sys.argv[1]=="piedra":
        n = 0
        return n
    elif sys.argv[1]=='papel':
        n = 1
        return n
    elif sys.argv[1]=='tijera':
        n=2
        return n
    else:
        print "por favor escoge entre piedra, papel o tijera"

def computer():
    n = np.random.randint(0,3)
    if n==0:
        comp = "piedra"
        return comp
    elif n==1:
        comp = "papel"
        return comp
    elif n==2:
        comp = "tijera"
        return comp

def juego(comp, n):
    x = player_number(sys.argv[1])
    y = np.random.randint(0,3)
    if x==y:
        print "empate"
