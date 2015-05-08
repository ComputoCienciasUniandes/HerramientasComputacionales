#tarea
x=1
#lista hasta y o (n)
l=[x]
#lista de multiplos de 3
s=[]
#lista de multiplos de 5
t=[]
#lista de multiplos de 7
r=[]
#suma multiplos de 3
a=0
#suma multiplos de 5
b=0
#suma multiplos de 7
c=0

y=100
#multiplos
v=3
w=5
z=7

while x<y:
    x+=1
    l+=[x]

for i in range(0,y):
    if l[i]%v==0:
        s+=[i+1]
        a+=i+1
        i+=1
       
    else:
        i+=1
#suma mas simple
a=sum(s)

for i in range(0,y):
    if l[i]%w==0:
        t+=[i+1]
        b+=i+1
        i+=1

    else:
        i+=1
#suma mas simple
b=sum(t)

for i in range(0,y):
    if l[i]%z==0:
        r+=[i+1]
        c+=i+1
        i+=1
    else:
        i+=1
#suma mas simple
c=sum(r)
        
print "la lista de 1 a 100 es:"  
print l
print "los multiplos de 3 son:"  
print s
print "La suma es: "
print a
print "los multiplos de 5 son:"
print t
print "La suma es: "
print b
print"los multiplos de 7 son:"
print r
print "La suma es: "
print c
