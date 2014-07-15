n = 100
a = 0
l = []
while a<=n:
    b = [a]
    l= l + b
    a += 1
print l[:]

suma3 = 0
l3 = []
print "multiplos de 3"
for i in range(n+1):
    if l[i] != 0:
        if l[i]%3 == 0:
            suma3 += l[i]
            b = [i]
            l3 += b
print l3
print suma3

suma5 = 0
l5 = []
print "multiplos de 5"
for i in range(n+1):
    if l[i]%5 == 0:
        if l[i] != 0:
            suma5 += l[i]
            b = [i]
            l5 += b
print l5
print suma5

suma7 = 0
l7 = []
print "multiplos de 7"
for i in range(n+1):
    if l[i] != 0:
        if l[i]%7 == 0:
            if l[i] != 0:
                suma7 += l[i]
                b = [i]
                l7 += b
print l7
print suma7

suma9 = 0
l9 = []
print "multiplos de 9"
for i in range(n+1):
    if l[i] != 0:
        if l[i]%9 == 0:
            if l[i] != 0:
                suma9 += l[i]
                b = [i]
                l9 += b
print l9
print suma9
