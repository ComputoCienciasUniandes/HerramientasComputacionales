l=[]
N=100
suma1=0
suma2=0
suma3=0 
suma4=0
sumatotal=0
b=[]
b1=[]
b2=[]
b3=[]
for i in range (0,N+1):
    l+=[i]
for i in range(0,N+1):
    if l[i]%3==0:
        b+=[l[i]]
        suma1+=l[i]
print "los multiplos de 3 de 0 hasta"
print N
print "son"
print b
print suma1
for i in range(0,N+1):
    if l[i]%5==0:
        b1+=[l[i]]
        suma2+=l[i]
print "los multiplos de 5 de 0 hasta"
print N
print "son"
print b1
print suma2
for i in range(0,N+1):
    if l[i]%7==0:
        b2+=[l[i]]
        suma3+=l[i]
print "los multiplos de 7 de 0 hasta "
print N 
print "son:"
print b2
print suma3
for i in range(0,N+1):
    if l[i]%9==0:
        b3+=[l[i]]
        suma4+=l[i]
print "los multiplos de 9 de 0 hasta"
print N
print "son"
print b3
print suma4
print "la suma total es " 
print suma1+suma2+suma3+suma4
