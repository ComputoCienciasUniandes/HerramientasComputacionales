l = []
suma3 = 0
N = 100
for i in range (0, N+1):
   if i%3==0:
        l+=[i]
        suma3+=i
        
print "Los multiplos de 3 de 1 hasta " + str(N) + " son:"
print l
print "La suma da:"
print suma3

l = []
suma5 = 0
N = 100
for i in range(0, N+1):
   if i%5==0:
        l+=[i]
        suma5+=i
        
print "Los multiplos de 5 de 1 hasta " + str(N) + " son:"
print l
print "La suma da:"
print suma5


l = []
suma7 = 0
N = 100
for i in range(0, N+1):
   if i%7==0:
        l+=[i]
        suma7+=i
        
print "Los multiplos de 7 de 1 hasta " + str(N) + " son:"
print l
print "La suma da:"
print suma7

l = []
suma9 = 0
N = 100
for i in range(0, N+1):
   if i%9==0:
        l+=[i]
        suma9+=i
        
print "Los multiplos de 9 de 1 hasta " + str(N) + " son:"
print l
print "La suma da:"
print suma9

print "La suma total es:"
print suma3+suma5+suma7+suma9


    


