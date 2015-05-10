#Inicializo las variables y la lista resultado
n = 30
y = []
v = 0

#Un ciclo que compara los primeros n numeros naturales para saber si son         multiplos y si los son se agregan a la lista resultado
for i in range(n):
   comp3 = (i+1)%3
   comp5 = (i+1)%5
   comp7 = (i+1)%7
   comp9 = (i+1)%9
   z = [i+1]
   if comp3 == 0:
       y = y + z
   elif comp5 == 0:
       y = y + z
   elif comp7 == 0:
       y = y + z
   elif comp9 == 0:
       y = y + z

#Muestra la lista con los numeros multiplos de 3, 5, 7 y 9 en los primeros n numeros naturales
print "Los multiplos de los numeros (3,5,7,9) que hay en los primeros", n, "numeros naturales son:"
print y

#Ciclo que suma todos los numeros de la lista y
k = len(y)
for i in range(k):
   v = v + y[i]

#Muestra la suma de los numeros multiplos de 3, 5, 7 y 9 en los primeros n numeros naturales
print "Y su suma es:"
print v
