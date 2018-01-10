def encipher_fence(plaintext,numRails):
    '''encipher_fence(plaintext,numRails) -> str
    encodes plaintext using the railfence cipher
    numRails is the number of rails'''
    word = ""
    num = numRails - 1
    while(num >= 0):
        w = ""
        for i in range(len(plaintext)):
            if(i % numRails == num):
                w = w + plaintext[i]
        word = word + w
        num = num - 1
    return word

def decipher_fence(ciphertext,numRails):
    '''decipher_fence(ciphertext,numRails) -> str
    returns decoding of ciphertext using railfence cipher
    with numRails rails'''
    length = len(ciphertext)
    n1 = int(length / numRails)
    r = length % numRails
    word = ""
    position = []
    for x in range(0, numRails):
        position.append(0)
    
    if(r == 0):
        for i in range(0, n1):
            for j in range(numRails - 1, -1, -1):
                word = word + ciphertext[n1 * j + i]

    else:
        n2 = r
        for j in range(0, numRails):
            position[j] = n1 * j
            
        n9 = len(position)- r
        
        for l in range(0, r):
            position[n9] = position[n9] + l
            n9 = n9 + 1
            
        for k in range(0, n1):
            for h in range(len(position) - 1, -1, -1):
                word = word + ciphertext[position[h]]
                position[h] += 1

        num = r
        count = len(position) - 1
        while(num > 0):
            word = word + ciphertext[position[count]]
            num = num - 1
            count = count - 1

    return word
            

def decode_text(ciphertext,wordfilename):
    '''decode_text(ciphertext,wordfilename) -> str
    attempts to decode ciphertext using railfence cipher
    wordfilename is a file with a list of valid words'''

    inputFile = open('wordlist.txt','r')
    wordList = inputFile.readlines()
    inputFile.close()
    
    highest = -1
    rail = -1
    for i in range(1, 11):
        word = decipher_fence(ciphertext, i)
        count = 0
        words = word.split()
    
        for word1 in words:
            for word in wordList:
                word = word.strip('\n')
                if(word == word1):
                    count += 1
                    
        if(count == lens(words)):
            highest = 
    
        if(count > highest):
            highest = count
            rail = i
    w = decipher_fence(ciphertext, rail)
    return w
        

# test cases

# enciphering
print(encipher_fence("abcdefghi", 3))
# should print: cfibehadg
print(encipher_fence("This is a test.", 2))
# should print: hsi  etTi sats.
print(encipher_fence("This is a test.", 3))
# should print: iiae.h  ttTss s
print(encipher_fence("Happy birthday to you!", 4))
# should print: pidtopbh ya ty !Hyraou

# deciphering
print(decipher_fence("hsi  etTi sats.",2))
# should print: This is a test.
print(decipher_fence("iiae.h  ttTss s",3))
# should print: This is a test.
print(decipher_fence("pidtopbh ya ty !Hyraou",4))
# should print: Happy birthday to you!

# decoding
print(decode_text(" cr  pvtl eibnxmo  yghu wou rezotqkofjsehad", 'wordlist.txt'))
# should print: the quick brown fox jumps over the lazy dog
print(decode_text("unt S.frynPs aPiosse  Aa'lgn lt noncIniha ", 'wordlist.txt'))
# should print... we'll let you find out!
