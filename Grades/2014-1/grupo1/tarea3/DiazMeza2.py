print "Programa de Conteo"
print ""
N=50
a=0
b=0
c=0
d=0
tres=[]
cinco= []
siete=[]
nueve=[]
for i in range(0,N):
    w=i%3
    if w==0:
        a+=i
        tres+=[i]
print "Multiplos de Tres"
print tres

for j in range(0,N):
    x=j%5
    if x==0:
        b+=j
        cinco+=[j]
print "Multiplos de Cinco"
print cinco

for k in range(0,N):
    y=k%7
    if y==0:
        c+=k
        siete+=[k]
print "Multiplos de Siete"
print siete

for l  in range(0,N):
    z=l%9
    if z==0:
        d+=l
        nueve+=[l]
print "Multiplos de Nueve"
print nueve

print ""

print "Suma de los Multiplos de Tres"
print a

print "Suma de los Multiplos de Cinco"
print b

print "Suma de los Multiplos de Siete"
print c

print "Suma de los Multiplos de Nueve"
print d

print "Suma Total"
print a+b+c+d

print ""
        
print "Sergio Diaz 201224162"
