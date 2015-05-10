N = 100
suma3 = 0
suma5 = 0
suma7 = 0
suma9 = 0
print "multiplos de 3: "
for i in range( N ):
    a = 3 * ( i + 1 )
    if( a < ( N + 1 ) ):
        suma3 = suma3 + a
        print a
print "suma =", suma3
        
print "multiplos de 5: "
for i in range( N ):
    b = 5 * ( i + 1 )
    if( b < ( N + 1 ) ):
        suma5 = suma5 + b
        print b
print "suma =", suma5

print "multiplos de 7: "
for i in range( N ):
    c = 7 * ( i + 1 )
    if( c < ( N + 1) ):
        suma7 = suma7+ c
        print c
print "suma =", suma7

print "multiplos de 9: "
for i in range( N ):
    d = 9 * ( i + 1 )
    if( d < ( N + 1 ) ):
        suma9 = suma9 + d
        print d
print "suma =", suma9
