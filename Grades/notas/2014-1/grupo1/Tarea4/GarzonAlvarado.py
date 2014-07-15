import sys
import random
#Inicializar armas de los jugadores
jugador= ''
computador= ''
# Variable random arma del computador
z=4
#Contantes de las armas
pi='piedra'
pap='papel'
tij='tijera'
# Variable que detiene el programa si existe un error de escritura, 0 permite que el programa corra 1 lo detiene.
ok=0

#Seleccion de arma usuario

if sys.argv[1]==pi:
    jugador=pi
elif sys.argv[1]==pap:
    jugador=pap
elif sys.argv[1]==tij:
    jugador=tij
else:
    print 'Ha cometido un error de escritura, intente de nuevo'
    ok=1


#Seleccion de arma computador
if ok==0:
    z=random.randrange(3)

    if z==0:
        computador=pi
    elif z==1:
        computador=tij
    elif z==2:
        computador=pap

#Mensaje que refleja las armas escogidas

    print 'El usuario escogio : '+jugador
    print 'El computador escogio : '+computador

#Metodo que define el ganador

    if computador==jugador:
        print 'LOS JUGADORES EMPATAN'
    elif (computador==pi and jugador==pap):
        print 'USUARIO GANA'
    elif (computador==pi and jugador==tij):
        print 'COMPUTADOR GANA.'
    elif (computador==pap and jugador==tij):
        print 'USUARIO GANA'
    elif computador==pap and jugador==pi:
        print 'COMPUTADOR GANA'
    elif computador==tij and jugador==pi:
        print 'USUARIO GANA'
    elif computador==tij and jugador==pap:
        print 'COMPUTADOR GANA'


