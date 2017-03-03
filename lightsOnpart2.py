# Assignment 5
# David Ciupei
# October 1, 2013

import time # provides time.sleep(0.5)
from random import * # provides choice( [0,1] ), etc.
import sys  # larger recursive stack
from csplot import * 
sys.setrecursionlimit(30000) # 100,000 deep
 
def runGenerations( L ):
    """ runGenerations keeps running evolve...
    """
    show (L)
    print L  # display the list, L
    time.sleep(0)   # pause a bit
    newL = evolve( L )   # evolve L into newL
    runGenerations( newL )  # recurse
    
def evolve( L ):
    """ evolve takes in a list of integers, L,
    and returns a new list of integers
    considered to be the "next generation"
    """
    N = len(L)  # N now holds the size of the list L
    return [ setNewElement( L, i ) for i in range(N) ]
 

def setNewElement( L, i, x=0 ):
    """ setNewElement returns the NEW list's ith element
    input L: any list of integers
    input i: the index of the new element to return
    input x: an extra, optional input for future use
    """
    return L[i] + 1

#since in the setNewElement function it says plus 1 it will add one to each of the three numbers provided. The setNewElement function tells what numbers to use and what to do to the numbers, the evolve gives the next list of integers that setNewElement told it to do, and the setGeneration just does what evolve said to do. It seems to start from the bottom and work its way up.

#question 0
def setNewElement( L, i, x=0):
    return L[i] * 2
#question 1
def setNewElement( L, i, x=0):
    return L[i] ** 2
#question 2
def setNewElement( L, i, x=0):
    return L[i - 1]
#question 3
def setNewElement( L, i, x=0):
    return L[i + 1]
#random list generator
def setNewElement( L, i, x=0):
    return choice( [0,1] )

def allOnes(L):
    if 0 in L:
        return False
    #print true
    #else:
    return True

def runGenerations( L ):
    """ runGenerations keeps running evolve...
    """
    show (L)
    print L  # display the list, L
    time.sleep(0)   # pause a bit
    if allOnes(L)==True:
        return 1
    else:
        newL = evolve( L )
        return 1 + runGenerations( newL )

#setColor( 0, "red")
#setColor( 2, "yellow")
#setColor( 4, "blue")
    
def evolve( L ):
    """ evolve takes in a list of integers, L,
    and returns a new list of integers
    considered to be the "next generation"
    """
    N = len(L)  # N now holds the size of the list L
    x = sqinput()  # Get mouse input from the user
    return [ setNewElement( L, i, x ) for i in range(N) ]
 
def setNewElement( L, i, x=0 ):
    """ setNewElement returns the NEW list's ith element
    input L: any list of integers
    input i: the index of the new element to return
    input x: an extra, optional input for future use
    """
    if i == x:  # if it's the user's chosen column,
        return L[i] # return a random 0 or 1
    else: # otherwise
        return 1 - L[i] # return the original
    
#print runGenerations( [0,0,0,0,0,0] )

def randBL(N):
    return [choice([0,1]) for i in range(N)]

#unGenerations( randBL(9) )

#show( [ [0,1,0], [1,1,0], [0,0,1] ] )

def run2dGenerations( L ):
    """ runGenerations keeps running evolve...
    """
    show (L)
    print L  # display the list, L
    time.sleep(0)   # pause a bit
    if allOnes2d(L)==True:
        return 1
    else:
        newL = evolve2d( L )
        return 1 + run2dGenerations( newL )

    
def evolve2d( L ):
    """ evolve takes in a list of integers, L,
    and returns a new list of integers
    considered to be the "next generation"
    """
    N = len(L)  # N now holds the size of the list L
    x, y = sqinput2()  # Get mouse input from the user
    return [[ setNewElement2d( L, i, j, x, y ) for i in range(N) ] for j in range(N) ]
 
def setNewElement2d( L, i, j, x=0, y=0 ):
    """ setNewElement returns the NEW list's ith element
    input L: any list of integers
    input i: the index of the new element to return
    input x: an extra, optional input for future use
    """
    #if abs(y - i) <= 1 and abs(x - j) <= 1:
        #return L[j][i] 

    if i == x and y:  # if it's the user's chosen column,
        return 1 - L[j][i] # return a random 0 or 1
    else: # otherwise
        return L[j][i] # return the original

def allOnes2d(L):
    rowOnes = [allOnes(L[row]) for row in range(len(N))]
    if sum(rowOnes) == len(L):
        return True
    else:
        return False

def randBL2d(N):
    return [ [choice([0,1]) for i in range(N)] for j in range(N) ]

print run2dGenerations( randBL2d(4) )