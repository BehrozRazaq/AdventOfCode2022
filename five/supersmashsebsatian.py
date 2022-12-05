file = open('five\input.txt')
input = file.readlines()

stacks = []
for line in input:
    if line [1] == '1':
        for stack in range(int(line.split()[-1])):
            stacks.append([])
        break

instructions = []
originalState = True
for line in input:
    if originalState:
        if line[1] == '1':
            originalState = False
            continue
        for stack in range(len(stacks)):
            if not line[4*stack: 4*stack+3] == '   ':
                stacks[stack].append(line[4*stack: 4*stack+3])        
    else:    
        if line == '\n':
            continue
        else:
            instruction = line.split()
            instructions.append(
                {'amount': int(instruction[1]),'from': int(instruction[3])-1,'to': int(instruction[5])-1})
for stack in stacks:
    stack.reverse()

for instruction in instructions:
    rangeList = list(range(instruction['amount']+1))[1:]
    rangeList.reverse()
    for move in rangeList:
        stacks[instruction['to']].append(stacks[instruction['from']].pop(-1*move))
        
res = ''
for stack in stacks:
    res += stack[-1][1]
print(res)
    

