N=50
b=[]
s=0
b1=[]
s1=0
b2=[]
s2=0
b3=[]
s3=0

for i in range(0,N+1):
    if i%3==0:
        b+=[i]
        s=sum(b)
print "Los multiplos de 3 son:"
print b
print "La suma de los multiplos de 3 es:"
print s

for i in range(0,N+1):
    if i%5==0:
        b1+=[i]
        s1=sum(b1)
print "Los multiplos de 5 son:"
print b1
print "La suma de los multiplos de 5 es:"
print s1

for i in range(0,N+1):
    if i%7==0:
        b2+=[i]
        s2=sum(b2)
print "Los multiplos de 7 son:"
print b2
print "La suma de los multiplos de 7 es:"
print s2

for i in range(0,N+1):
    if i%9==0:
        b3+=[i]
        s3=sum(b3)
print "Los multiplos de 9 son:"
print b3
print "La suma de los multiplos de 9 es:"
print s3

print "La suma de todos los multiplos es:"
print s+s1+s2+s3


