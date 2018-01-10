import turtle

class SpecialTurtle(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        # the getscreen() method returns the Screen object that
        #    the turtle lives in
        self.getscreen().onkey(self.stop,'s')
        self.goforward()

    def goforward(self):
        self.forward(1)
        self.getscreen().ontimer(self.goforward,40)

    def stop(self):
        self.getscreen().bye()

wn = turtle.Screen()
st = SpecialTurtle()
wn.listen()
wn.mainloop()
