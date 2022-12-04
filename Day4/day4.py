# part 1

cover = 0
f = open("input.txt", "r")
for i in f:
    pair = i.rstrip().split(",")
    oneStart = int(pair[0].split("-")[0])
    oneEnd = int(pair[0].split("-")[1])
    twoStart = int(pair[1].split("-")[0])
    twoEnd = int(pair[1].split("-")[1])
    if (oneStart <= twoStart) and (oneEnd >= twoEnd):
        cover += 1
    elif (twoStart <= oneStart) and (twoEnd >= oneEnd):
        cover += 1
print(cover)
f.close()

# part 2

cover = 0
f = open("input.txt", "r")
for i in f:
    oneList = []
    twoList = []
    pair = i.rstrip().split(",")
    oneStart = int(pair[0].split("-")[0])
    oneEnd = int(pair[0].split("-")[1])
    twoStart = int(pair[1].split("-")[0])
    twoEnd = int(pair[1].split("-")[1])
    for i in range(oneStart, oneEnd+1):
        oneList.append(i)
    
    for i in range(twoStart, twoEnd+1):
        twoList.append(i)
    
    for i in range(len(oneList)):
        if oneList[i] in twoList:
            cover += 1
            break
f.close()
print(cover)