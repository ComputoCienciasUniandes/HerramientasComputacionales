N=100

lista1= []
i=1
while i< N:
           z=i%3 
           if z==0:
                  print i
                  lista1.append(i)
           i+=1  
print  sum(lista1)   

lista2= []
i=1
while i< N:
           c=i%5
           if c==0:
                  print i
                  lista2.append(i)
           i+=1  
print  sum(lista2)           

lista3= []
i=1
while i< N:
           d=i%7
           if d==0:
                  print i
                  lista3.append(i)
           i+=1  
print  sum(lista3)
          
lista4= []
i=1
while i< N:
           e=i%9
           if e==0:
                  print i
                  lista4.append(i)
           i+=1  
print  sum(lista4)      
     
