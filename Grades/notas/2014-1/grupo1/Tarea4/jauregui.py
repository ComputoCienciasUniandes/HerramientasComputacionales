import numpy as np

a = np.random.randint(0, 3)

if (input()=='piedra' & a==0):
    print "Usted jugo 'piedra' y el computador 'piedra': ha empatado"
elif (input()=='piedra' & a==1):
    print "Usted jugo 'piedra' y el computador 'papel': ha perdido"
elif (input()=='piedra' & a==2):
    print "Usted jugo 'piedra' y el computador 'tijeras': ha gando"
elif (input()=='papel' & a==0):
    print "Usted jugo 'papel' y el computador 'piedra': ha gando"
elif (input()=='papel' & a==1):
    print "Usted jugo 'papel' y el computador 'papel': ha empatado"
elif (input()=='papel' & a==2):
    print "Usted jugo 'papel' y el computador 'tijeras': ha perdido"
elif (input()=='tijeras' & a==0):
    print "Usted jugo 'tijeras' y el computador 'piedra': ha perdido"
elif (input()=='tijeras' & a==1):
    print "Usted jugo 'tijeras' y el computador 'papel': ha ganado"
elif (input()=='tijeras' & a==2):
    print "Usted jugo 'tijeras' y el computador 'tijeras': ha empatado"
