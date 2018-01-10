from tkinter import *
import random

class MinesweeperCell(Label):
    '''represents a cell in Minesweeper'''

    def __init__(self,master,coord):
        '''MinesweeperCell(master,coord) ->
        creates a blank minesweeper cell with (row,column) coord'''

        #creates label
        Label.__init__(self,master,height=2,width=4,text='',\
                       bg='white',font=('Arial',10),relief=RAISED)

        #initialize values
        self.colormap = colormap = ['','blue','darkgreen','red','purple','maroon','cyan','black','gray'] #color of text depending on cell's number
        self.coord = coord 
        self.number = 0 #number's default value is 0
        self.isBomb = False #not a bomb by default
        self.end = False #game end set as False by default
        self.disabled = False #cell is not flagged by default

        #set up listeners
        self.bind('<Button-1>',self.reveal)
        self.bind('<Button-3>',self.asterik)


    def get_coord(self):
        '''MinesweeperCell.get_coord() -> tuple
        returns (row,column) coordinate of the cell'''
        
        return self.coord

    def set_number(self,num):
        '''MinesweeperCell.set_number(num)
        sets the number in the cell'''

        self.number = num
    
    def get_number(self):
        '''MinesweeperCell.get_number() -> int
        returns the number in the cell (0 if empty)'''
        return self.number

    def set_gameend(self):
        '''MinesweeperCell.set_gameend()
        ends the game by setting end to True'''

        self.end = True
    
    def is_disabled(self):
        '''MinesweeperCell.is_read_only() -> boolean
        returns True if the cell is read-only, False if not'''

        return self.disabled

    def is_bomb(self):
        '''MinesweeperCell.is_bomb() -> boolean
        returns True if cell is bomb, False if not'''

        return self.isBomb

    def makebomb(self):
        '''MinesweeperCell_makebomb()
        makes the current cell a bomb and sets isBomb to True'''

        self.isBomb = True

    def reveal(self,event):
        '''MinesweeperCell.reveal(event)
        reveals the cell when cell is left clicked and not flagged'''
        
        if(not self.disabled and self.isBomb and not self.end): #if cell revealed is bomb
            self['text'] = '*' #reveal cells as a bomb
            self['bg'] = 'red' #set background to red
            self.master.end_game('loss') #end game as a loss
            
        if(not self.disabled and self['relief'] == RAISED and not self.end): #if cell revealed is not a bomb, not flagged, and not already pressed
            if(self.number != 0): #if the cell number is not equal to 0
                self['relief'] = SUNKEN #change relief to sunken
                self['bg']='gray' #change background color to gray
                self['text'] = self.number #display its number 
                self['fg'] = self.colormap[self.number] #change text color depending on its color
            else:
                self.master.auto_expose(self.get_coord()) #call the auto expose method if cell's number is equal to 0
            self.master.update() #updates cell to check if game is won
                

    def asterik(self,event):
        '''MinesweeperCell.asterik(event)
        flags cell when right clicked and not already revealed'''
        
        if(self['text'] == '*' and not self.end): #if cell is already flagged and game has not ended
           self['text'] = '' #unflag the cell
           self.disabled = False
           self.master.update() #update counter on the bottom
        elif(self['relief'] == RAISED and not self.end): #if cell is not yet flagged, game has not ended, and cell not yet revealed
            self['text'] = '*' #flag the cell by setting text to * and disabling it
            self.disabled = True
            self.master.update()

class MinesweeperGrid(Frame):
    '''object for a Minesweeper Grid'''

    def __init__(self,master,height,width,numBombs):
        '''MinesweeperGrid(master,height,width,numBombs)
        creates a new blank MinesweeperGrid
        with height as the height of the grid, width as grid's width
        and numBombs as number of bombs in the game'''
        #initialize new Frame
        Frame.__init__(self,master,bg='black')
        self.grid()

        #initialize values
        self.totalBombs = numBombs
        self.height = height
        self.width = width

        #set up cells
        self.cells = {}
        for r in range(height):
            for col in range(width):
                coord = (r,col)
                self.cells[coord] = MinesweeperCell(self,coord)
                self.cells[coord].grid(row=r,column=col)

        #set up remaining bombs label
        self.remainLabel = Label(self,text=str(self.totalBombs),bg='white',font=('Arial',18))
        self.remainLabel.grid(row=height,column=(int)(width/2)-1,columnspan=3,sticky=N)

        count = 0
        
        #insert bombs in random locations
        while(count < numBombs): 
            randrow = random.randint(0,height-1)
            randcol = random.randint(0,width-1)
            coord = (randrow,randcol)
            if(self.cells[coord].is_bomb()): # check to make sure cell is already not a bomb
                continue
            else:
                self.cells[coord].makebomb()
                #increase the number for adjacent cells
                for x in range(-1,2):
                    for y in range(-1,2):
                        r = randrow + x
                        c = randcol + y
                        #if coord is valid increase the cell's number by 1 
                        if(r < height and r >= 0 and c < width and c >= 0):
                            tmpCoord = (r,c)
                            self.cells[tmpCoord].set_number(self.cells[tmpCoord].get_number() + 1)
                count += 1

    def update(self):
        '''MinesweeperCell.update()
        updates counter on the bottom and checks to see if game is won'''
        
        stars = 0
        unpressed = 0

        #checks all cells for a star and any unpressed buttons
        for r in range(self.height):
            for col in range(self.width):
                coord = (r,col)
                if(self.cells[coord]['text'] == '' and self.cells[coord]['relief'] == RAISED):
                    #if cell is unpressed increment count for unpressed
                    unpressed += 1
                if(self.cells[coord]['text'] == '*' and self.cells[coord]['bg'] == 'white'):
                    #if cell is flagged increment count for stars
                    stars += 1

        remaining = self.totalBombs - stars
        self.remainLabel['text'] = str(remaining) #update label with remaining number of bombs

        if(unpressed == 0 and remaining == 0):
            self.end_game('win') # if there are no more unpressed buttons and right number of flagged cells

    def end_game(self,result):
        '''MinesweeperCell.end_game(result)
        ends the game with either a loss or win depending on result'''

        if(result == 'loss'): #if loss display loss message
            messagebox.showerror('Minesweeper','KABOOM! You lose.',parent=self)
        elif(result == 'win'): #if win display win message
            messagebox.showinfo('Minesweeper','Congratulations -- you won!',parent=self)

        #expose all other bombs not yet exposed
        for r in range(self.height):
            for col in range(self.width):
                coord = (r,col)
                self.cells[coord].set_gameend()
                if(self.cells[coord].is_bomb()):
                    if(self.cells[coord]['text'] != '*'):
                        self.cells[coord]['text'] = '*'
                        self.cells[coord]['bg'] = 'red'

    def auto_expose(self,coord):
        '''MinesweeperCell.auto_expose(coord)
        expose nearby cells if current cell's number is 1'''

        #if cell is not pressed, not flagged, and not a bomb, reveal it
        if(self.cells[coord]['relief'] != SUNKEN and not self.cells[coord].is_disabled()):
            self.cells[coord]['relief'] = SUNKEN
            self.cells[coord]['bg']='gray'
            if(self.cells[coord].get_number() != 0):
                self.cells[coord]['text'] = self.cells[coord].get_number()
                self.cells[coord]['fg'] = self.cells[coord].colormap[self.cells[coord].get_number()]
            else: #if cell's number is equal to 0, call autoexpose again for possible coords
                if(coord[0] + 1 < self.height):
                    newcoord = (coord[0]+1,coord[1])
                    self.auto_expose(newcoord)
                if(coord[0] - 1 >= 0):
                    newcoord = (coord[0]-1,coord[1])
                    self.auto_expose(newcoord)
                if(coord[1] + 1 < self.width):
                    newcoord = (coord[0],coord[1]+1)
                    self.auto_expose(newcoord)
                if(coord[1] - 1 >= 0):
                    newcoord = (coord[0],coord[1]-1)
                    self.auto_expose(newcoord)                        
            #updates to check for win
            self.master.update()

        

def play_minesweeper(width,height,numBombs):
    '''play_minesweeper(width,height,numBombs)
    plays minesweeper'''
    root = Tk()
    root.title('Minesweeper')
    mine = MinesweeperGrid(root,width,height,numBombs)
    root.mainloop()

play_minesweeper(2,2,2)
    
