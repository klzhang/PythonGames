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


class GUIFreezeableDie(GUIDie):
    '''a GUIDie that can be "frozen" so that it can't be rolled'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6):
        '''GUIFreezeableDie(master,[valueList,colorList]) -> GUIFreezeableDie
        creates a GUI 6-sided freeze-able die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        GUIDie.__init__(self,master,valueList,colorList)
        self.isFrozen = False  # die starts out unfrozen

    def is_frozen(self):
        '''GUIFreezeableDie.is_frozen() -> bool
        returns True if the die is frozen, False otherwise'''
        return self.isFrozen
    
    def toggle_freeze(self):
        '''GUIFreezeableDie.toggle_freeze()
        toggles the frozen status'''
        self.isFrozen = not self.isFrozen
        if self.isFrozen:
            self['bg'] = 'gray'
        else:
            self['bg'] = 'white'

    def roll(self):
        '''GuiFreezeableDie.roll()
        overloads GUIDie.roll() to not allow a roll if frozen'''
        if not self.isFrozen:
            GUIDie.roll(self)


class Discus(Frame):
    '''a small application to test the freezeable die'''
    
    def __init__(self,master,name):
        
        Frame.__init__(self,master)
        self.grid()
        
        Label(self,text=name,font=('Arial',10)).grid(columnspan=3,sticky=W)

        self.attemptLabel = Label(self,text='Attempt #1',font=('Arial',10))
        self.attemptLabel.grid(row=0,column=2,columnspan=2,sticky=W)
        self.scoreLabel = Label(self,text='Score: 0',font=('Arial',10))
        self.scoreLabel.grid(row=0,column=3,columnspan=2)
        self.highscoreLabel = Label(self,text='High Score: 0',font=('Arial',10))
        self.highscoreLabel.grid(row=0,column=5,columnspan=2)

        self.gameround = 1
        self.score = 0
        self.highscore = 0

        self.dice = []
        self.freezeButtons = []

        for n in range(5):
            self.dice.append(GUIFreezeableDie(self,[0,2,0,4,0,6],['red','black','red','black','red','black']))
            self.dice[n].grid(row=1,column=n)
            self.freezeButtons.append(Button(self,text='Freeze',command=self.dice[n].toggle_freeze))
            self.freezeButtons[n].grid(row=2,column=n)

        self.rollButton = Button(self,text='Roll',command=self.roll)
        self.rollButton.grid(row=1,column=5)
        self.stopButton = Button(self,text='Stop',command=self.stop)
        self.stopButton.grid(row=2,column=5)


    def roll(self):

        count = 0
        self.score = 0

        for n in range(5):
            self.dice[n].roll()
            if(self.dice[n].get_top() % 2 == 0):
                self.score += self.dice[n].get_top()
                self.freezeButtons[n]['state']=ACTIVE

        if(self.score == 0):
            self.stop()
            
        self.scoreLabel['text'] = 'Score: ' + str(self.score)

    def stop(self):

        if(self.score > self.highscore):
            self.highscore = self.score
            self.highscoreLabel['text'] = 'High Score: ' + str(self.highscore)

        if self.gameround < 3:
            for n in range(5):
                self.dice[n].erase()
                self.freezeButtons[n]['state']=DISABLED
            self.scoreLabel['text'] = 'Score: 0'
            self.attemptLabel['text'] = 'Attempt: ' + str(self.gameround + 1)
            self.gameround += 1
        else:
            self.scoreLabel.grid_remove()
            self.rollButton.grid_remove()
            self.stopButton.grid_remove()
            self.attemptLabel['text'] = 'Game Over'
        


# test application
name = input("Enter your name: ")
root = Tk()
root.title('Discus')
game = Discus(root,name)
game.mainloop()
