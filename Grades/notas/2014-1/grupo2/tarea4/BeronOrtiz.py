import sys
import numpy

if sys.argv[1]=="Paper":
    n="Paper"
    j = 0
elif sys.argv[1]=="Rock":
    n="Rock"
    j = 1
elif sys.argv [1]=="Scissors":
    n="Scissors"
    j = 2
else:
    j = 3
    print "Usar Paper, Rock y Scissors"

r=numpy.random.randint(0,3)
if r== 0:
    p = "Paper"
elif r==1:
    p = "Rock"
elif r==2:
    p = "Scissors"

if j==0:
    if r==0:
        print "Tie"
        print "Player: " + n
        print "Computer: " + p
    elif r==1:
        print "You won"
        print "Player: " + n
        print "Computer: " + p
    elif r==2:
       print "You loose"
       print "Player: " + n
       print "Computer: " + p
elif  j==1:
    if r==1:
        print "Tie"
        print "Player: " + n
        print "Computer: " + p
    elif r==2:
        print "You won"
        print "Player: " + n
        print "Computer: " + p
    elif r==0:
        print "You loose"
        print "Player: " + n
        print "Computer: " + p

elif  j==2:
    if r==2:
        print "Tie"
        print "Player: " + n
        print "Computer: " + p
    elif r==0:
        print "You won"
        print "Player: " + n
        print "Computer: " + p
    elif r==1:
        print "You loose"
        print "Player: " + n
        print "Computer: " + p
