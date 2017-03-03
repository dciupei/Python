from turtle import *
import time

def spiral(InitLength, turnAngle, multiplier):
    if InitLength >= 1:
    
        forward(InitLength)
        left (90)
        spiral (InitLength * .9, turnAngle == left, multiplier * InitLength)
        
spiral(100, 90, .9)
        

def svTree(trunkLength, levels):
    if trunkLength <= (trunkLength / levels):
        return
    
    forward (trunkLength)
    right (30)
    svTree (trunkLength * .5, trunkLength / levels)
    left (60)
    svTree (trunkLength * .5, trunkLength / levels)
    right (30)
    backward (trunkLength)
    
svTree(100,4)
 

def snowflake(lengthSide, levels):
    if levels == 0:
        forward (lengthSide)
        return
    lengthSide /= 3
    snowflake (lengthSide / 3, levels - 1)
    right(60)
    snowflake (lengthSide / 3, levels - 1)
    left(120)
    snowflake (lengthSide / 3, levels - 1)
    right(60)
    snowflake (lengthSide / 3, levels - 1)
    
def wholesnowflake (lengthSide, levels):
    for i in range (3):
        snowflake (lengthSide, levels)
        left (120)
        
wholesnowflake (100, 5)

    




    

        
    
    
    
    
    
