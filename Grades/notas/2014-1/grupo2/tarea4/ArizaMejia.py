import random
print "Bienvenido a piedra, papel o tijera"
repetir = 1
l = ["piedra", "papel", "tijera"]
while (repetir == 1):
    eleccion = 0
    eleccion = input("Elige (1-piedra, 2-papel, 3-tijera): ")
    while (1 > eleccion or eleccion > 3):
        print "Debes marcar una opcion entre 1 y 3"
        eleccion = input("Elige (1-piedra, 2-papel, 3-tijera): ")
    computador = random.randint(1,3)
    if (eleccion == computador):
        print "Empate, el computador eligio ", l[computador-1], " y tu elegiste ", l[eleccion-1]
    else:
        computador2 = computador +1
        if (computador2 > 3):
            computador2 -= 3
        if (eleccion == computador2):
            print "Ganaste, el computador eligio ", l[computador-1], " y tu elegiste ", l[eleccion-1]
        else: print "Perdiste, el computador eligio ", l[computador-1], " y tu elegiste ", l[eleccion-1]
    repetir = input("Elige 1 si deseas volver a jugar: ")
