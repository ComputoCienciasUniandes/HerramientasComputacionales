

n=10
i=0
respuesta =[]
respuesta2 =0
h=[1]

while i<n:
  j=[i]
  b=[i%3]
  c=[i%5]
  d=[i%7]
  e=[i%9]
  if(b[0]==0): 
   respuesta = respuesta + j
   respuesta2 = respuesta2 + i
  
  if(c[0]==0):
   respuesta = respuesta + j
   respuesta2 = respuesta2 + i 

  if(d[0]==0):
   respuesta = respuesta + j
   respuesta2 = respuesta2 + i

  if(e[0]==0):
   respuesta = respuesta + j
   respuesta2 = respuesta2 + i 

  i=i+1


print "Los multiplos de (3,5,7,9) que se encuentran entre 0 y " + str(n) + " Son: " + str (respuesta)
print
print "La suma de estos numeros es: " + str(respuesta2)
