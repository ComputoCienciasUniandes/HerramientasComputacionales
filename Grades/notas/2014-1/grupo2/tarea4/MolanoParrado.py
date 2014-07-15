import random

print " Juego : Piedra, papel y tijera "

S = int(input('selecciona tu arma; 1. tijera 2. piedra 3. papel'))

if ( S == 1):
   print" Su seleccion fue : tijera"
elif( S ==2):
   print" Su selecion fue : piedra" 
elif( S ==3):
   print" Su selecion fue : papel"
else:
   print" No es valido"


l = [1,2,3]

Ganador = ["Bien, has ganado, pendejo","que man tan chochon","no, no estaba preparado, hagale otra vez"]
Perdedor = ["Jajaja, ay pero que idiota","Nooo loco, usted si es pero malo","No da la talla viejo"]
Empate = ["No mameees","rapido, quiero decidir esto de una vez"]

M = random.choice(l)

if (M == 1):
   print" He seleccionado tijera "
elif( S == 2):
   print"  He seleccionado piedra" 
elif( S == 3):
   print"  He seleccionado papel"


if (S == M):
 print random.choice(Empate)
elif ( S == 3 and M == 2):
 print random.choice(Ganador)
elif ( S == 2 and M == 1):
 print random.choice(Ganador)
elif ( S == 1 and M == 3):
 print random.choice(Ganador)
elif ( S == 3 and M == 1):
 print random.choice(Perdedor)
elif ( S == 2 and M == 3):
 print random.choice(Ganador)
elif ( S == 1 and M == 2):
 print random.choice(Ganador)
