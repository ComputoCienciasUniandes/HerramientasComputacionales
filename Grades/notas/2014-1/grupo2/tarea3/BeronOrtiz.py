N = 100
# Lista de numero desl 1 al 100
l = []
for i in range (1, N+1):
    l += [i]
# lista de numeros multiplos de 3
s=[]

# lista de multiplos de 5
u=[]

#lista de multiplos de 7
v=[]

# lista de multiplos de 9
t= []

for i in range (0, N):
    if l[i]%3 == 0:
        s += [l[i]]
    if l[i]%5 == 0:
        u += [l[i]]
    if l[i]%7 == 0:
        v += [l[i]]
    if l[i]%9 == 0:
        t += [l[i]]
a= sum (s)
b= sum (u)
c = sum (v)
d = sum (t)

print "Los multiplos de 3 son:"
print s
print "la suma es:"
print a

print "los multiplos de 5 son:"
print u
print "la suma es:"
print b

print "Los multiplos de 7 son:"
print v
print "La suma es:"
print c

print "Los multiplos de 9 son:"
print t
print "la suma es:"
print d
