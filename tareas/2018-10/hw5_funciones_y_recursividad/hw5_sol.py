# Punto 2
var1 = 'variable 1 global'
var2 = 'variable 2 global'

# Punto 3
def fun1():
    var1 = 'variable 1 local'
    print var1
    
# Punto 4
def fun2(var2):
    print var2
    
# Punto 5

# Por orden
print('------------------------------------------------------------')

# Parte 1
print('Ejecutando fun1()')
fun1() # Solo se ejecuta porque el return es nulo
print('Imprimiendo variable 1')
print var1

# Por orden
print('------------------------------------------------------------')

# Parte 2
print('Ejecutando fun2()')
fun2('variable 2 local') # Solo se ejecuta porque el return es nulo
print('Imprimiendo variable 2')
print var2

# Por orden
print('------------------------------------------------------------')

# Aqui corro el codigo para verificar el alcance de las variables 

# Aqui ya he ejecutado el codigo y he sacado mis conclusiones
print('Conclusion: Hay una version local y una version global de cada variable aunque tengan el mismo nombre.')

# Por orden
print('------------------------------------------------------------')

# Punto 6
def fun3():
    # Primero establecemos que la variable var1 que trabajemos en esta funcion sera la version global, en vez de una version local
    global var1
    var1 = 'variable 1 global modificada'
    print var1
    
print('Ejecutando fun3()')
fun3() # Solo se ejecuta porque el return es nulo
print('Imprimiendo variable 1')
print var1

# Por orden
print('------------------------------------------------------------')

#######################
# PARTE 2 DE LA TAREA #
#######################

# Punto 7

# Esta funcion IMPRIME la secuencia de Collatz asociada a un numero n
def Collatz(n):
    # Caso base
    if n == 1:
        print n
    # Caso recursivo (son dos versiones de la recursi\'on
    else:
        if n%2 == 0:
            print n, # La coma es para que los imprima en un solo renglon
            Collatz(n/2) # Se imprime el numero actual y la secuencia del siguiente
        else:
            print n,
            Collatz(3*n+1) # Se imprime el numero actual y la secuencia del siguiente
            
# Punto 8
for i in range(1,21): # Los numeros del 1 al 20
    print("Imprimiendo la secuencia del :"+str(i))
    Collatz(i) # Solo se llama la funcion ya que esta se encarga de imprimir (el return es nulo)











        
    
    
    
    
    
    
    
    
    
    
    
    




















