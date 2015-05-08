N = 100 
z = []
x = []
y = []
w = []

s = 0
l = 0
m = 0
o = 0
e = 0

for i in range (0 , N): 
    if (i%3)==0:
        z+=[i]
        s+=i
print "multiplos del 3"
print z
print "suma multiplos del 3"
print s


for g in range (0 , N): 
    if (g%5)==0:
        x+=[g]
        l+=g
print "multiplos del 5"
print x
print "suma multiplos del 5"
print l


for r in range (0 , N): 
    if (r%7)==0:
        x+=[r]
        m+=r
print "multipiplos del 7"
print x
print "suma multiplos del 7"
print m


for p in range (0 , N): 
    if (p%9)==0:
        w+=[p]
        o+=p
print "multiplos del 9"
print w
print "suma multiplos del 9"
print o

e = s + l + m + o 

print "SUMA TOTAL"
print e 

print "Alejandro Rodriguez  201214840"




