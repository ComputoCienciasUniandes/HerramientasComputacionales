# Punto 1
def sumatoria(n):
	if n == 1:
		return 1
	else:
		return n+sumatoria(n-1)

print(sumatoria(100))

# Punto 2. La entrada debe ser un numero natural
def suma_cifras(n):
	if n < 10:
		return n
	else:
		return n%10+suma_cifras(n//10)

n = 8
print('El input es', n)	
print(suma_cifras(n))
