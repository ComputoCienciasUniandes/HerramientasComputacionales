import random
print "Hola, vamos a jugar piedra, papel o tijera"

dato = int(input('para empezar escribe: 1 si es piedra, 2 si es papel o 3 si e tijera '))
if (dato ==1):
 print "Has seleccionado piedra" 
elif (dato ==2):
 print "Has seleccionado papel"
elif (dato ==3):
 print "Has seleccionado tijera"
else: 
 print "no has seleccionado ninguno de los anteriores, por favor juega de nuevo"
lista = [1,2,3]
comentariosg = ["Va, solo es pura suerte", "No te creas, es que ni me he acomodado", "te crees el rey ahora solo porque estoy mal? ", "Pff eres un pobre iluso, vamos de nuevo", "no quiero que digas nada"]
comentariose = ["parece que tienes madera para esto", "esto no puede quedar asi desempatemos", "En serio no eres tan malo como pensaba", "Empatar pff esos es para debiluchos, vamos de nuevo"]
comentariosp = ["Ja te lo dije soy invencible","No hay nada malo en perder, el problema es perder como tu lo haces", "No es malo perder con el mejor", "Que? quedo asustado?" ]
valormaquina = random.choice(lista)
if (valormaquina ==1):
 print "He seleccionado piedra" 
elif (valormaquina ==2):
 print "He seleccionado papel"
elif (valormaquina ==3):
 print "He seleccionado tijera"


if (dato == valormaquina):
 print random.choice(comentariose)
elif (dato == 3 and valormaquina ==1):
 print random.choice(comentariosp)
elif (dato == 3 and valormaquina==2):
 print random.choice(comentariosg)
elif (dato == 2 and valormaquina ==3):
 print random.choice(comentariosp)
elif (dato == 2 and valormaquina==1):
 print random.choice(comentariosg)
elif (dato == 1 and valormaquina ==2):
 print random.choice(comentariosp)
elif (dato == 1 and valormaquina==3):
 print random.choice(comentariosg)

