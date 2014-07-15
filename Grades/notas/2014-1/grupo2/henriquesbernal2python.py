import numpy as np
import sys

piedra=1
papel=2
tijera=3

x=sys.argv[1]
if(x=="piedra"):
    y=np.random.randint(1,3)
    if(y==1):
        print "maquina:piedra, empate"
    elif(y!=1):
        if(y==2):
            print "maquina:papel,perdio"
        else:
            print "maquina:tijera, gano"
elif(x=="papel"):
     y=np.random.randint(1,3)
     if(y==2):
         print "maquina:papel, empate"
     elif(y!=2):
         if(y==3):
             print "maquina:tijera, perdio"
         else:
             print "maquina:piedra, gano"
elif(x=="tijera"):
    y=np.random.randint(1,3)
    if(y==3):
        print "maquina tijera, empate"
    elif(y!=3):
        if(y==1):
            print "maquina piedra, perdio"
        else:
            print "maquina papel,gano"
else:
    print "opcion no valida"
