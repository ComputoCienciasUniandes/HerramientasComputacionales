a=[]
N=100


sumatoria1 = 0

sumatoria2 = 0

sumatoria3 = 0

sumatoria4 = 0


total = 0



z=[]

z1=[]

z2=[]

z3=[]


for i in range (0,N+1):

    a += [i]

for i in range (0,N+1):

    if a[i] % 3 == 0:
     
     z += [a[i]]
     
    sumatoria1 += a[i]

print "los numeros multiplos de 3 de cero hasta"
#print J
print "son"
print a 
print sumatoria1



for i in range (0,N+1):
 
   a += [i]

for i in range (0,N+1):

    if a[i] % 5 == 0:

        z1 += [a[i]]

        sumatoria2 += a[i]


print "los numeros multiplos de 5 de cero hasta"
#print J
print "son"
print a1
print sumatoria2



for i in range (0,N+1):
  
  a += [i]

for i in range (0,N+1):

    if a[i]% 7 == 0:
 
       z2 += [a[i]]

       sumatoria3 += a[i]


print "los numeros multiplos de 7 de cero hasta"
#print J
print "son" 
print a2
print sumatoria3



for i in range (0,N+1):

    a += [i]

for i in range (0,N+1):

     if a[i] % 9 == 0:
       
       z3 += [a[i]]
     

     sumatoria4 += a[i]

print "los numeros multiplos de 3 de cero hasta" 
print a 
print "son"
print a3 
print sumatoria4


print "la suma total es "
print sumatoria1+sumatoria2+sumatoria3+sumatoria4
