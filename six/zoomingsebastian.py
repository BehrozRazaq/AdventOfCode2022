file = open("six\input.txt")
line = file.readline()

previousForteen = line[:13]
hasDuplicates = 0
start = 0
for charIndex in range(len(line)):
    char = line[charIndex]
    if char in previousForteen or hasDuplicates:
        previousForteen = previousForteen[1:]
        previousForteen += char
    else:
        start = charIndex + 1
        break
    hasDuplicates = 0
    for previous in previousForteen:
        hasDuplicates += int(previousForteen.count(previous) > 1)
        
                
    
print(start)