# part 1
# uppercase +26
caseItems = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6,
             'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 
             'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 
             's':19, 't':20, 'u':21, 'v':22, 'w': 23, 'x':24, 
             'y':25, 'z':26}


total = 0
f = open("input.txt", "r")
for i in f:
    firstHalf = i.rstrip()[:len(i)//2]
    secondHalf = i.rstrip()[len(i)//2:]
    for j in firstHalf:
        if j in secondHalf:
            if j.isupper():
                total += caseItems[j.lower()] + 26
                break
            else:
                total += caseItems[j]
                break
f.close()
print(total)

# part 2
f = open("input.txt", "r")
lineCounter = 0
badgeTotal = 0
allLines = []
for i in f:
    allLines.append(i)
    lineCounter += 1
    if lineCounter == 3:
        for j in allLines[0]:
            if j in allLines[1] and j in allLines[2]:
                if j.isupper():
                    badgeTotal += caseItems[j.lower()] + 26
                    break
                else:
                    badgeTotal += caseItems[j]
                    break
        allLines.clear()
        lineCounter = 0

print(badgeTotal)
