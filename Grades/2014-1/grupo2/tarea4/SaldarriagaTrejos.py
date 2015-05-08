import sys
import numpy as np

r= np.random.randint(0,3)

if r==0:
    n= "Scissors"
    i=0
elif r==1:
    n="Rock"
    i=1
elif r==2:
    n="Paper"
    i=2

if sys.argv[1]== "Rock":
    p= "Rock"
    j=1
elif sys.argv[1]=="Scissors":
    p="Scissors"
    j=0
elif sys.argv[1]=="Paper":
    p= "Paper"
    j=2
else:
    p= "No valido"

if i==j:
    print"Empate!"
elif i==0 & j==1:
    print"Ganaste!"
elif i==1 & j==2:
    print"Ganaste!"
elif i==2 & j==0:
    print"Ganaste!"
elif i==2 & j==1:
    print"Perdiste!"
elif i==0 & j==2:
    print "Perdiste!"
elif i==1  & j==0 :  
    print "Perdiste!"
else:
    print "Error: Asegurese que la primera letra este en mayuscula"

print "El jugador escogio:"+ p
print "El computador escogio:"+ n
