from operator import mod


file = open("input.txt")
input = file.readlines()

groups = []
bagIndex = 0
badge = ''
for bag in input:
    if bagIndex % 3 == 0:
        for item in bag:
            bagTwo = input[bagIndex + 1]
            bagThree = input[bagIndex + 2]
            if (item in bagTwo[:-1]) and (item in bagThree[:-1]):
                badge = item
        groups.append(badge)
    bagIndex += 1

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
pointMap = {}
for charIndex in range(len(alphabet)):
    point = charIndex+1
    pointMap[alphabet[charIndex]] = point

sumPriorities = 0
for groupBadge in groups:
    sumPriorities += pointMap[groupBadge]

print(sumPriorities) 