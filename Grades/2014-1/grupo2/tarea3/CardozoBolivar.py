#Description : Este programa, calcula todos los números divisibles por 3 desde 1 hasta n
#__author__ = 'David Cardozo'
#__email__ = 'gd.cardozo684@uniandes.edu.co'

import sys
if sys.version_info <= (3, 0):
    sys.stdout.write('Perdón, se requiere de Python 3.x, no Python 2.x para ejecutar este programa\n')
    sys.exit(1)

a_list = []

for x in range(0, 100):
    if x % 3 == 0:
        print(x, 'es divisible 3')
        a_list.extend([x])
    else:
        print(x, 'no es divisible 3')

print(a_list)
