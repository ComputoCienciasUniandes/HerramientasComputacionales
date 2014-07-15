N = 10
i = 0
j = 0
k = 0
l = 0
m = 0
x = 0

r = []
while i<=N: 
    s = i%3
    if s==0:
        n = [i]
        r = r + n
        i+=1
        m+=1
    else :
        i+=1
while j<=N: 
    t =j%5
    if t==0:
        n = [j]
        r = r + n
        j+=1 
        m+=1
    else :
        j+=1

while k<=N:    
    u = k%7
    if u==0:
        n = [k]
        r = r+n
        k+=1
        m+=1
    else:
        k+=1

while l<=N:
    w = l%9
    if w==0:
        n = [l]
        r = r+n
        l+=1
        m+=1
    else:
        l+=1
for p in range(0,m):
    b = r[p]
    x = x + b
        
print r
print x
