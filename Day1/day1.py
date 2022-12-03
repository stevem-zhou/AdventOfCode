# part1
f = open("input.txt", "r")
allCalories = []
calories = 0
for i in f:
    if i != "\n":
        calories += int(i.rstrip())
    else:
        calories = 0
    allCalories.append(calories)
print(max(allCalories))
    
# part2
print(sum(sorted(allCalories)[-3:]))