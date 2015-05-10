import matplotlib.pyplot as mt
iterations = []
roots = []
x = 0
print "Compute el numero del que desea sacar raiz"
N = input()
xmax = N
xmin = 0
counter = 0
print "Ingrese la raiz que desea sacar"
raiz = input()
while (abs(x**raiz - N) > 0.000001):
   # x = (xmax+xmin)/2.0
    counter= counter +1
    if((x**raiz - N) <0 and (xmax**raiz -N)  >0):
        xmin = x
    elif(x**raiz>0 and xmax**raiz>0):
        xmax = x
    x= (xmax+xmin)/2.0
    roots = roots + [x]
    iterations = iterations + [counter]

mt.scatter(iterations,roots)
mt.ylabel("Raiz calculada", fontsize=20)
mt.xlabel("Iteraciones", fontsize=20)
mt.title ("Raiz calculada contra numero de iteraciones")
mt.show()

print "El numero de iteraciones es:"
print counter
print "La raiz es:"
print x 
    
