#nth triangle number can be computed by n(n+1)/2
import math

n = 1
k = 1


def isSquare(n):
    root = int(math.sqrt(n))
    if root**2 == n:
        return True
    else:
        return False

while k < 500:
    k = 0
    N = n*(n+1)/2
    for j in range(1,int(math.sqrt(N))):
        if N % j == 0:
            k += 1
    n += 1
    k *= 2
    if isSquare(N):
        k += 1
    print N, k

#the nth triangular number has a value of O(n^2)
#it takes O(sqrt(N)) time to count all divisors of a number N
#total: O(n^2) time
#though it fails for squre number
