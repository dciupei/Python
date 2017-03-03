#David Ciupei
#CS121
#assignment #6


from bmp import *

def inMSet(c,n):
    z = 0
    for x in range(0, n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

 
def testImage():
    """ a function to demonstrate how
    to create and save a bitmap image
    """
    width = 200
    height = 200
    image = BitMap( width, height )
 
    # create a loop in order to draw some pixels
 
    for col in range(width):
        if col % 10 == 0: print 'col is', col
        for row in range(height):
            if col % 10 == 0 or row % 10 == 0:
                image.plotPoint( col, row ) 
                
                # we have now looped through every image pixel
                # next, we write it out to a file
 
    image.saveFile( "test.bmp" )
    #changing the col and row number determines how big the grid is for the picture or how zoomed in it is. Changing the and to or just makes the grid go from dotted grid to lines.

def scale(pix, pixNum, floatMin, floatMax):
    return float(pix)/pixNum * (floatMax - floatMin) + floatMin
    
def mset(width, height, coordinateList ):
    height = width * (coordinateList[3] - coordinateList[2]) / (coordinateList[1] - coordinateList[0]) 
    image = BitMap( width, height )
    numIterations = 25
    image.setPenColor( Color.DKRED ) 
     
    # create a loop in order to draw some pixels
     
    for col in range(width):
        x = scale (col, width, coordinateList[0], coordinateList[1])
        for row in range(height):
            y = scale (row, height, coordinateList[2], coordinateList[3])
        #if col % 10 == 0: print 'col is', col
        #for row in range(height):
            #if col % 10 == 0 and row % 10 == 0:
            if inMSet(x + y*1j, numIterations): image.plotPoint( col, row )
    
     
                # we have now looped through every image pixel
                # next, we write it out to a file
    
    
    image.saveFile( "mset.bmp" )        
    
mset(2000, 2000, [-2, 1, -1, 1])