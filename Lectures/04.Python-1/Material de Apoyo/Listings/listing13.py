numero_leido = raw_input("inserta un numero >> ")
numero = int(numero_leido)
contador = 0
for i in range(1,numero+1):
    if (numero% i)==0:
        contador = contador + 1

if contador==2:
    print "el numero es primo"
else print "el numero no es primo"