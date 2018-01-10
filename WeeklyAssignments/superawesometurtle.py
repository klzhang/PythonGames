import turtle

class SuperAwesomeTurtle(turtle.Turtle):
    '''a super awesome turtle!'''

    def __init__(self):
        '''SuperAwesomeTurtle() -> new SuperAwesomeTurtle
        subclass of Turtle'''
        
        turtle.Turtle.__init__(self)
        
        self.velocity = 0 #set starting velocity to 0

        #listeners
        self.getscreen().onkey(self.upkeypressed,'Up')
        self.getscreen().onkey(self.downkeypressed,'Down')
        self.getscreen().onkey(self.leftkeypressed,'Left')
        self.getscreen().onkey(self.rightkeypressed,'Right')
        self.getscreen().onkey(self.stop,'s')
        self.getscreen().onkey(self.close,'q')
        
        self.goforward()

    def goforward(self):
        '''moves the turtle forward if velocity is positive and backwards if velocity is negative'''
        
        if(self.velocity == 0): #if velocity is negative dont move
            self.forward(0)
            self.getscreen().ontimer(self.goforward, 40) #call itself with a 40 miliisecond timer
        else:
            self.forward(self.velocity) #set forward distance to its velocity
            self.getscreen().ontimer(self.goforward, 40) #call itself with a 40 miliisecond timer

    #handler methods
    def upkeypressed(self):
        '''increases velocity of turtle by 25 units/sec'''

        self.velocity = self.velocity + 1      

    def downkeypressed(self):
        '''decreases velocity of turtle by 25 units/sec'''
        
        self.velocity = self.velocity - 1

    def leftkeypressed(self):
        '''turns turtle 90 degrees to left'''
        
        self.left(90)

    def rightkeypressed(self):
        '''turns turtle 90 degrees to right'''
        
        self.right(90)

    def stop(self):
        '''stops turtle and sets velocity to 0'''
        
        self.velocity = 0
        
    def close(self):
        '''closes window and ends program'''
        
        self.getscreen().bye()

wn = turtle.Screen()
pete = SuperAwesomeTurtle()
wn.listen()
wn.mainloop()
