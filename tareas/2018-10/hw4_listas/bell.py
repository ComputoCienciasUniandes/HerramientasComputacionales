
#punto 1
#definir variables
N=20
listapre=[1]
listapres=[1,2]
listapost=[]

#punto 2
#calcular la N-esima fila del triangulo de Bell, el triangulo de bell se genera con
#
for i in range(2,N):
	
	listapost=[]
	listapost.append(listapres[-1])
	for j in range(i):
		listapost.append(listapost[j]+listapres[j])
			
	listapre=list(listapres)
	listapres=list(listapost)

print(listapost)



#punto 3 Devolver el ultimo elemento de la Nesima fila del triangulo de Bell
print(len(str(listapost[-1])),str(listapost[-1]))
x=str(listapost[-1])



#punto 4
infile = open("code2.txt",'r')
lines= infile.readlines()
file.close()
print(lines)

###punto 5

#decodificar el mensaje, cada digito del numero recien calculado corresponde
##a la posicion de un caracter del mensaje, por ejemplo...

for i in range(len(lines)):
	print(lines[i][int(x[i])])
