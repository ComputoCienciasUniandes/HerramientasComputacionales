class Particula(object):
	"esta partacula se mueve con el metodo de euler tambien"
	def __init__(self, q, M, x0, y0, Vx0, Vy0):
		self.e=q
		self.m=M
		self.x=x0
		self.y=y0
		self.Vx=Vx0
		self.Vy=Vy0

	def calcularFuerzaX(self,Bz, Ex):
		self.Fx=self.e*self.Vy*Bz + self.e*Ex
	
	def calcularFuerzaY(self,Bz,Ey):
		self.Fy=-self.e*self.Vx*Bz + self.e*Ey
	
	def muevete(self, dt):

		self.x+=self.Vx*dt
		self.y+=self.Vy*dt

		self.Vx+=self.Fx*dt/self.m
		self.Vy+=self.Fy*dt/self.m
	def imprime(self):
		print self.x, self.y

'''
#forma mas capa de imprimir las cosas
	
	def __str__(self):
		return "%f %f" % (self.x, self.y)
'''

B=10
Ex=5
Ey=5
q=-1
M=1
Vx0=0.0
Vy0=5.0
x0=2.0
y0=0.0

timothy=Particula(q, M, x0, y0, Vx0, Vy0)
timothy.calcularFuerzaX(B,Ex)
timothy.calcularFuerzaY(B,Ey)	
t=0.0
Deltat=0.0005
while t<10.0:
	timothy.muevete(Deltat)
	#print t, timothy #con la forma capa de imprimir
	timothy.imprime()
	t+=Deltat
	timothy.calcularFuerzaX(B,Ex)
	timothy.calcularFuerzaY(B,Ey)



