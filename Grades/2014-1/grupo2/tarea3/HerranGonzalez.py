#creo una lista para cada numero
#creo una varible que lleve la cuenta de la suma de cada muliplo
#el modulo de un numero multiplo de otro debe ser igual a 0
#se toman los multiplos de el numero y se suman 
#se agregan a una lista ya creada 
#se imprime la lista y  la suma de los numeros

N=101
sum = 0
s = 0
suma = 0
con = 0
a = []
b = []
c = []
d = []


print "Multiplos de 3:"
for i in range (0,N):

   if i % 3 == 0:
       sum = sum + i
       a.append(i)
print a
print "La suma de los multiplos de 3 es:", sum
print

print "Multiplos de 5:"
for i in range (0,N):
   
   if i % 5 == 0:
       s = s + i
       b.append(i)
print b

print "La suma de los multiplos de 5 es:", s
print

print "Multiplos de 7:"
for i in range (0,N):
   
   if i % 7 == 0:
       suma = suma + i
       c.append(i)
print c

print "La suma de los multiplos de 7 es:", suma
print 

print "Multiplos de 9:"
for i in range (0,N):
   
   if i % 9 == 0:
       con = con + i
       d.append(i)
print d

print "La suma de los multiplos de 9 es:", con
print
