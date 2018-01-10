from tkinter import *

class Conversion(Frame):
    '''temperature conversion app'''
    
    def __init__(self,master):
        '''Temperatures(master) -> new temperature conversion window'''
        Frame.__init__(self,master)
        self.grid()
        # set up control variables
        # (tkinter uses DoubleVar() for floats)
        self.inches = DoubleVar()
        self.centimeters = DoubleVar()
        # initialize values to freezing point of water
        self.inches.set(0)
        self.centimeters.set(0.0)
        # set up widgets
        Label(self,text="Inches").grid(row=0,column=0)
        Label(self,text="Centimeters").grid(row=0,column=1)
        Entry(self,textvariable=self.inches).grid(row=1,column=0)
        Entry(self,textvariable=self.centimeters).grid(row=1,column=1)
        Button(self,text="Convert to centimeters",command=self.inches_to_cm).grid(row=2,column=0)
        Button(self,text="Convert to inches",command=self.cm_to_inches).grid(row=2,column=1)

    def inches_to_cm(self):
        
        self.centimeters.set(self.inches.get() * 2.54)

    def cm_to_inches(self):
        
        self.inches.set(self.centimeters.get() / 2.54)

root = Tk()
root.title('Inches to Cm')
temps = Conversion(root)
temps.mainloop()
