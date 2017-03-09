# 1.
	# OPCION A (imprime el indice de solo la primera ocasion donde aparece Waldo)

string = 'abdwaldotasdasdwaldo'

splitted_string = string.split('waldo')
if len(splitted_string) == len(string):
	print("Waldo no se encuentra en ninguna posicion")
else:
	print("Waldo se encuentra en la posicion ", len(splitted_string[0]))

	# OPCION B (imprime el indice de solo la primera ocasion donde aparece Waldo)

i = 0
encontrado = False
while encontrado == False and i <= len(string) - len('waldo'):
	if string[i:i+len('waldo')] == 'waldo':
		encontrado = True
		print("Waldo se encuentra en la posicion ", i)
	i += 1

	# OPCION C (imprime todas las ocasiones en las que aparece Waldo, no solo la primera)
for i in range(len(string) - len('waldo')+1):
	if string[i:i+len('waldo')] == 'waldo':
		print("Waldo se encuentra en la posicion ", i)


# 2. 

input2 = "(()(())))"

contador = 0
incorrecta = False
i = 0
while incorrecta == False and i < len(input2):
	
	if contador < 0:
		incorrecta = True
		print("La sintaxis es incorrecta")
	

	if(input2[i] == "("):
		contador += 1
	elif(input2[i] == ")"):
		contador -= 1
	
	i += 1

if(contador == 0 and incorrecta == False):
	print("La sintaxis es correcta")
elif(contador != 0 and incorrecta == False):
	print("La sintaxis es incorrecta")

		

		
	
