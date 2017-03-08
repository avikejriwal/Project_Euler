tot = 0

maxVal = 4*(10**6)
x = 1
y = 1
z = 0

while z < maxVal:
    z = x+y
    if z % 2 == 0:
        tot += z
    x = y
    y = z

print tot
