import random
papel=0.34
tijeras=0.67
piedra =0

u=raw_input("piedra, papel o tijeras")
if u=="piedra":v=piedra
if u=="papel":v=papel
if u=="tijeras":v=tijeras
piedra =0

a= random.random()
if 0.666<a:maquina=tijeras
elif 0.333<a:maquina=papel
else: maquina=papel
if  (maquina-v)**(2/2)>0.6 and maquina>v: print "Gana usuario con piedra"
elif (maquina-v)**(2/2)>0.6 and maquina<v: print "Gana maquina con piedra"
elif maquina<v:print"Gana usuario con "+u
elif 0.67>maquina>v:print"Gana maquina con tijeras"
elif maquina>v==0:print"Gana maquina con papel"
else: print "Empate"

    
