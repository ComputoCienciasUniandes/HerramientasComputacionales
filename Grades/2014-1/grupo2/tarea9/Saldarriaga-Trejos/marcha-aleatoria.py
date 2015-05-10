import numpy as np
import sys

R=float(sys.argv[1])
x=[]
y=[]
z=[]
r=[]
pasos=[]


t=0
v=0
w=0
rad=0

i=1
radio=0
while (rad<=R):
    pasos.append(i)
    ang= np.random.rand()
    angulo= np.random.rand()
    theta=2*(np.pi)*ang
    phi=(np.pi)*angulo
    t= np.sin(theta)*(np.sin(phi))
    v= np.sin(theta)*(np.cos(phi))
    w= np.cos(theta)
    radio=np.sqrt((t**2)+(v**2)+(w**2))
    x.append(t)
    y.append(v)
    z.append(w)
    r.append(radio)
    rad+=radio
    i+=1

f =open("marcha-aleatoria.dat","w")
for j in range(len(x)):
    f.write(str(x[j])+" "+ str(y[j])+" "+str(z[j])+" "+str(r[j])+" "+str(pasos[j])+"\n")
f.close

    
