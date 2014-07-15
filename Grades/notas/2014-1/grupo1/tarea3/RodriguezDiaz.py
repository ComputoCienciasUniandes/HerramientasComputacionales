J=[]
N=100
Suma1 = 0
Suma2 = 0
Suma3 = 0
Suma4 = 0
total = 0

a=[]
a1=[]
a2=[]
a3=[]
for i in range (0,N+1):
    J+=[i]
for i in range (0,N+1):
    if J[i]%3==0:
        a+=[J[i]]
        Suma1+=J[i]
print "los numeros multiplos de 3 de cero hasta"
print J
print "son"
print a
print Suma1

for i in range (0,N+1):
    J+=[i]
for i in range (0,N+1):
    if J[i]%5==0:
        a1+=[J[i]]
        Suma2+=J[i]
print "los numeros multiplos de 5 de cero hasta"
print J
print "son"
print a1
print Suma2

for i in range (0,N+1):
    J+=[i]
for i in range (0,N+1):
    if J[i]%7==0:
        a2+=[J[i]]
        Suma3+=J[i]
print "los numeros multiplos de 7 de cero hasta"
print J
print "son"
print a2
print Suma3

for i in range (0,N+1):
    J+=[i]
for i in range (0,N+1):
    if J[i]%9==0:
        a3+=[J[i]]
        Suma4+=J[i]
print "los numeros multiplos de 3 de cero hasta"
print J
print "son"
print a3
print Suma4

print "la suma total es "
print Suma1+Suma2+Suma3+Suma4
