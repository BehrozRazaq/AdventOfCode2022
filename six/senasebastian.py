file = open("six\input.txt")
line = file.readline()

previousThree = line[:3]
hasDuplicates = 0
start = 0
for charIndex in range(len(line)):
    char = line[charIndex]
    if char in previousThree or hasDuplicates:
        previousThree = previousThree[1:]
        previousThree += char
    else:
        start = charIndex + 1
        break
    hasDuplicates = 0
    for previous in previousThree:
        hasDuplicates += int(previousThree.count(previous) > 1)
        
                
    
print(start)