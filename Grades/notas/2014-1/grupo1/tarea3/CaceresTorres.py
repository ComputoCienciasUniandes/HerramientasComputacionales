suma3 = []
suma5 = []
suma7 = []
suma9 = []
lc =int
sumaT3 = 0
sumaT5 = 0
sumaT7 = 0
sumaT9 = 0

n=500


for i in range (0,n):
    numero = i
    if i%3==0:
       lc=[numero]
    
       suma3 += lc
       sumaT3 +=numero
print "Los Multiplos del Numero 3 Son:" , suma3 , "La Suma Total de los Multiplos de 3 es:" , sumaT3



for i in range (0,n):
    numero = i
    if i%5==0:
        lc=[numero]
        
        suma5 += lc
        sumaT5 +=numero
print "Los Multiplos del NUmero 5 son:" , suma5 , "La Suma Total de los Multiplos de 5 es:" , sumaT5




for i in range (0,n):
     numero = i
     if i%7==0:
      lc=[numero]

      suma7 += lc
      sumaT7 +=numero 
print "Los Multiplos del Numero 7 son:" , suma7 , "La Suma Total de los Multiplos de 7 es:" , sumaT7



for i in range (0,n):
    numero = i
    if i%9==0:
        lc=[numero]
        
        suma9 += lc
        sumaT9 +=numero
print "Los Multiplos del Numero 9 son:" , suma9 , "La suma Total de los Multiplos de 9 es:"  ,  sumaT9 






