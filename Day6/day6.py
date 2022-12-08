# part1
unique = []
with open("input.txt", "r") as f:
    for i in f:
        for letter in i:
            unique.append(letter)
            if len(unique) > 4:
                temp = set(unique[-4:])
                if len(temp) == 4:
                    print(len(unique))
                    break

# part2
unique = []
with open("input.txt", "r") as f:
    for i in f:
        for letter in i:
            unique.append(letter)
            if len(unique) > 14:
                temp = set(unique[-14:])
                if len(temp) == 14:
                    print(len(unique))
                    break