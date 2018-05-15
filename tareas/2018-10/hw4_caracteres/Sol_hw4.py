#ejercicio1 grupo 1
palabra= "parpaaocdelle"
print "GRUPO 1" 
print " " 
if(palabra[0]=="a" and palabra[1]=="o"):
	print "la palabra ", palabra, " empieza por ao"
else:
	print "la palabra ", palabra, "NO empieza por ao"
test=1
i=0
for letra in palabra:
	if (palabra[i] == "a" and palabra[i+1]=="s" and palabra[i+2]=="a"):
		print "la palabra ", palabra, "contiene la secuencia asa"
		test=0
	i=i+1
if test==1:
	print "la palabra ", palabra, "NO contiene la secuencia asa"


alreves=palabra[::-1]
test2=1
j=0
for letra in palabra:
	if (palabra[j] == "c" and palabra[j-1]=="o" and palabra[j-2]=="a"):
		print "la palabra al reves", alreves, "contiene la secuencia coa"
		test2=0
	j=j+1
if test2==1:
	print "la palabra al reves", palabra, "NO contiene la secuencia coa"


#ejercicio2 grupo 1
lista=[ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print lista
lista10=10*lista
print lista10
newlenght=len(lista10)
k=0
unootres=[]
while k < newlenght:
	if lista10[k]==19:
		lista10.pop(k)	
		newlenght=len(lista10)
	if (lista10[k]==3 or (lista10[k]>=10 and lista10[k]<20) ): 
		unootres.append(lista10[k])	

	k+=1

print lista10
print unootres




print " " 
print " " 
print "GRUPO 2" 
print " " 
#ejercicio1 grupo 2
palabra= "parpaaocdeaaaaalleio"
if(palabra[-1]=="o"):
	print "la palabra ", palabra, " termina por o"
else:
	print "la palabra ", palabra, " NO termina por o"
test=1
i=0
for letra in palabra:
	if (palabra[i] == "a" and palabra[i+1]=="s" and palabra[i+2]=="a"):
		print "la palabra", palabra, "contiene la secuencia asa"
		test=0
	i=i+1
if test==1:
	print "la palabra ", palabra, "NO contiene la secuencia asa"


test2=1
j=0
count=0
for letra in palabra:
	if (palabra[j] == "a" ):
		count = count+1
	j=j+1
print "la palabra", palabra, "contiene", count, "veces la letra a"

#ejercicio2 grupo 2

lista=[ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#print lista
lista2=[31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
lista=lista + lista2
print lista

#lista.pop(8)
#print lista
newlenght=len(lista)
k=0
tresocinco=[]


while k < newlenght:
	if (lista[k]>=10 and lista[k]<20):
		lista.pop(k)	
		newlenght=len(lista)
		k=k-1
	if (lista[k]==3 or (lista[k]>=30 and lista[k]<40) or lista[k]==5 or (lista[k]>=50 and lista[k]<60) ): 
		tresocinco.append(lista[k])	

	k+=1

print lista
print tresocinco

