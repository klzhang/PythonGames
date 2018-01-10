import random

class DominoTile:

    def __init__(self,left,right):

        self.left = left
        self.right = right

    def __str__(self):

        return(str(self.left) + ' ' + str(self.right))

    def is_match(self,other):

        return (self.left == other.left) or (self.left == other.right) or (self.right == other.left) or (self.right == other.right)


class DominoDeck:

    def __init__(self):

        self.deck = []
        for a in range(7):
            for b in range(a,7):
                self.deck.append(DominoTile(a,b))
        random.shuffle(self.deck)

    def __str__(self):

        return 'A domino deck with ' + str(len(self.deck)) + ' dominoes remaining'

    def deal_domino(self):
        return self.deck.pop()
    
class DominoPlayer:

    def __init__(self,name,deck,cpu):

        self.name = name
        self.hand = [deck.deal_domino() for i in range(7)]
        if(cpu == 'yes'):
            self.cpu = True
        else:
            self.cpu = False

    def __str__(self):

        return str(self.name)+ ' has ' + str(len(self.hand)) + ' dominoes.'

    def get_name(self):

        return self.name

    def get_hand(self):

        output = ''
        for domino in self.hand:
            output += str(domino) + '\n'
        return output

    def has_won(self):
        return len(self.hand) == 0

    def play_domino(self,domino,chain):

        self.hand.remove(domino)
        if(chain.left == domino.left):
            chain.left = domino.right
        elif(chain.left == domino.right):
            chain.left = domino.left
        elif(chain.right == domino.left):
            chain.right = domino.right
        else:
            chain.right = domino.left

    def take_turn(self,chain):

        print(self.name + ", it's your turn.")
        print(chain)
        if(self.cpu == False):
            print("Your hand: ")
            print(self.get_hand())
        matches = [domino for domino in self.hand if domino.is_match(chain)]

        if len(matches) > 0:
            for index in range(len(matches)):
                if(self.cpu == False):
                    print(str(index + 1) + ": " + str(matches[index]))
                choice = 0
                while(choice < 1 or choice > len(matches)):
                    if(self.cpu):
                        choice = random.randint(1, len(matches))
                    else:
                        choicestr = input("Which do you want to play? ")
                        if choicestr.isdigit():
                            choice = int(choicestr)
                self.play_domino(matches[choice-1],chain)
        else:
            print("You can't play anything, so your turn is skipped")

def play_domino():

    deck = DominoDeck()
    playerList = []
    chain = DominoTile(6,6)
    copy = DominoTile(6,6)
    name = input('Player #1, enter your name: ')
    playerList.append(DominoPlayer(name,deck,'no'))
    for i in range(3):
        cpuName = "cpu" + str(i)
        playerList.append(DominoPlayer(cpuName,deck,'yes'))

    start = -1
    place = -1
    for i in range(4):
        for j in range(7):
            if(playerList[i].hand[j].left == 6 and playerList[i].hand[j].right == 6):
                start = i
                place = j

    currentPlayerNum = i
    print('-------')
    for player in playerList:
        print(player)
    print('-------')

    playerList[currentPlayerNum].play_domino(playerList[currentPlayerNum].hand[place],chain)
    currentPlayerNum = (currentPlayerNum + 1) % 4

    count= 0


    while True:
        print('-------')
        for player in playerList:
            print(player)
        print('-------')

        playerList[currentPlayerNum].take_turn(chain)

        if(playerList[currentPlayerNum].has_won()):
            print(playerList[currentPlayerNum].get_name() + " wins!")
            print("Thanks for playing")
            break

        if(copy.left == chain.left and copy.right == chain.right):
            count = count + 1
        else:
            copy.left = chain.left
            copy.right = chain.right
            count = 0

        if(count == 4):
            print(playerList[currentPlayerNum].get_name() + " wins!")
            print("Thanks for playing")
            break

        currentPlayerNum = (currentPlayerNum + 1) % 4

        
play_domino()





    
