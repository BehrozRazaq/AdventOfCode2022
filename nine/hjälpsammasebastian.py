lines = open('nine\input.txt').readlines()

def deltaPos(back, front):
    return [front[0] - back[0], front[1] - back[1]]

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

def updateKnots(back, front):
    x,y = deltaPos(back, front)
    if abs(x) + abs(y) > 2:
        if x > 0 and y > 0:
            movePos(back, 'U')
            movePos(back, 'R')
        elif x > 0 and y < 0:
            movePos(back, 'D')
            movePos(back, 'R')
        elif x < 0 and y < 0:
            movePos(back, 'D')
            movePos(back, 'L')
        else:
            movePos(back, 'U')
            movePos(back, 'L')
    else:
        if y > 1:
            movePos(back, 'U')
        elif x > 1:
            movePos(back, 'R')
        elif y < -1:
            movePos(back, 'D')
        elif x < -1:
            movePos(back, 'L')
    rope['visitedPos'].add(tuple(rope['knots'][-1]))

def updateHead(move):
    for _ in range(move[1]):
        movePos(rope['head'], move[0])
        updateKnots(rope['knots'][0], rope['head'])
        for knotIndex in range(1, len(rope['knots'])):
            updateKnots(rope['knots'][knotIndex], rope['knots'][knotIndex-1])

numberOfKnots = 9 # Change this
rope = {'knots': [], 'head': [0,0], 'visitedPos': {(0,0)}}
for knots in range(numberOfKnots):
    rope['knots'].append([0,0])

for line in lines:
    move = line[:-1].split()
    updateHead([move[0], int(move[1])])

print(len(rope['visitedPos']))