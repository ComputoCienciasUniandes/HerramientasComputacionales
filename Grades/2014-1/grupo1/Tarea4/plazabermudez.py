import sys
%pylab inline 

if sys.argv[1]==str(1):
	print "hola sys"

rand = random.randint(1,3) # 1 piedra, 2 = papel, 3 = tijera

if answer == ("piedra"):
    if rand == (1):
      print "empate"
    if rand == (2):
      print "gana el computador"
    if rand == (3):
      print "gana el jugador"
    
elif answer == ("papel"):
    if rand == (1):
      print "gana el jugador"
    if rand == (2):
      print "empate"
    if rand == (3):
      print "gana el computador"

elif answer == ("tijera"):
    if rand == (1):
      print "gana el jugador"
    if rand == (2):
      print "empate"
    if rand == (3):
      print "gana el computador"
    