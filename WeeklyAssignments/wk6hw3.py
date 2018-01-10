from tkinter import *

class ClickCounter(Frame):
    '''a window that counts button clicks'''

    def __init__(self,master):
        '''ClickCounter(master) -> new ClickCounter frame'''
        Frame.__init__(self,master)
        self.grid()
        # intialize counter
        self.counter = 0
        # initialize button and label
        Button(self,text='Click me!',command=self.add_click).grid()
        self.counterLabel = Label(self,text='No clicks yet.')
        self.counterLabel.grid()

    def add_click(self):
        '''ClickCounter.add_click()
        adds a click to the counter, and updates the label'''
        self.counter += 1
        message = str(self.counter) + ' click'
        if self.counter > 1:
            message += 's'
        message += ' so far.'
        self.counterLabel['text'] = message

# set up window and frame
root = Tk()
ccf = ClickCounter(root)
ccf.mainloop()
