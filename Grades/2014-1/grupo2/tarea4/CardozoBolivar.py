#Description : Este programa, juega roshambo
__author__ = 'David Cardozo'
__email__ = 'gd.cardozo684@uniandes.edu.co'

import sys
if sys.version_info <= (3, 0):
    sys.stdout.write('Perdón, se requiere de Python 3.x, no Python 2.x para ejecutar este programa\n')
    sys.exit(1)

import random as rd

play = True
ganados = 0
jugados = 0

while play:
    jugados += 1
    print("Hola, vamos a jugar roshambo, las opciones son las siguientes \n Digita 1 para papel \n Digita 2 para piedra \n Digita 3 para tijeras")
    selection = int(input("Digita una opcion: "))
    while selection > 3 or selection < 1:
        print("Has selecionado una opcion no posible, vuelve a intentar")
        selection = int(input("Digita una opcion: "))

    compu = rd.randint(1, 3)
    if compu == 1:
        print("Computador ha elegido papel")
    if compu == 2:
        print("Computador ha elegido piedra")
    if compu == 3:
        print("Computador ha elegido tijeras")
    if selection == compu:
        print("Existe un empate")
    if selection == 1:
        if compu == 2:
            print("jugador gana, papel envuelve a piedra")
            ganados += 1
        if compu == 3:
            print("Computador gana, tijeras cortan papel")
    if selection == 2:
        if compu == 1:
            print("Computador gana, papel envuelve a piedra")
        if compu == 3:
            print("jugador gana, piedra destroza tijeras")
            ganados += 1
    if selection == 3:
        if compu == 1:
            print("Jugador gana, tijeras cortan papel")
            ganados += 1
        if compu == 2:
            print("Computador gana,piedra destroza tijeras")
    if input("continuar? (si/no) ") == "no":
        print("juegos ganados : ", ganados)
        print("juegos hechos:", jugados)
        play = False

