file = open("input.txt")
input = file.readlines()

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
pointMap = {}
for charIndex in range(len(alphabet)):
    point = charIndex+1
    pointMap[alphabet[charIndex]] = point

sumPriorities = 0
faultyItem = ''
for bag in input:
    compOne = bag[:int(len(bag)/2)]
    compTwo = bag[int(len(bag)/2):]
    for item in compOne:
        if (item in compTwo):
            faultyItem = item
    sumPriorities += pointMap[faultyItem]
            
print(sumPriorities)