from primeFunc import *
import math

num = 2000000

tot = 0

i = 2

while i < num:
    print i
    if isPrime(i):
        tot += i
    if i == 2:
        i += 1
    else:
        i += 2

print tot
