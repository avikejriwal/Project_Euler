x = 1
y = 1
z = 0

k = 2

while len(str(z)) < 1000:
    z = x + y
    x = y
    y = z
    k += 1

print k
