import random
print "Hola, vamos a jugar piedra, papel o tijera"

dato = int(input('Para comenzar debes escoger 1 si quieres piedra, 2 si quieres papel o 3 si quieres tijera '))
if (dato == 1):
 print "Has seleccionado piedra" 
if (dato == 2):
 print "Has seleccionado papel"
if (dato == 3):
 print "Has seleccionado tijera"
else:
 print "Nos has seleccionado nada"


lista =[1,2,3]
pc = random.choice(lista)

if (pc == 1):
 print "He seleccionado piedra"
if (pc == 2):
 print "He seleccionado papel"
if (pc == 3):
 print "He seleccionado tijera"

if (pc == dato):
 print "Hemos empatado"
elif (pc == 1 and dato == 2):
 print "Me has ganado"
elif (pc == 1 and dato == 3):
 print "Te he ganado"
elif (pc == 2 and dato == 1):
 print "Te he ganado"
elif (pc == 2 and dato == 3):
 print "Me has ganado"
elif (pc == 3 and dato == 1):
 print "Me has ganado" 
elif (pc== 3 and dato == 2):
 print "Te he ganado"
