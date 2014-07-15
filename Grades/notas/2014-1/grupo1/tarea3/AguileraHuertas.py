a=3
b=5
c=7
d=9
N=10
lista1=[]
lista2=[]
lista3=[]
lista4=[]

for i in range(0, N+1):
    if i%a==0:
        lista1+=[i]
    if i%b==0:
        lista2+=[i]
    if i%c==0:
        lista3+=[i]
    if i%d==0:
          lista4+=[i]

s=0
s=sum(lista1)+sum(lista2)+sum(lista3)+sum(lista4)

print "Los multiplos de 3 son:"
print lista1
print "Los multiplos de 5 son:"
print lista2
print "Los multiplos de 7 son:"
print lista3
print "Los multiplos de 9 son:"
print lista4
print "La suma de todos los multiplos es:"
print s



