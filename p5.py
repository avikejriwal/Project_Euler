from primeFunc import *

num = 20
retVal = 1
k = 2

#take every prime number less than 20, then take
#the highest whole power that is still less than 20, and multiply the running
#result by that
#this will incorporate the prime factorization of every number less than/equal to 20


while k < num:
    if isPrime(k):
        ex = 0
        j = k
        while j < num:
            j *= k
            ex += 1
        print j/k
        retVal *= j/k
    k += 1

print retVal
