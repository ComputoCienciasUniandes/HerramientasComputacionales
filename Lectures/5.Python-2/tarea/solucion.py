import numpy as np
import sys

def number_to_name(number):
   if number == 0:
        name = "Rock"
        return name
   elif number == 1:
        name = 'Paper'
        return name
   elif number == 2:
        name = 'Scissors'
        return name


    
def name_to_number(name):
    if name == "rock":
        number = 0
        return number 
    elif name == 'paper':
        number = 1
        return number
    elif name == 'scissors':
        number = 2
        return number
    else:
        print 'Please choose between: rock, paper, scissors in order to start the game'



def rpsls(name): 
    # convert name to player_number using name_to_number
    
    player_number = name_to_number(name)
       
    # compute random guess for comp_number using random.randrange()
    
    comp_number = np.random.randint(0, 3)
    
    # compute difference of player_number and comp_number modulo five
    
    key = (player_number - comp_number)%3
   
    # use if/elif/else to determine winner
    if key == 0:
        winner = 'Player and computer tie!'
        print '     '
        print winner
    elif key <= 1:
        winner = number_to_name(player_number)
        print '     '
        print 'Player wins'
    elif key >= 2:
        winner = number_to_name(comp_number)
        print '        '
        print 'Computer wins'
    else:
        print 'whats going on?'
    
    print "Player choose:" 
    print number_to_name(player_number)
    print "Computer choose:"
    print number_to_name(comp_number)
  
   

    
    # test your code
rpsls(sys.argv[1])

