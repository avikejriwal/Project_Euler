import csv
import math

f = open('p042_words.txt','r')
reader = csv.reader(f)

ansArr = []

def isTri(n):
    x = (-1 + math.sqrt(1 + 8*n))/2
    if int(x) == x:
        return True
    else:
        return False

for line in reader:
    for word in line:
        tot = 0
        for cha in word:
            val = ord(cha)-64
            tot += val
        if isTri(tot):
            ansArr.append(word)

print len(ansArr)

f.close()
