# Python Class 1139
# Lesson 6 Problem 3
# Author: Mr. Geometry (47507)

import turtle
import random

class MisbehavingTurtle(turtle.Turtle):

    def __init__(self):

        turtle.Turtle.__init__(self)

    def forward(self,amt):
        turtle.Turtle.forward(self,amt)

    def backward(self,amt):
        turtle.Turtle.backward(self,amt)

    def left(self,amt):
        num = random.randit(0,3)
        if(num == 0):
            turtle.Turtle.right(self,amt)
        else:
            turtle.Turtle.left(self,amt)

    def right(self,amt):
        num = random.randit(0,3)
        if(num == 0):
            turtle.Turtle.left(self,amt)
        else:
            turtle.Turtle.right(self,amt)

# test case
# drawing an octagon and a square
def drawing_test(t):
    '''drawing_test(t)
     draws an octagon and square with t'''
    for i in range(8):
        t.forward(30)
        t.left(45)
    t.right(45)
    for i in range(4):
        t.forward(50)
        t.right(90)
        
# one nice turtle and one not-so-nice turtle
wn = turtle.Screen()
sugar = turtle.Turtle()
sugar.color('green')
drawing_test(sugar)
spice = MisbehavingTurtle()
spice.color('red')
drawing_test(spice)
wn.mainloop()
