N = 50
a = []
b = []
c = []
q = 0
w = 0
e = 0
for i in range(1, N):
    x= i%3
    if x==0:
        q+=i
        a+=[i]

print "la lista de numeros multiplos de 3 de 0 a 50 y su suma son", a , q

for i in range(1, N):
    x= i%5
    if x==0:
        w+=i
        b+=[i]

print "la lista de numeros multiplos de 5 de 0 a 50 y su suma son:", b,w

for i in range(1, N):
    x= i%7
    if x==0:
        e+=i
        c+=[i]

print "la lista de numeros multiplos de 7 de 0 a 50 y su suma son:", c,e
