#David Ciupei
#Assignment 7

def encipher(S, n):
    return ''.join([sort(x,n) for x in S])

def sort( c, n ):
    #for the lower case letters
    if 'a' <= c <= 'z':
        result = ord(c) + n
        if result <= ord('z'):
            return chr(result)
        else:
            return chr(result - 26)
    #for the upper case letters    
    elif 'A' <= c <= 'Z':
        result = ord(c) + n
        if result <= ord('Z'):
            return chr(result)
        else:
            return chr(result - 26)
    else:
        return c

#decipher2 returns a new list of english string of the ciphered S. The new list consists of giving the probability of each string with x in range of 26. Best would be the max of the new list and the best is 1. 
def decipher(S):
    newList = [(prob(decipherList(S)[x]), decipherList(S)[x]) for x in range(26)]
    best = max(newList)
    return best[1]

#this function returns a list of strings of the ciphered S and moves the string n times which in this case is n and n is in range of 26 because there are 26 letters in the alphabet. 
def decipherList(S):
    List = [encipher(S,n) for n in range (26)]
    return List
 
#The prob function returns letter probability for the word S from the letProb function, which has the probability of all of the letters.   
def prob(S):
    return sum([letProb(x) for x in str(S)])

#table of probabilities for each letter... 
def letProb( c ):
    """ if c is the space character or an alphabetic character,
        we return its monogram probability (for english),
        otherwise we return 1.0 We ignore capitalization.
        Adapted from
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    else: return 1.000