import sys 
import numpy as ass


#errores al procesar 
if (len(sys.argv)!=2 ):
    print "less arguments than needed"
    exit(1)
if( sys.argv[1]!= "papel" and sys.argv[1]!="piedra" and sys.argv[1]!= "tijera"):
    print "wtf are you playing? Run me again with piedra, papel o tijera"
    exit(1)
#Parametros y metodo
a=sys.argv[1]

b=ass.random.random()*3

if(b<1):
    d="piedra"

if(b>=1 and b<2):
    d="papel"

if(b>=2 and b<3):
    d="tijera"

print d

if(d==a):
  
    print  "damn it, we have got a tie"

if(d=="piedra" and a=="papel"):
    
    print ":( Loooser, i wooon, i wooon "

if(d=="papel" and a=="tijera"):
    
    print ":( Loooser, i wooon, i wooon "

if(d=="tijera" and a=="piedra"):
    
    print ":( Loooser, i wooon, i wooon "


if(a=="piedra" and d=="papel"):
    
    print ":) You won"

if(a=="papel" and d=="tijera"):
    
    print ":) You won"

if(a=="tijera" and d=="piedra"):
    
    print ":) You won"





