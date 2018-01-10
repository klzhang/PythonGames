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

class ShotPutFrame(Frame):
    '''frame for a game of Shot Put'''

    def __init__(self,master,name):
        '''ShotPutFrame(master,name) -> ShotPutFrame
        creates a new frame for the game ShotPut
        name is player's name'''

        #set up Frame object
        Frame.__init__(self,master)
        self.grid()
        #label for player's name
        Label(self,text=name,font=('Arial',12)).grid(columnspan=3,sticky=W)
        #set up score labels
        self.attemptscoreLabel = Label(self,text='Attempt #1 Score: 0',font=('Arial',12))
        self.attemptscoreLabel.grid(row=0,column=2,columnspan=4)
        self.highscoreLabel = Label(self,text='High Score: 0',font=('Arial',12))
        self.highscoreLabel.grid(row=0,column=6,columnspan=2)
        #initialize game data
        self.score = 0
        self.attempt = 1
        self.gameround = 0
        self.highscore = 0
        #set up dice
        self.dice = []
        for n in range(8):
            self.dice.append(GUIDie(self,[0,2,3,4,5,6],['red']+['black']*5))
            self.dice[n].grid(row=1,column=n)
        #set up buttons
        self.rollButton = Button(self,text='Roll',command=self.roll)
        self.rollButton.grid(row=2,column=0)
        self.stopButton = Button(self,text='Stop',state=DISABLED,command=self.stop)
        self.stopButton.grid(row=3,column=0)

    def roll(self):
        '''ShotPutFrame.roll()
        handler method for the roll button click'''

        #rolls dice
        self.dice[self.gameround].roll()

        #if it is first roll of the round, activate stop button
        if(self.stopButton['state']==DISABLED):
            self.stopButton['state']=ACTIVE

        #if dice returns 1 on top then it is a foul, going to next round
        if(self.dice[self.gameround].get_top() == 0):
            self.attemptscoreLabel['text'] = 'FOULED ATTEMPT'
            self.rollButton['state'] = DISABLED #disable roll button
            self.stopButton['text'] = 'Foul'
            self.score = 0 #set round score to 0
        else: # otherwise add up score
            self.score += self.dice[self.gameround].get_top()
            self.attemptscoreLabel['text'] = 'Attempt #{} Score: {}'.format(self.attempt,self.score)
            #disable roll button after the 8th dice is rolled
            if(self.gameround == 7):
                self.rollButton['state']=DISABLED
            #increment game round and move buttons
            if(self.gameround < 7):
                self.gameround += 1
                self.rollButton.grid(row=2,column=self.gameround)
                self.stopButton.grid(row=3,column=self.gameround)


    def stop(self):
        '''ShotPutFrame.stop()
        handler method for the stop button click'''
        
        if(self.score > self.highscore):
            self.highscore = self.score #updates new high score
            self.highscoreLabel['text'] = 'High Score: {}'.format(self.highscore)

        if(self.attempt < 3):
            self.score = 0 #set score to 0
            
            for n in range(8): #clears dice for new round
                self.dice[n].erase()

            #move buttons back to the first dice
            self.rollButton.grid(row=2,column=0) 
            self.stopButton.grid(row=3,column=0)
            self.rollButton['state']=ACTIVE #activate roll button in case it was disabled in previous round
            self.stopButton['text']='Stop' #stop button's text should say stop again in case it was changed to foul in previous round
            self.stopButton['state']=DISABLED #disable stop button

            self.gameround = 0 #set game round to 0
            self.attempt += 1 #increase attempt and update label
            self.attemptscoreLabel['text']= 'Attempt #' + str(self.attempt) + ' Score: 0'
        else: #otherwise if 3 attempts are done remove buttons and end game
            self.rollButton.grid_remove()
            self.stopButton.grid_remove()
            self.attemptscoreLabel['text']='Game Over'



# play the game
name = input("Enter your name: ")
root = Tk()
root.title('ShotPut')
game = ShotPutFrame(root,name)
game.mainloop()

        
