from primeFunc import *


k = 1

n = 3

while k < 10001:
    if isPrime(n):
        k += 1
    n += 2

print n-2 #account for the fact that the loop updates n
#even after k reaches 10001
