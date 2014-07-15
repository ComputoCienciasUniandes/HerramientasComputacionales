import pylab as py
import sys
import math
import numpy as np

archivo=sys.argv[1]
data=np.loadtxt(archivo)

x=data[:,3]
y=data[:,4]



fit = py.polyfit(x, y, 1)


py.plot(x, x*fit[0] + fit[1], linewidth='2.0', label=str(fit[0]) +'x' + '('+ str(fit[1]) + ')')
py.plot(x, y, linewidth=2.0, c='r', label="Real")
py.scatter(x, y, c='k', alpha=0.7)
py.legend(loc='best')
py.xlabel("$\mathrm{Numero\ Pasos}$", fontsize=25)
py.ylabel("$\mathrm{Radios}$", fontsize=25)
py.title("$\mathrm{Recorrido\ Foton}$", fontsize=25)
py.savefig('ajuste.png')

py.show()
