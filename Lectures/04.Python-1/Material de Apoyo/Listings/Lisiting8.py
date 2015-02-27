x = "Existen %d tipos de personas" % 10
binario = "binario"
no = "no"
y = "Aquellas que saben %s y aquellos que %s." % (binario, no)

print x
print y

print "Yo dije %r." % x
print "I tambien dije: '%s'." % y

chistoso = False
evaluacion_chiste = "Isn't that joke so funny?! %r"

print evaluacion_chiste % chistoso

w = "Esta es la parte izquierda de..."
e = "un string con esta parte a la derecha."

print w + e