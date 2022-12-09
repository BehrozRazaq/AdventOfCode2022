import time
lines = open('eight\input.txt').readlines()

def transpose(matrix):
    newMatrix = []
    for element in matrix[0]:
        newMatrix.append([])
    for row in matrix:
        for elementIndex in range(len(row)):
            newMatrix[elementIndex].append(row[elementIndex])
    return newMatrix

def countVisibles(map):
    sum = 0
    for row in map:
        for tree in row:
            sum += tree['visibleH'] or tree['visibleV']
    return sum        

def visibilityTwoDirections(map, orientation):
    for rowIndex in range(len(map)):
        row = map[rowIndex]
        for treeIndex in range(len(row)):
            tree = row[treeIndex]
            visibleBehind = True 
            for otherTree in row[:treeIndex]:
                if otherTree['height'] >= tree['height']:
                    visibleBehind = False
                    break
            visibleFront = True 
            for otherTree in row[treeIndex + 1:]:
                if otherTree['height'] >= tree['height']:
                    visibleFront = False
                    break
            tree[orientation] = visibleFront or visibleBehind    

def scenicDistances(map, orientation):
    for rowIndex in range(len(map)):
        row = map[rowIndex]
        for treeIndex in range(len(row)):
            tree = row[treeIndex]
            elementsBehind = row[:treeIndex]
            elementsBehind.reverse()
            for otherTree in elementsBehind:
                tree[orientation][0] += 1
                if otherTree['height'] >= tree['height']:   
                    break
            for otherTree in row[treeIndex + 1:]:
                tree[orientation][1] += 1
                if otherTree['height'] >= tree['height']:   
                    break

def biggestScenicDistance(map):
    maxDist = 0
    for row in map:
        for tree in row:
            dist = tree['viewingDistancesH'][0] * tree['viewingDistancesH'][1] * tree['viewingDistancesV'][0] * tree['viewingDistancesV'][1]
            if dist > maxDist:
                maxDist = dist
    return maxDist

def identifyEdges(map):
    for rowIndex in range(len(map)):
        row = map[rowIndex]
        for treeIndex in range(len(row)):
            tree = row[treeIndex]
            tree['isEdge'] = rowIndex == 0 or rowIndex == (len(map) - 1) or treeIndex == 0 or treeIndex == (len(row) -1)

st = time.time()
treeMap = []
for line in lines:
    treeMap.append([])
    lineIndex = lines.index(line)
    for char in line[:-1]:
        treeMap[lineIndex].append({'height': int(char), 'visibleH' : False, 'visibleV': False, 'viewingDistancesH': [0,0], 'viewingDistancesV': [0,0], 'isEdge': False})

# Part 1
visibilityTwoDirections(treeMap, 'visibleH')
visibilityTwoDirections(transpose(treeMap), 'visibleV')
print(countVisibles(treeMap))

# Part 2
identifyEdges(treeMap)
scenicDistances(treeMap, 'viewingDistancesH')
scenicDistances(transpose(treeMap), 'viewingDistancesV')
print(biggestScenicDistance(treeMap))

et = time.time()

print(et-st, ' seconds')