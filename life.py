#David Ciupei
#assignment #8

import csplot
import random
import time

def createOneRow( n ):
    """ returns rows of n zeros...  You might use
    this as the INNER loop in createBoard """
    R = []
    for col in range(n):
        R += [0]
        return R
    
def createBoard( width, height ): 
    return [[ 0 for x in range(width)] for y in range(height)]

def update1( B ):
    """ Takes an empty board as input and modifies that board
    so that it has a diagonal strip of "on" cells
    """
    width = len(B[0])
    height = len(B)
   
    for row in range(height):
        for col in range(width):
            if row == col:
                B[row][col] = 1
            else:
                B[row][col] = 0  # else not needed here,but OK
                
                
def update2( B ):
    """ Takes an empty board as input and modifies that board
    so that it has a diagonal strip of "on" cells
    """
    width = len(B)
    height = len(B)
   
    for row in range(height):
        for col in range(width):
            if col - 0: 
                if col - 9:
                    if row - 0:
                        if row - 9:
                            B[row][col] = 1
                        else:
                            B[row][col] = 0
                            
def updateRandom( B ):
    width = len(B[0])
    height = len(B)
       
    for row in range(height):
        for col in range(width):
            if col - 0: 
                if col - 9:
                    if row - 0:
                        if row - 9:
                            if col - 0:
                                B[row][col] = random.choice([0,1])
                            else:
                                B[row][col] = random.choice([0,1])   

def updateReversed( oldB, newB ):
    width = len(oldB[0])
    height = len(oldB)
    
    for row in range(height):
        for col in range(width):
            if col - 0:
                if col - 9:
                    if row - 0:
                        if row - 9:
                            if oldB[row][col] is 0:
                                newB[row][col] = 1
                            else: newB[row][col] = 0
                                    
def life( width, height ):
    """ will become John Conway's Game of Life... """
    B = createBoard( width, height )
    updateRandom( B )
    #csplot.showAndClickInIdle( B )
    if pause == False:
        B = createNextLifeBoard( oldB )
        keysList = csplot.getKeysDown()
        if 'p' in keysList:
            pause = True    
 
    while True:                      # run forever
        csplot.show(B)               # show current B
        time.sleep(0.25)              # pause a bit
        oldB = B       #  just a reminder for us humans
        B = createBoard(width, height)   #  creates a new board
        updateNextLife( oldB, B )  #  sets the new board correctly
    
def countNeighbors(B,row,col):
    count = 0
    for i in range(row - 1,row + 2):
        for j in range(col - 1,col + 2):
            if i == row and j == col:continue
            if B[i][j] is 1: count += 1
    return count
   
def updateNextLife(oldB,newB):
    width = len(oldB[0])
    height = len(oldB)
    for row in range(1, width - 1):
        for col in range(1, height - 1):
            count = countNeighbors(oldB,row,col)
            if oldB[row][col] and (count < 2 or count > 3):
                newB[row][col] = 0
            elif oldB[row][col] is 0 and count == 3:
                newB[row][col] = 1
            else:
                newB[row][col] = oldB[row][col] 
    
    
#B = createBoard(10,10)
#updateRandom(B)
#d = {0: 'green',1: 'red'}
#csplot.show(B,d)
#newB = createBoard(10,10)
#updateReversed(B,newB)
#csplot.show(newB)

life(10,10)


#I tried opening the file in the terminal in the directory where the life.py and csplot is saved and got the python to work but whenever I type in something nothing happens so I couldnt do the extensions part