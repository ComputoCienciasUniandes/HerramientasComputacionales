#Para realizar el trabajo primero es necesario crear una lista con N numeros.
N= 100
listanumeros1 = [] 
listanumeros2 = []
listanumeros3 = []
listanumeros4 = []
numerosmultiplosde3 = 0
numerosmultiplosde5 = 0
numerosmultiplosde7 = 0
numerosmultiplosde9 = 0
cantidadnumerosenlista1 =0
cantidadnumerosenlista2 =0
cantidadnumerosenlista3 =0
cantidadnumerosenlista4 =0
print "la lista de numeros divisibles entre 3 es:"

for i in range (0,N):
 if ((i+1)%3==0):
  listanumeros1.append(i+1)
  cantidadnumerosenlista1 = cantidadnumerosenlista1 +1

print listanumeros1
  
print "la sumatoria de estos numeros es:"

for i in range (0,cantidadnumerosenlista1):
 numerosmultiplosde3 =  numerosmultiplosde3 + listanumeros1[i]

print numerosmultiplosde3

print "la lista de numeros divisibles entre 5 es:"

for i in range (0,N):
 if ((i+1)%5==0):
  listanumeros2.append(i+1)
  cantidadnumerosenlista2 = cantidadnumerosenlista2 +1

print listanumeros2
  
print "la sumatoria de estos numeros es:"

for i in range (0,cantidadnumerosenlista2):
 numerosmultiplosde5 =  numerosmultiplosde5 + listanumeros2[i]
print numerosmultiplosde5

print "la lista de numeros divisibles entre 7 es:"

for i in range (0,N):
 if ((i+1)%7==0):
  listanumeros3.append(i+1)
  cantidadnumerosenlista3 = cantidadnumerosenlista3 +1

print listanumeros3
  
print "la sumatoria de estos numeros es:"

for i in range (0,cantidadnumerosenlista3):
 numerosmultiplosde7 =  numerosmultiplosde7 + listanumeros3[i]
print numerosmultiplosde7

print "la lista de numeros divisibles entre 9 es:"

for i in range (0,N):
 if ((i+1)%9==0):
  listanumeros4.append(i+1)
  cantidadnumerosenlista4 = cantidadnumerosenlista4 +1

print listanumeros4
  
print "la sumatoria de estos numeros es:"

for i in range (0,cantidadnumerosenlista4):
 numerosmultiplosde9 =  numerosmultiplosde9 + listanumeros4[i]
print numerosmultiplosde9





