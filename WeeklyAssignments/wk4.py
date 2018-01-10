import random

class Die:
    '''Die class'''

    def __init__(self,sides=6):
        '''Die(sides)
        creates a new Die object
        int sides is the number of sides
        (default is 6)
        -or- sides is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sides,int):
            self.numSides = sides
            self.sides = list(range(1,sides+1))
        else:  # use the list/tuple provided 
            self.numSides = len(sides)
            self.sides = list(sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A ' + str(self.numSides) + '-sided die with ' + \
               str(self.get_top()) + ' on top'

    def __add__(self,other):
        '''Die+Die -> object
        returns the sum of the two dice's tops'''
        return self.top + other.top

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = self.sides[random.randrange(self.numSides)]

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self,value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value

    def flip(self):
        self.top = self.sides[self.numSides - self.top]

def europadice():

    dice = Die([1,2,3,4,"W"])
    result = []
    n = [0,0,0,0,0]
    rerolls = 3
    count = 1

    for i in range(10):
        dice.roll()
        num = dice.get_top()
        if(num == 1):
            n[1] += 1
        elif(num == 2):
            n[2] += 1
        elif(num == 3):
            n[3] += 1
        elif(num == 4):
            n[4] += 1
        else:
            n[0] += 1
            
        result.append(num)

    largest = 0
    want = -1
    
    for i in range(1,5):
        if(n[i] > largest):
            largest = n[i]
            want = i

    out = ""
    for i in range(len(result)):
        out = out + str(result[i]) + " "

    print(out)
    print("We're going for all " + str(want) + "s")

    while(rerolls > 0):
        print("Reroll #" + str(count) + ". Please enter to reroll.")
        for i in range(len(result)):
            if(result[i] == want):
                continue
            elif(result[i] == "W"):
                continue
            else:
                dice.roll()
                num = dice.get_top()
                result[i] = num

        s = ""
        for i in range(len(result)):
            s = s + str(result[i]) + " "

        print(s)

        count += 1
        rerolls -= 1

    total = 0
    for i in range(len(result)):
        if(result[i] == want or result[i] == "W"):
              total += 1

    if(total == 10):
        print("Yay, you win!")
    else:
        print("Sorry, only got " + str(total))
        


europadice()
        
        

    
    
    
    


        
