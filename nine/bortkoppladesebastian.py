lines = open('nine\input.txt').readlines()

def deltaPos():
    return [tail['head'][0] - tail['pos'][0], tail['head'][1] - tail['pos'][1]]

def movePos(pos, dir):
    match dir:
        case 'U':
            pos[1] += 1
        case 'R':
            pos[0] += 1
        case 'D':
            pos[1] -= 1
        case 'L':
            pos[0] -= 1

def updateTail():
    x,y = deltaPos()
    # print(tail['pos'])
    # print(x,y)
    if abs(x) + abs(y) > 2:
        if x > 0 and y > 0:
            movePos(tail['pos'], 'U')
            movePos(tail['pos'], 'R')
            # print('ne')
        elif x > 0 and y < 0:
            movePos(tail['pos'], 'D')
            movePos(tail['pos'], 'R')
            # print('se')
        elif x < 0 and y < 0:
            movePos(tail['pos'], 'D')
            movePos(tail['pos'], 'L')
            # print('sw')
        else:
            movePos(tail['pos'], 'U')
            movePos(tail['pos'], 'L')
            # print('nw')
    else:
        if y > 1:
            movePos(tail['pos'], 'U')
        elif x > 1:
            movePos(tail['pos'], 'R')
        elif y < -1:
            movePos(tail['pos'], 'D')
        elif x < -1:
            movePos(tail['pos'], 'L')
    tail['visitedPos'].add(tuple(tail['pos']))

def updateHead(move):
    for _ in range(move[1]):
        # print(step)
        movePos(tail['head'], move[0])
        updateTail()

tail = {'pos': [0,0], 'head': [0,0], 'visitedPos': {(0,0)}}

for line in lines:
    move = line[:-1].split()
    updateHead([move[0], int(move[1])])
    # print(tail['pos'], tail['head'])

# print(tail)
print(len(tail['visitedPos']))