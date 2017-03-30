#solution for problem 17


maxN = 1000

#'hundred and' adds 10 characters

#have to hardcode the first few because no predictable pattern
orgDict = {1: 3, 2: 3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6,\
            12: 6, 13: 8, 14:8, 15:7, 16: 7, 17: 9, 18: 8, 19: 8, 20:6,\
            30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}

countDict = {1: 3, 2: 3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6,\
            12: 6, 13: 8, 14:8, 15:7, 16: 7, 17: 9, 18: 8, 19: 8, 20:6,\
            30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}

tot = 0

for j in range(1, maxN):
    addVal = 0
    n = 0
    if j < 100: #the dict method works just fine for numbers <100
        n = j
    else:
        n = j % 100
        addVal += orgDict[int(j/100)] #number @ beginning; 1,2,3..9
        if n > 0: #check if there's anything left over after the modulus
            addVal += 10 #hundred and
        else:
            addVal += 7 #hundred
            print n, addVal
    if n > 0:
        if n in orgDict:
            addVal += orgDict[n]
        else:
            #find the largest number in the dict smaller than n, subtract it from n, then find the letter values
            keys = orgDict.keys()[::-1]
            keyInd = 0
            while keys[keyInd] > n:
                keyInd += 1
            m = n-keys[keyInd]
            countDict[n] = orgDict[m] + orgDict[keys[keyInd]]
            addVal += countDict[n]
        print j, addVal
    tot += addVal

tot += len('onethousand') #iterate the last one

print tot
