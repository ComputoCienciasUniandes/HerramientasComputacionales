print "Tarea python"
import numpy as np

N=30

tres=[]
cinco=[]
siete=[]
nueve=[]

print tres 

for i in range (N+1):
    tr=3*i
    cin=5*i
    sie=7*i
    nue=9*i

    if(tr<=N):
        tres.append(tr)
    if(cin<=N):
        cinco.append(cin)
    if(sie<=N):
        siete.append(sie)
    if(nue<=N):
        nueve.append(nue)

print "multiplos de tres hasta",str(N),"\n",tres 
print "multiplos de cinco hasta",str(N),"\n",cinco
print "multiplos de siete hasta",str(N),"\n",siete
print "multiplos de nueve hasta",str(N),"\n",nueve
t3=len(tres)

for i in range (t3-len(cinco)):
    cinco.append(0)
for i in range (t3-len(siete)):
    siete.append(0)
for i in range (t3-len(nueve)):
    nueve.append(0)

a=len(tres)

b=0
for i in range (a):
    b=b+(tres[i]+cinco[i]+siete[i]+nueve[i])
print "suma de los multiplos de 3, 5, 7 y 9 hasta el numero", str(N),"\n",b
