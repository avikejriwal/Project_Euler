num = 100

tot = 0
tot2 = 0

for i in range(1,num+1):
    tot += i
    tot2 += i**2

print tot**2-tot2
