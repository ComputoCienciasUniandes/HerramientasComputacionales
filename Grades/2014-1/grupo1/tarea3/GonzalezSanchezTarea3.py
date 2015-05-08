import numpy as np
comp = 'piedra'
com =  np.random.random_integers(0,2)
if (com == 1):
        comp = 'papel'
elif (com == 2):
        comp = 'tijeras'
ganar = 'perdio'
ply = raw_input('Juegue: piedra, papel o tijeras ')
plyn = 0
if (ply == 'piedra' or ply =='papel' or ply == 'tijeras'):
        if (ply == 'papel'):
                plyn = 1
        elif (ply == 'tijeras'):
                plyn =2

        


        if(plyn == 0 and com == 2):
                ganar = 'gano'
        elif(plyn == 1 and com == 0):
                ganar = 'gano'
        elif(plyn == 2 and com == 1):
               ganar = 'gano '


        if (plyn == com):
                print 'Ha empatado, usted ha escogido '+ ply + ', el computador ha escogido ' + comp

        else: print 'Usted '+ganar+'. Usted escogio ' + ply + ', el computador escogio ' + comp 

else: print 'No ha insertado un valor valido'
