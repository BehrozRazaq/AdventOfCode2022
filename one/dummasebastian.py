file = open("input.txt")
input = file.readlines()

prevBig = [0]
current = 0
for line in input:
    if line == '\n':
        current += 1
        prevBig.append(0)
        continue
    prevBig[current] += int(line[0: -1])

prevBig.sort()
result = prevBig[-1] + prevBig[-2] + prevBig[-3]
print(result)