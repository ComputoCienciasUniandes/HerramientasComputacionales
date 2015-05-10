import sys
import random

variable = raw_input("Ingresa piedra, papel o tijera: ")
  

if (variable=="piedra"):
           valor=0
           
elif (variable=="tijera"):
           valor=1
elif (variable=="papel"):
           valor=2

t = [0, 1, 2]
a= random.choice(t)

if(a==0 and valor==0):
        print "Empate."
        print "El usuario y el computador seleccionaron piedra."
elif(a==1 and valor==1):
        print "Empate"
        print "El usuario y el computador seleccionaron tijera."
elif(a==2 and valor==2):
        print "Empate" 
        print "El usuario y el computador seleccionaron papel."       
elif(a==0 and valor== 1):
        print "El computador gano"
        print "El usuario selecciono tijera y el computador piedra."
elif(a==0 and valor==2):
        print "El usuario gano"
        print "El usuario selecciono papel y el computador piedra."
elif(a==1 and valor==0):
        print "El usuario gano"
        print "El usuario selecciono piedra y el computador tijera."
elif(a==1 and valor==2):
        print "El computador gano."
        print "El usuario selecciono papel y el computador tijera."
elif(a==2 and valor==0):
        print "El computador gano."
        print "El usuario selecciono piedra y el computador papel."
elif(a==2 and valor==1):
        print "El usuario gano."
        print "El usuario selecciono tijera y el computador papel."


 







