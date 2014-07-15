# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%pylab inline

#por si es deseado cambiar el N, corresponde a la tercera posicion de la siguiente funcion.

lasfrac = []
def fracc(M,N):
    cara =[]
    sello =[]
    
    for i in range(M):
        caras=0.0
        for j in range (N):
            a=np.random.randint(2)
            if(a==1):
               caras=caras+1
              
        cara.append(caras)
        lasfrac.append(caras/N)
        sellos=N-caras       
        sello.append(sellos)
        
    return cara, sello
fracc(100,100)

hist(lasfrac, bins=20)
xlabel('fraccion')
ylabel('lanzamientos')
axvline(0.5+0.015617, c='y', linewidth=2.5)
axvline(0.5-0.015617, c ='y', linewidth=2.5)
axvline(0.5+2*0.015617, c='r', linewidth=2.5)
axvline(0.5-2*0.015617, c ='r', linewidth=2.5)
axvline(0.5+3*0.015617, c='g', linewidth=2.5)
axvline(0.5-3*0.015617, c ='g', linewidth=2.5)




                
   



# <codecell>

#0.1 corresponde al intervalo de confianza σ5, 0.35 en σ4, 0.4 en σ3, 1.7 en σ23.

# <codecell>


#Valor promedio de cara y sellos
xs=[]
lanz=[]
i=1000
while i<=20000:
    x , y = fracc(i , 1000)
    promca= mean(x)
    promse= mean(y)
    y = abs(promca - promse)
    xs.append(y)
    lanz.append(i)
    i+=1000

    
print xs

scatter(lanz,xs)
xlabel('lanzamientos')
ylabel('Valor absoluto')

# <codecell>

xs=[]
lanz=[]
i=1000
while i<=20000:
    x , y = fracc(i , 1000)
    promca= mean(x)
    promse= mean(y)
    y = abs(promca / promse)
    xs.append(y)
    lanz.append(i)
    i+=1000

    
print xs

scatter(lanz,xs)
xlabel('lanzamientos')
ylabel('Razon')

# <codecell>

xs=[]
lanz=[]
i=1000
while i<=20000:
    x , y = fracc(i , 1000)
    promca= mean(x)
    promse= mean(y)
    y = abs(promca - promse)
    xs.append(y)
    lanz.append(i)
    i+=1000

    
print xs

scatter(lanz,xs)
xlabel('lanzamientos')
ylabel('Valor absoluto')
xscale("log")
yscale("log")

# <codecell>

xs=[]
lanz=[]
i=1000
while i<=20000:
    x , y = fracc(i , 1000)
    promca= mean(x)
    promse= mean(y)
    y = abs(promca / promse)
    xs.append(y)
    lanz.append(i)
    i+=1000

    
print xs

scatter(lanz,xs)
xlabel('lanzamientos')
ylabel('Razon')
xscale("log")
yscale("log")

# <codecell>


# <codecell>


