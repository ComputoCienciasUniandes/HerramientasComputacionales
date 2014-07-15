import sys
import random

Piedra=1
Papel=2
Tijera=3


lc=sys.argv[1]


if lc=="Piedra":
    variable=1
    c= random.randint(1, 3)
    print c

    if c==1:
        print "Lo Sentimos, hay un Empate:"
        print "Jugador:Piedra"
        print "Maquina:Piedra"

    if c==2:
        print "Maquina,Ha Ganado"
        print "Jugador:Piedra"
        print "Maquina:Papel"
        
    if c==3:
      print "Usted Jugador, Ha Ganado"
      print "Jugador:Piedra"
      print "Maquina:Tijera"

if lc=="Papel":
   varible=2
   c= random.randint(1, 3) 
   print c

   if c==1:
      print "Usted Jugador, Ha Ganado"
      print "Jugador:Papel"
      print "Maquina:Piedra"

   if c==2:
      print "Lo Sentimos, un Empate"
      print "Jugador:Papel"
      print "Maquina:Papel"

   if c==3:
      print "Maquina, Ha  Ganado"
      print "Jugador:Papel"
      print "Maquina:Tijera"

if lc=="Tijera":
   variable=3
   c= random.randint(1,3)
   print c

   if c==1:
     print "Maquina, Ha Ganado"
     print "Jugador:Tijera"
     print "Maquina:Piedra"

   if c==2:
     print "Usted Jugador,Ha Ganado"
     print "Jugador:Tijera"
     print "Maquina: Papel"

   if c==3:
     print "Lo Sentimos, hay un Empate"
     print "Jugador:Tijera"
     print "Maquina:Tijera" 


  



    
       
     













