n = 100
l = []
tres = []
cinco = []
siete = []
nueve = []
i = 0
j = 0
k = 0
m = 0
p = 0

#creacion de la lista con todos los numeros
while i<=n:    
    l.append(i)
    i+=1
#proceso para multiplos de 3    
while j<=n:
    x = l[j]
    if x%3==0:
        tres.append(x)
        
    j+=1
print "Los multiplos de 3 son:"
print tres
print "La suma de los multiplos de 3 es:"
print sum(tres)

#proceso para multiplos de 5
while k<=n:
    x = l[k]
    if x%5==0:
        cinco.append(x)
        
    k+=1
print "Los multiplos de 5 son:"
print cinco
print "La suma de los multiplos de 5 es:"
print sum(cinco)

#proceso para multiplos de 7
while m<=n:
    x = l[m]
    if x%7==0:
        siete.append(x)
        
    m+=1
print "Los multiplos de 7 son:"
print siete
print "La suma de los multiplos de 7 es:"
print sum(siete) 

#proceso para multiplos de 9
while p<=n:
    x = l[p]
    if x%9==0:
       nueve.append(x)
        
    p+=1
print "Los multiplos de 9 son:"
print nueve
print "La suma de los multiplos de 9 es:"
print sum(nueve)       
        
    
    
