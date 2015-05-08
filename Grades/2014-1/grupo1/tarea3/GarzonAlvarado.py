n=100
print "     "
print 'Con n igual a: '+ repr(n)
lista3=[]
lista5=[]
lista7=[]
lista9=[]
#metodo primos de 3
print "Lista numeros primos de 3"
for i in range (1,n):
    x=i%3
    if(x==0):
        lista3.append(i)
print lista3
a= sum(lista3)
#metodo primos de 5
print "Lista numeros primos de 5"
for i in range (1,n):
    x=i%5
    if(x==0):
        lista5.append(i)
print lista5
b= sum(lista5)
#metodo primos de 7
print "Lista numeros primos de 7"
for i in range (1,n):
    x=i%7
    if(x==0):
        lista7.append(i)
print lista7
c= sum(lista7)
#metodo primos de 9
print "Lista numeros primos de 9"
for i in range (1,n):
    x=i%9
    if(x==0):
        lista9.append(i)
print lista9
d= sum(lista9)
#metodo suma de elementos de lista
e= a+b+c+d
print 'La suma de los numeros primos de 3,5,7 y 9 entre 0 y el numero ingresado ' + repr(n) + ' es:'
print e


