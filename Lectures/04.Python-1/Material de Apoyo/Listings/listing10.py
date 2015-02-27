from sys import argv

script, filename = argv

txt = open(filename)

print "Aqui esta su archivo %r:" % filename
print txt.read()

print "Escribirlo otra vez:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()