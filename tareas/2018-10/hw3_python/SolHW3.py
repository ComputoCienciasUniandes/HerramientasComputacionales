#1a
fpast=1
fpres=1
fnew=0
#1b
while(fpres<10000):
	fnew=fpast+fpres
	fpast=fpres
	fpres=fnew
print("el minimo valor de cuatro digitos en la secuencia de fibonacci es",fpres)

#2a
d=21
m=1
a=2002
MCD=0
MCM=0
Min=0


#2b
x=fpres
y=a*d*m
if(x>y):
	Min=y
else:
	Min=x
#print(Min,x,y)

#2c
i=1
while(i<Min):
	if (x%i==0) & (y%i==0):
		MCD=i
	i+=1
print("el maximo comun divisor es",MCD)

#2d
MCM=x*y/MCD
print("el minimo comun multiplo es",MCM)
