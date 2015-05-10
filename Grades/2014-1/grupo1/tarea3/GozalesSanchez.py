cuenta = 0
lista = []
for i in range (input()):
        
        if (i%3 == 0):
                 cuenta = cuenta + i
                 lista = lista + [i]
        elif (i%5 == 0):
                 cuenta = cuenta + i
                 lista = lista + [i]
        elif (i%7 == 0):
                 cuenta = cuenta + i
                 lista = lista + [i]




print cuenta
print lista
