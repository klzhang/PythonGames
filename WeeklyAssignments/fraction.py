class Fraction:
    '''represents fractions'''

    def __init__(self,num,denom):
        '''Fraction(num,denom) -> Fraction
        creates the fraction object representing num/denom'''
        if denom == 0: # raise an error if the denominator is zero
            raise ZeroDivisionError

        factor = 1
        lowest = min(abs(num), abs(denom)) #finds the lowest of the two numbers

        for i in range(lowest, 1, -1): #finds the greatest common factor
            if(num % i == 0 and denom % i == 0): #if both numerator and denominator are divisible, then it is a common factor
                factor = i
                break

        if(denom < 0): # if denominator is negative places negative sign onto numerator
            self.num = - int(num / factor)
            self.denom = - int(denom / factor)
        else: #if denominator is not negative, leave as is
            self.num = int(num/factor)
            self.denom = int(denom/factor)
        

    def __str__(self):
        '''str(Fraction) -> str
        string representation of the Fraction'''

        return str(self.num)+ "/" + str(self.denom)

    def __float__(self):
        '''float(Fraction) -> float
        float representation of the Fraction'''

        return (self.num/self.denom)

    def add(self, other):
        '''fraction1.add(fraction2) -> object
        returns sum of two fractions'''

        gcd = 1 #base case for greatest common denominator
        lowest = min(self.denom, other.denom) #finds the lowest of the two numbers

        for i in range(lowest, 1, -1): #finds the greatest common factor
            if(self.denom % i == 0 and other.denom % i == 0): #if both numerator and denominator are divisible, then it is a common factor
                gcd = i #finds gcd and exits out of loop
                break

        lcm = int(self.denom * other.denom / gcd) #finds least common multiple / also serves as denominator
        numerator = int(lcm*(self.num/self.denom + other.num/other.denom)) #calculates numerator

        fracsum = Fraction(numerator, lcm) #constructs new Fraction
        return fracsum

    def subtract(self, other):
        '''fraction1.subtract(fraction2) -> object
        returns difference of two fractions'''

        gcd = 1 #base case for greatest common denominator
        lowest = min(self.denom, other.denom) #finds the lowest of the two numbers

        for i in range(lowest, 1, -1): #finds the greatest common factor
            if(self.denom % i == 0 and other.denom % i == 0): #if both numerator and denominator are divisible, then it is a common factor
                gcd = i
                break

        lcm = int(self.denom * other.denom / gcd) #finds least common multiple / also serves as denominator
        numerator = int(lcm*(self.num/self.denom - other.num/other.denom)) #calculates numerator

        if(numerator == 0):
            fracdifference = Fraction(0, 1) #if fractions are equal, construct a fraction "0/1"
        else:
            fracdifference = Fraction(numerator, lcm) #else construct a fraction with numerator and lcm as denominator

        return fracdifference

    def mul(self, other):
        '''fraction1.mul(fraction2) -> object
        returns product of two fractions'''

        numerator = self.num * other.num #calculates numerator
        denominator = self.denom * other.denom #calculates denominator

        fracmul = Fraction(numerator, denominator) #constructs new Fraction
        return fracmul

    def div(self, other):
        '''fraction1.div(fraction2) -> object
        returns quotient of two fractions'''

        numerator = self.num * other.denom #calculates numerator
        denominator = self.denom * other.num #calculates denominator

        fracdiv = Fraction(numerator, denominator) #constructs new Fraction
        return fracdiv

    def eq(self, other):
        '''fraction1.eq(fraction2) -> boolean
        determines whether or not the two fractions are equal
        and returns True or False as result'''
        
        if(self.num/self.denom == other.num/other.denom): #sees if two fractions are equal
            return True #if equal return true
        else:
            return False #if not equal return false

    
        
# examples
p = Fraction(1,2)
print(p)  # should print 1/2
q = Fraction(2,-6)
print(q)  # should print -1/3
x = float(p)
print(x)  # should print 0.5
### if implementing "normal" arithmetic methods
print(p.add(q))       # should print 1/6, since 1/2 + (-1/3) = 1/6
print(p.subtract(q))  # should print 5/6, since 1/2 - (-1/3) = 5/6
print(p.subtract(p))  # should print 0/1, since p-p is 0
print(p.mul(q)) # should print -1/6
print(p.div(q))  # should print -3/2
print(p.eq(p))   # should print True
print(p.eq(q))   # should print False

