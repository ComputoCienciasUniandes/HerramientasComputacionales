# 1.
a = 7.0
print('El numero es', a)

# 2.
if a%2 == 0: 
	print('El numero', a, 'es par')
else:
	print('El numero', a, 'es impar')

# 3
print('Los divisores de', a, 'son: ')
i = 1.0
while(i <= a):
	if(a%i == 0):
		print(i)
	i = i+1

# 4.
b = 24.0

i = 1.0
mcd = 1.0
while(i<=min(a,b)):
	if(a%i == 0 and b%i == 0 and i>mcd):
		mcd = i
	i = i + 1
	
print('El maximo comun divisor entre ', a, ' y ', b, 'es ', mcd)
