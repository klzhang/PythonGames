class Jar:
    '''Represents a jar'''

    def __init__(self, size):
        '''Jar(size) -> Jar
        Constructs a Jar
        size: int giving size of jar'''

        self.size = size
        self.water = 0 # starting jar is empty

    def __str__(self):
        '''str(Jar) -> str
        Returns a string giving the size of jar and how much water is in it'''
        answer = "Jar of size " + str(self.size) #returns size of jar
        answer += " contains exactly " + str(self.water) + " liters of water" # how much water is in jar
        return answer

    def fill(self):
        '''Jar.fill()
        Fills jar full of water'''

        self.water = self.size #sets water level to jar size

    def empty(self):
        '''Jar.empty()
        Empties jar of water'''

        self.water = 0 # sets water level to 0

    def pour(self, jar):
        '''Jar1.pour(Jar2)
        Pours contents of first jar into second
        until either jar1 is empty or jar2 is full'''

        if(jar.water + self.water <= jar.size): #if jar2 does not overflow from adding jar1's water
            jar.water += self.water             #add water from jar1 into jar2
            self.empty()                        #empty jar1
        else:                                   #if jar2 will overflow
            remain = jar.size - jar.water       #find required amount of water to fill up jar2
            jar.fill()                          #fill up jar2
            self.water = self.water - remain    #subtract from jar1 how much was added to jar2

j1 = Jar(3)
j2 = Jar(5)
j2.fill()
print(j1)
print(j2)
j2.pour(j1)
print(j1)
print(j2)
j2.empty()
print(j1)
print(j2)
j1.pour(j2)
print(j1)
print(j2)
j1.fill()
print(j1)
print(j2)
j1.pour(j2)
print(j1)
print(j2)
j2.empty()
print(j1)
print(j2)
j1.pour(j2)
print(j1)
print(j2)
j1.fill()
print(j1)
print(j2)
j1.pour(j2)
print(j1)
print(j2)

#should print out:
#Jar of size 3 contains exactly 0 liters of water
#Jar of size 5 contains exactly 4 liters of water
        
