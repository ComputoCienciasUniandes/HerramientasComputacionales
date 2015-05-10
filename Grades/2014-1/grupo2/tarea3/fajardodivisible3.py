x=1
y=0

while x<100:
    if (x%3==0)|(x%5==0)|(x%5==0)|(x%7==0):
        print "Este es multiplo " + str(x)
    x=x+1
    y=x+y
    
else:
    x=x+1
print "La suma de multiplos es " + str(y)        

