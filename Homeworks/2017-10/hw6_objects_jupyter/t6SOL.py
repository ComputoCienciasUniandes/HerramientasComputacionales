
# Este comando importa matplotlib y numpy, permitiendo visualizar las graficas en la misma ventana del notebook
import numpy as np
import matplotlib.pyplot as plt


class Pendulo:
    g = 9.8
    def __init__(self, x0, v0, l0):
        self.x = x0
        self.v = v0
        self.l = l0
        
        self.T = []
        self.X = []
        self.V = []
        
        self.T.append(0)
        self.X.append(x0)
        self.V.append(v0)

    def calculaAceleracion(self):
        self.a = -Pendulo.g*self.x/self.l
    def muevete(self, dt):
        self.v += self.a*dt
        self.x += self.v*dt
    def guarda(self, t):
        self.T.append(t)
        self.X.append(self.x)
        self.V.append(self.v)

pendulo1 = Pendulo(1.0, 1.0, 3.0)
t = 0.0
Deltat = 0.001
pendulo1.calculaAceleracion()
while t < 12:
    pendulo1.guarda(t)
    pendulo1.muevete(Deltat)
    pendulo1.calculaAceleracion()
    t+=Deltat

plt.plot(pendulo1.T, pendulo1.V)
plt.show()


