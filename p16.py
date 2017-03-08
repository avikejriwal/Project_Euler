#trivially easy with a language that handles massive numbers

strVal = str(2**1000)

tot = 0

for i in strVal:
    tot += int(i)

print tot
