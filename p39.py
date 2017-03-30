#Solution to problem 39
import time
start_time = time.time()
from math import sqrt

#value n:
#loop through values i,j < n/2, compute sqrt(i^2+j^2), check if equal to n

#only need n/2 because triangular inequality; a single side of a triangle must be\
#less than half the perimeter

#brute force, but runs in about 25 seconds

#solution is O(n^3)

maxN = 1000
solutions = [0 for i in range(maxN)]

for n in range(maxN):
    for i in range(1, n/2):
        for j in range(i+1, n/2):
            k = sqrt(i**2 + j **2)
            if int(k) == k and i + j + k == n:
                print n, ':', i, j, int(k)
                solutions[n] += 1

print solutions.index(max(solutions))

print time.time() - start_time
