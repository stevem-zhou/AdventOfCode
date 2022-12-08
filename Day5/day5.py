# part1
chart = {1:['z','j','n','w','p','s'],
         2:['g','s','t'],
         3:['v','q','r','l','h'],
         4:['v','s','t','d'],
         5:['q','z','t','d','b','m','j'],
         6:['m','w','t','j','d','c','z','l'],
         7:['l','p','m','w','g','t','j'],
         8:['n','g','m','t','b','f','q','h'],
         9:['r','d','g','c','p','b','q','w']}

result = ""

with open("input.txt", "r") as f:
    for i in f:
        if i[0] == "m":
            for _ in range(int(i.rstrip().split(' ')[1])):
                moving = chart[int(i.rstrip().split(' ')[3])].pop()
                chart[int(i.rstrip().split(' ')[5])].append(moving)
            
for i in chart.keys():
    result += chart[i].pop()

print(result)

# part2

secondResult = ""

with open("input.txt", "r") as f:
    for i in f:
        if i[0] == "m":
            temp = []
            if int(i.rstrip().split(' ')[1]) > 1:
                for _ in range(int(i.rstrip().split(' ')[1])):
                    temp.append(chart[int(i.rstrip().split(' ')[3])].pop())
                chart[int(i.rstrip().split(' ')[5])].extend(temp[::-1])
            else:
                moving = chart[int(i.rstrip().split(' ')[3])].pop()
                chart[int(i.rstrip().split(' ')[5])].append(moving)
            
for i in chart.keys():
    secondResult += chart[i].pop()

print(secondResult)
