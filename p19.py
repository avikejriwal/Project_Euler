#solution to problem 19

Year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapYear = list(Year)
leapYear[1] = 29


initDay = 2 #1/1/1901 was a Tuesday
count = 0
for i in range(1901,2001):
    for j in range(0,12):
        initDay = initDay % 7
        if initDay == 0:
            count += 1
        if i < 1905:
            print i, j+1, initDay
        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
                #leap year
            isLeap = True
        else:
            isLeap = False
        if isLeap:
            initDay += leapYear[j] #shift the start date for the next month by this much
        else:
            initDay += Year[j]

print count
