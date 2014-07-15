suma3 = []
suma5 = []
suma7 = []
suma9 = []
y = int
sumatotal3 = 0
sumatotal5 = 0
sumatotal7 = 0
sumatotal9 = 0


n=100
 
for i in range (0,n):
    num = i
    if i%3==0:
        y=[num]
        
        suma3 += y
        sumatotal3 +=num

for i in range (0,n):
    num = i
    if i%5==0:
        y=[num]
        
        suma5 += y
        sumatotal5 +=num

for i in range (0,n):
    num = i
    if i%7==0:
        y=[num]
        
        suma7 += y
        sumatotal7 +=num

for i in range (0,n):
    num = i
    if i%9==0:
        y=[num]
        
        suma9 += y
        sumatotal9 +=num

print "los multiplos de 3 son:", suma3, "la sumatoria de los multiplos de 3 es:", sumatotal3

print "los multiplos de 5 son:", suma5, "la sumatoria de los multiplos de 5 es:", sumatotal5

print "los multiplos de 7 son:", suma7, "la sumatoria de los multiplos de 7 es:", sumatotal7

print "los multiplos de 9 son:", suma9, "la sumatoria de los multiplos de 9 es:", sumatotal9
