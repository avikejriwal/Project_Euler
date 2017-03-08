from primeFunc import *

num = 600851475143

k = 0

while k < num:
    k +=1
    if num % k == 0:
        if isPrime(k):
            print k
print k
