import numpy as np
import sys

x = []
y = []
z = []

r = []
R = float( sys.argv[1] )

while (len(r) == 0 or R > r[len(r)-1]):
    phi = 2*np.pi*np.random.random_sample()
    theta = np.pi*np.random.random_sample()
    if (len(r) != 0):
        x.append( x[len(x)-1] + (np.sin(theta)*np.cos(phi)) )
        y.append( y[len(y)-1] + (np.sin(theta)*np.sin(phi)) )
        z.append( z[len(z)-1] + (np.cos(theta)) )

    if (len(r) == 0):
        x.append(np.sin(theta)*np.cos(phi))
        y.append(np.sin(theta)*np.sin(phi))
        z.append(np.cos(theta))
    r.append(abs( np.sqrt( ((x[len(x)-1])**2) + ((y[len(y)-1])**2) + ((z[len(z)-1])**2)) ))

f = file("marcha-aleatoria.dat", "w")

for i in range(len(x)):
    f.write(str(x[i]) + " " + str(y[i]) + " " + str(z[i]) + " " + str(i+1)  + " " + str(r[i]))
    f.write('\n') 
