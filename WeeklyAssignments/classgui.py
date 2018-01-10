import turtle

# handler function for spacebar keypress event
def spacebar_pressed():
    print("You pressed the spacebar!")

# create a new window
wn = turtle.Screen()

# listener for a spacebar keypress
wn.onkey(spacebar_pressed,"space")

# have the window listen and wait
wn.listen()
wn.mainloop()
