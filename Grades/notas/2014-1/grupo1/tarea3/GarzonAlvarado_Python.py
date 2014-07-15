n=100
print "     "
print 'Con n igual a: '+ repr(n)
lista3=[]
lista5=[]
lista7=[]
lista9=[]
e=int

#metodo primos de 3
print "Lista numeros primos de 3"
for i in range (1,n):
    nume=i
    x=i%3
    if(x==0):
        e=[nume]
        lista3+= e
print lista3
a= sum(lista3)

#metodo primos de 5
print "Lista numeros primos de 5"
for i in range (1,n):
    nume=i
    x=i%5
    if(x==0):
        e=[nume]
        lista5 += e
print lista5
b= sum(lista5)

#metodo primos de 7
print "Lista numeros primos de 7"
for i in range (1,n):
    nume=i
    x=i%7
    if(x==0):
        e=[nume]
        lista7+= e
print lista7
c= sum(lista7)

#metodo primos de 9
print "Lista numeros primos de 9"
for i in range (1,n):
    nume=i
    x=i%9
    if(x==0):
        e=[nume]
        lista9+= e
print lista9
d= sum(lista9)

#metodo suma de todos los numeros primos encontrados

suma= a+b+c+d

#metodo mensaje final

print 'La suma de los numeros primos de 3,5,7 y 9 entre 0 y el numero ingresado ' + repr(n) + ' es:'
print suma


