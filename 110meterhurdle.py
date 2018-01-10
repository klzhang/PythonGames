from tkinter import *
import random

class GUIDie(Canvas):
    '''6-sided Die class for GUI'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6):
        '''GUIDie(master,[valueList,colorList]) -> GUIDie
        creates a GUI 6-sided die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self,master,width=60,height=60,bg='white',\
                        bd=5,relief=GROOVE)
        # store the valuelist and colorlist
        self.valueList = valueList
        self.colorList = colorList
        # initialize the top value
        self.top = 1

    def get_top(self):
        '''GUIDie.get_top() -> int
        returns the value on the die'''
        return self.valueList[self.top-1]

    def roll(self):
        '''GUIDie.roll()
        rolls the die'''
        self.top = random.randrange(1,7)
        self.draw()

    def draw(self):
        '''GUIDie.draw()
        draws the pips on the die'''
        # clear old pips first
        self.erase()
        # location of which pips should be drawn
        pipList = [[(1,1)],
                   [(0,0),(2,2)],
                   [(0,0),(1,1),(2,2)],
                   [(0,0),(0,2),(2,0),(2,2)],
                   [(0,0),(0,2),(1,1),(2,0),(2,2)],
                   [(0,0),(0,2),(1,0),(1,2),(2,0),(2,2)]]
        for location in pipList[self.top-1]:
            self.draw_pip(location,self.colorList[self.top-1])

    def draw_pip(self,location,color):
        '''GUIDie.draw_pip(location,color)
        draws a pip at (row,col) given by location, with given color'''
        (centerx,centery) = (17+20*location[1],17+20*location[0])  # center
        self.create_oval(centerx-5,centery-5,centerx+5,centery+5,fill=color)

    def erase(self):
        '''GUIDie.erase()
        erases all the pips'''
        pipList = self.find_all()
        for pip in pipList:
            self.delete(pip)

class Hurdle(Frame):

    def __init__(self,master,name):

        # set up Frame object
        Frame.__init__(self,master)
        self.grid()
        # label for player's name
        Label(self,text=name,font=('Arial',14)).grid(columnspan=3,sticky=W)

        self.attemptscoreLabel = Label(self,text='Attempt #1 Score: 0',font=('Arial',14))
        self.attemptscoreLabel.grid(row=0,column=2,columnspan=4)

        self.score = 0
        self.attempt = 1

        self.dice = []

        for n in range(5):
            self.dice.append(GUIDie(self,[1,2,3,4,5,6],['black']*6))
            self.dice[n].grid(row=1,column=n)

        self.rollButton = Button(self,text='Roll',command=self.roll)
        self.rollButton.grid(row=2,columnspan=2)
        self.keepButton = Button(self,text='Keep',state=DISABLED,command=self.keep)
        self.keepButton.grid(row=3,columnspan=2)

    def roll(self):
            
            self.score = 0
        
            for n in range(5):
                self.dice[n].roll()
                self.score += self.dice[n].get_top()

            self.attemptscoreLabel['text'] = 'Attempt #{} Score: {}'.format(self.attempt,self.score)

            if self.keepButton['state'] == DISABLED :
                self.keepButton['state'] = ACTIVE

            self.attempt += 1
            if(self.attempt > 5):
                self.rollButton['state']=DISABLED

    def keep(self):

        self.rollButton.grid_remove()
        self.keepButton.grid_remove()
        self.attemptscoreLabel['text']='Score: {} with {} attempts'.format(self.score,self.attempt)

# play the game
name = input("Enter your name: ")
root = Tk()
root.title('110 Meter Hurdle')
game = Hurdle(root,name)
game.mainloop()
        
