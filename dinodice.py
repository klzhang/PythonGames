# Python Class 1139
# Lesson 6 Problem 5
# Author: Mr. Geometry (47507)

import random

### Die class that we previously wrote ###

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
        return 'A '+str(self.numSides)+'-sided die with '+\
               str(self.get_top())+' on top'

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

### end Die class ###

class DinoDie(Die):
    '''implements the dice for Dino Hunt'''

    def __init__(self,color):
        '''DinoDie(color) -> DinoDie
        creates a dino die based on its color'''

        self.color = color
        if(color == 'green'):
            Die.__init__(self,['dino','dino','dino','leaf','leaf','foot']) #creates green dice
        elif(color == 'yellow'):
            Die.__init__(self,['dino','dino','foot','leaf','leaf','foot']) #creates yellow dice
        else:
            Die.__init__(self,['dino','foot','foot','leaf','leaf','foot']) #creates red dice

    def __str__(self):
        '''str(DinoDie) -> str
        string representation of a Dino Die'''

        return 'A {} Dino die with a {} on top.'.format(self.color,self.get_top())


class DinoPlayer:
    '''implements a player of Dino Hunt'''

    def __init__(self,name):
        '''DinoPlayer(name) -> DinoPlayer
        Creates a player for the Dino hunt game'''

        self.name = name
        self.score = 0 #set intial score to 0

    def __str__(self):
        '''str(DinoPlayer) -> str
        string representation of a player playing Dino hunt'''

        return '{} has {} points.'.format(self.name,self.score)

    def take_turn(self):

        print()
        print(self.name + ", it's your turn!")
        dice = ['green','green','green','green','green','green','red','red','red','yellow','yellow','yellow','yellow']
        green = 6 #starting number of green dice
        yellow = 4 #starting number of yellow dice
        red = 3 #starting number of red dice
        numDice = 13 #starting number of dice
        dinos = 0
        feet = 0
        print("You have " + str(numDice) + " dice remaining.")
        print(str(green) + " green, " + str(yellow) + " yellow, " + str(red) + " red")
        print("Press enter to select dice and roll")        
        while(True):
            print()
            if(numDice == 0):
                print("No more dice remaining") #exits if no dice remaining
                break
            count = 0
            while(count != 3): #simulates picking three dice
                num = random.randint(0,len(dice)-1) #randomly picks a dice
                d = DinoDie(dice[num])
                print(d)
                if(d.top == 'dino'): #if the top of the dice says dino
                    dinos += 1       #add one to number dinos in round
                    dice.pop(num)    #remove that dice
                    numDice -= 1     #updates counter of dice
                    if(d.color == 'green'): 
                        green -= 1
                    elif(d.color == 'yellow'):
                        yellow -= 1
                    else:
                        red -= 1
                if(d.top == 'foot'): #if the top of the dice says foot
                    feet += 1        #add one to number of feet in round
                    dice.pop(num)    #remove that dice
                    numDice -= 1     #updates counter of dice
                    if(d.color == 'green'): 
                        green -= 1
                    elif(d.color == 'yellow'):
                        yellow -= 1
                    else:
                        red -= 1                    
                count += 1
            print("This turn so far: " + str(dinos) + " dinos and " + str(feet) + " feet")
            if(feet >= 3): #if you get more than 3 feet, end turn and get 0 dinos for that turn
                print("Too bad -- you got stomped!")
                print()
                dinos = 0
                break
            print("You have " + str(numDice) + " dice remaining.")
            print(str(green) + " green, " + str(yellow) + " yellow, " + str(red) + " red")
            response = input("Do you want to roll again? (y/n) ")
            if(response.lower() == 'n'): #if the response is no then quit
                print()
                break
        self.score = self.score + dinos #update the score
            
            
def play_dino_hunt(numPlayers,numRounds):
    '''play_dino_hunt(numPlayer,numRounds)
    plays a game of Dino Hunt
      numPlayers is the number of players
      numRounds is the number of turns per player'''
    playerList = [] #list of players
    score = -1
    winner = ''
    for i in range(numPlayers):
        name = input("Player " + str(i + 1) + ", enter your name: ")
        playerList.append(DinoPlayer(name)) #creates and stores players in list
    round = 0
    while(round != numRounds): #keep playing until number of rounds is met
        print()
        print("ROUND " + str(round + 1))
        print()
        for i in range(numPlayers):
            for player in playerList:
                print(player)
            playerList[i].take_turn() #takes turn for each player in player list
        round += 1
    for player in playerList:
        if(player.score > score):
            score = player.score #stores highest score so far
            winner = player #scores highest scoring player so far
    print()
    print("We have a winner!")
    print(winner)


play_dino_hunt(2,2)
