# part1
points = {"A":{"X":4, "Y":8, "Z": 3}, "B":{"X": 1, "Y":5, "Z":9}, "C":{"X": 7,"Y": 2,"Z": 6}}

f = open("input.txt", "r")
score = 0
for i in f:
    start = i.rstrip()[0]
    answer = i.rstrip()[2]
    score += points[start][answer]
print(score)


# part2
points = {"A":{"X":3, "Y":4, "Z": 8}, "B":{"X": 1, "Y":5, "Z":9}, "C":{"X": 2,"Y": 6,"Z": 7}}

f = open("input.txt", "r")
score = 0
for i in f:
    start = i.rstrip()[0]
    answer = i.rstrip()[2]
    score += points[start][answer]
print(score)