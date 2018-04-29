'''
SOLUCION TALLER 4
'''

'''1. Leer el archivo linea por linea'''
fileIn = open('pg1524.txt','r')
lineas = fileIn.readlines()


'''2. Crear y llenar el arreglo de palabras'''
palabras = []

#Separa cada linea en palabras y agrega esto a la lista de palabras
for linea in lineas:
	palabras.extend(linea.split())

'''3. Buscar el numero de palabras de 9 letras'''

#Se define un contador y se aumenta en 1 si encuentra una palabra con 9 letras
contador9 = 0
for palabra in palabras:
	if(len(palabra) == 9):
		contador9 += 1

#Imprime el resultado
print("Hay "+str(contador9)+" palabras con 9 letras")

'''4. Hallar el numero de palabras de 1 a 10 letras'''

#Hay que hacer un ciclo sobre el numero de letras de 1 hasta 10 y adentro otro ciclo igual que el del numeral anterior. El contador se va actualizando para cada corrida del ciclo exterior
i = 1
while i <= 10:
	contador_actual = 0
	for palabra in palabras:
		if(len(palabra) == i):
			contador_actual += 1

	print(i, contador_actual)
	i += 1	
