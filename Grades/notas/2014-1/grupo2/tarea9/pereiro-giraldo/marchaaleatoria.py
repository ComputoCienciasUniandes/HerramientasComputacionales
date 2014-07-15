import numpy as np 
import sys

x=[0]
y=[0]
z=[0]

r=[0]

R= int(sys.argv[1])

while (r[len(r)- 1] < R):
      a=(np.pi)*np.random.random_sample()
      b=(2*np.pi)*np.random.random_sample()

      x.append(np.sin(a)*np.cos(b)+x[len(x)-1])
      y.append(np.sin(a)*np.sin(b)+y[len(y)- 1])
      z.append(np.cos(a)+z[len(z)-1])

      r.append(np.sqrt((x[len(x)-1])**2 + (y[len(y)-1])**2 + (z[len(z)-1])**2))


f=open("marcha-aleatoria.dat", "w")
for i in range(len(x)-1):
    f.write(str(x[i]) + " " + str(y[i]) + " " + str(z[i]) + " " + str(i) + " " + str(r[i]) + "\n")
f.close
