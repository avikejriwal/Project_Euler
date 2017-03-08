#given a number of value n, determine whether n is prime:
#a single number takes sqrt(n) time if prime; constant otherwise
#(will usually terminate MUCH earlier)

#Prime number theorem: probability of a
#number being prime approaches 1/ln(n)

#expected runtime: O(sqrt(n))/ln(n) + O(1)*(1-1/ln(n))

#so runtime approaches O(sqrt(n)/log(n))

#functions for dealing with prime numbers

import math

def isPrime(n):
    if n == 1:
        return False
    i = 2
    while i < int(math.floor(math.sqrt(n)+1)):
        if n % i == 0:
            return False
        elif i == 2:
            i += 1
        else:
            i += 2
    return True

#problem 35
def isCircularPrime(i):
    strI = str(i)
    for l in range(len(strI)):
        rot = strI[l:] + strI[:l]
        if not isPrime(int(rot)):
            return False
    return True

#problem 37
def isTruncatable(i):
    strI = str(i)
    strI2 = str(i)
    #from left
    while len(strI) >= 1:
        if not isPrime(int(strI)):
            return False
        if not isPrime(int(strI2)):
            return False
        strI = strI[:-1]
        strI2 = strI2[1:]
    return True
