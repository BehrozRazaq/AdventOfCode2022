file = open('seven\input.txt')
lines = file.readlines()

def sumOfLesserFiles(directory):
    res = 0
    for child in directory['dir']:
        if 'parent' in child.keys():
            res += sumOfLesserFiles(child)
    if directory['size'] <= 100000:    
        res += directory['size'] 
    return res

def smallestDeletableDirectory(directory, minSpace):
    smallestChild = 70000000
    if  directory['size'] >= minSpace:
        smallestChild = min(directory['size'], smallestChild)
    for child in directory['dir']:
        if 'parent' in child.keys():
            smallestChild = min(smallestDeletableDirectory(child, minSpace), smallestChild)                
    return smallestChild

files = {'name': '/', 'parent': '', 'size': 0,'dir': []}
currentDir = files
for line in lines: 
    splitLine = line.split()
    if splitLine[0] == '$':
        if splitLine[1] == 'cd':
            if splitLine[2] == '..':
                currentDir = currentDir['parent']
            elif splitLine[2] == '/':
                currentDir = files
            else:
                for dir in currentDir['dir']:
                    if dir['name'] == splitLine[2]:
                        currentDir = dir
    elif splitLine[0] == 'dir':
        currentDir['dir'].append({'name': splitLine[1], 'parent': currentDir, 'size': 0,'dir': []})
    else:
        currentDir['dir'].append({'name': splitLine[1], 'size': int(splitLine[0])})
        parentDir = currentDir
        while not parentDir == '':
            parentDir['size'] += int(splitLine[0])
            parentDir = parentDir['parent']
        
print(sumOfLesserFiles(files))

overusedSpace = files['size'] - 40000000
print(smallestDeletableDirectory(files, overusedSpace))