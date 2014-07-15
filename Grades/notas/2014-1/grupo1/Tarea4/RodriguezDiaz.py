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
   print "El computador eligio piedra"
if y==1:
   print "El computador eligio papel"
if y==2:
   print "El computador eligio tijera"
if x==0:    
   print "Usted escogio piedra"
if x==1:
   print "Usted escogio papel"
if x==2:    
   print "Usted escogio tijera"

if y==0 and x==0 :
   print "Empate"
if y==1 and x==1 :
   print "Empate"
if y==2 and x==2 :
   print "Empate"
if y==0 and x==1 :
   print "Usted gano"
if y==0 and x==2 :
   print "Usted perdio"
if y==1 and x==0 :
   print "Usted perdio"
if y==1 and x==2 :
   print "Usted gano"
if y==2 and x==0 :
   print "Usted gano"
if y==2 and x==1 :
   print "Usted perdio"
if y==0 and x==0 :
   print "Empate"


























