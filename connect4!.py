#David Ciupei
#Final (GUI)

from Tkinter import *

gutter = 75

class Board:

    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.data = [] # this will be the board
    
        for row in range( self.height ):
            boardRow = []
            for col in range( self.width ):
                boardRow += [' ']
            self.data += [boardRow]
    
    def __repr__ (self):
        #print out rows & cols
        s = '' # the string to return
        for row in range( self.height ):
            s += '|' # add the spacer character
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += '\n'
        
        s += '--'*self.width + '-\n'
    
        for col in range( self.width ):
            s += ' ' + str(col % 10)
        s += '\n'
        
        return s      #return it
    
    
    def addMove( self,col,ox,GUIplaying):
	#addMove will work for both human and gui
        if self.allowsMove(col):
            for row in range( self.height ):
                if self.data[row][col] != ' ':
                    self.data[row-1][col] = ox
                    if (GUIplaying): # print black or red piece
                    	if (ox == 'x'):
                    		self.gui(row-1, col, "red")
                    	else:
                    		self.gui(row-1, col, "black")
                    return
            self.data[self.height-1][col] = ox
            if (GUIplaying): # print black or red piece
                if (ox == 'x'):
            		self.gui(self.height-1, col, "red")
            	else:
            		self.gui(self.height-1, col, "black")

    def allowsMove( self,col ):
        if 0 <= col < self.width:
            return self.data[0][col] == ' '
        else:
            print "try a valid number"
                   
    def winsFor( self,ox ):
        for row in range( 0,self.height ):
            for col in range( 0,self.width-3 ):
                if self.data[row][col] == ox and \
                self.data[row][col+1] == ox and \
                self.data[row][col+2] == ox and \
                self.data[row][col+3] == ox:
                    return True
                          
        for col in range( 0,self.width):
            for row in range( 0,self.height-3 ):
                if self.data[row][col] == ox and \
                self.data[row+1][col] == ox and \
                self.data[row+2][col] == ox and \
                self.data[row+3][col] == ox:
                    return True
                           
        for row in range( 0,self.height-3 ):
            for col in range( 3,self.width ):
                if self.data[row][col] == ox and \
                self.data[row+1][col-1] == ox and \
                self.data[row+2][col-2] == ox and \
                self.data[row+3][col-3] == ox:
                    return True
                       
        for row in range( 0,self.height-3):
            for col in range( 0,self.width-3 ):
                if self.data[row][col] == ox and \
                self.data[row+1][col+1] == ox and \
                self.data[row+2][col+2] == ox and \
                self.data[row+3][col+3] == ox:
                    return True
        return False
                          
    def isFull( self ):
        for col in range( self.width ):
            if self.data[0][col] == ' ':
                return False
        return True     
                    
    def clear(self):
        for col in range( self.width ):
            for row in range( self.height ):
                self.data[row][col] = ' '
                           
    def delMove( self,col ):
        for row in range( self.height ):
            if self.data[row][col] != ' ':
                self.data[row][col] = ' '
                return
        
    def setBoard( self, moveString ):
        
        nextCh = 'x'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove( col, nextCh )
            if nextCh == 'x':
                nextCh = 'o'
            else:
                nextCh = 'x'
                       
    def hostGame( self ):
        print self
        while True:
            var = self.Input('x')
            self.addMove(var, 'x')
            print self
            if self.winsFor( 'x' ):
                print "x wins!"
                break
            var = self.Input('o')
            self.addMove(var, 'o')
            print self
            if self.winsFor( 'o' ):
                print "o won!"
                break
            if self.isFull():
                print "cat's game"
                break
    
    def Input( self,ox ):
        while True:
            var = raw_input(ox + " play your move: ")
            var = int(var)
            if self.allowsMove( var ):
                return var   
            
    def playGameWith(self,aiPlayer, GUIplaying = False):
        print self 
        while True:
            var = self.Input('x')
            self.addMove(var, 'x', GUIplaying)
            print self
            if self.winsFor( 'x' ):
                print "x wins!"
                break
            oMove = aiPlayer.nextMove( self, GUIplaying) 
            self.addMove(oMove, 'o', GUIplaying)
            print self
            if self.winsFor( 'o' ):
                print "o won!"
                break
            if self.isFull():
                print "cat's game"
                break
                
    def playGameWithGui(self):
        var = self.guiColNum
        self.addMove(var, 'x', GUIplaying)
        print self
        if self.winsFor( 'x' ):
            self.winnerOfGUI('Red') 
            return
        oMove = self.aiPlayer.nextMove(self, False)  
        self.addMove(oMove, 'o', self.GUIplaying)
        print self
        if self.winsFor( 'o' ):
            self.winnerOfGUI('Black') 
            return
        if self.isFull():
            #print "cat's game"
            self.winnerOfGUI('')   
    
    def winnerOfGUI(self, winner):
    	if winner == "Red":
    		self.postMessage("Red won this time!")
    	elif winner == "Black":
    		self.postMessage("Black won this time!")
    	else: 
    		self.postMessage("Cat's game!")
    	# disables column buttons when printing a message
    	#self.column1Button['state'] = 'disabled'
    	#self.column2Button['state'] = 'disabled'
    	#self.column3Button['state'] = 'disabled'
    	#self.column4Button['state'] = 'disabled'
    #	self.column5Button['state'] = 'disabled'
    #	self.column6Button['state'] = 'disabled'
    #	self.column7Button['state'] = 'disabled'
      
    def gui(self,row,col,color):
        x1 = col*self.cellwidth 
        y1 = row*self.cellheight 
        x2 = x1 + self.cellwidth 
        y2 = y1 + self.cellheight        
        self.oval[row,col] = self.draw.create_oval(x1+2,y1+2,x2-2,y2-2, tags="oval")
        c = self.oval[row,col]
        self.draw.itemconfig(c,fill=color)
        
    def postMessage(self,newText):
        if self.message != None:
            self.draw.delete(self.message)
        self.message = self.draw.create_text(10,560,text = newText,anchor = "w", font = "courier 18")
        self.window.update()
    
    def colPressed(self, colNum):
    	self.guiColNum = colNum
    	self.playGameWithGui()                       
    
    def attachGUI(self,window, aiPlayer):
        self.GUIplayed = True
        self.aiPlayer = aiPlayer
        self.guiColNum = -1 # will change, just a starting point
        self.window = window
        self.message = None
        self.frame = Frame(window)
        self.frame.pack()
        self.draw = Canvas(self.frame, width=500, height=500 + gutter, borderwidth=0, highlightthickness=0)
        self.qButton = Button(self.frame,text="Quit",command=quit).place(x=440,y=545)
        # lambda function below lets to pass in a parameter into the command function   
        self.column1Button = Button(self.frame,text="col 1",command=lambda: self.colPressed(0))
        self.column1Button.place(x=7,y=500)
        self.column2Button = Button(self.frame,text="col 2",command=lambda: self.colPressed(1))
        self.column2Button.place(x=78,y=500)
        self.column3Button = Button(self.frame,text="col 3",command=lambda: self.colPressed(2))
        self.column3Button.place(x=149,y=500)
        self.column4Button = Button(self.frame,text="col 4",command=lambda: self.colPressed(3))
        self.column4Button.place(x=220,y=500)
        self.column5Button = Button(self.frame,text="col 5",command=lambda: self.colPressed(4))
        self.column5Button.place(x=291,y=500)
        self.column6Button = Button(self.frame,text="col 6",command=lambda: self.colPressed(5))
        self.column6Button.place(x=362,y=500)
        self.column7Button = Button(self.frame,text="col 7",command=lambda: self.colPressed(6))
        self.column7Button.place(x=433,y=500)
        self.draw.pack(side="top", fill="both", expand="true")
        self.row = 6 
        self.col = 7
        self.cellwidth = 71 
        self.cellheight = 83
        width = self.col*self.cellwidth 
        height = self.row*self.cellheight +gutter
        self.rect = {}
        self.oval = {}
        for col in range(self.col):
            for row in range(self.row):
                x1 = col*self.cellwidth 
                y1 = row * self.cellheight 
                x2 = x1 + self.cellwidth 
                y2 = y1 + self.cellheight 
                self.rect[row,col] = self.draw.create_rectangle(x1,y1,x2,y2, fill="blue", tags="rect") 
        self.draw.pack()
        self.circles = []
        self.gutter = gutter
        self.postMessage("Click on a Column")
        
     
           
class Player:
    
    def __init__(self,ox,ply):
        self.ox = ox
        self.ply = ply    
    
    def nextMove( self,board, GUIplayed):
        L = self.scoresFor(board,self.ox,self.ply, GUIplaying)
        best = max(L)
        for col in range( len( L ) ):
            if L[col] == best:
                return col    
    
    def scoresFor(self,board,ox,ply, GUIplaying):
        scoresList = []
        for col in range (board.width):
            if board.allowsMove(col):
                board.addMove(col,ox, GUIplaying)
                if board.winsFor( ox ):
                    scoresList += [100]  
                elif ply == 1:
                    scoresList += [50]
                else:
                    if ox == 'x':
                        opponent = 'o'
                    else:
                        opponent = 'x'
                    oppList = self.scoresFor(board,ox,ply-1, GUIplaying)
                    bestScore = max(oppList)
                    scoresList += [100-bestScore]
                board.delMove(col)
            else:
                scoresList += [-1]
        return scoresList

                
def playText():                        
    bd = Board (7,6)
    aiPlayer = Player ('x',3)
    bd.playGameWith(aiPlayer, False)


def playGUI():
    window = Tk ()
    bd = Board (7,6)
    window.title("Connect4")
    aiPlayer = Player('x', 3)
    bd.attachGUI(window, aiPlayer)
    window.mainloop()
    
#playText()
playGUI()

