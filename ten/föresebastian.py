import time as t
import os
def updateSignalStrength():
    relevantCycles = [20,60,100,140,180,220]
    for relevantCycle in relevantCycles:
        if system['cycle'] == relevantCycle:
            hist.append((system['cycle'], system['X']))

def printSumOfSignalStrengths():
    sum = 0
    for point in hist:
        sum += point[0] * point[1]
    print('Sum of signal strengths:', sum)

def populateCRT():
    for row in range(6):
        system['CRT'].append('')

def updateCRT():
    if int(system['cycle'] % 40) - 1 in range(system['X'] - 1, system['X'] + 2):

        system['CRT'][int((system['cycle']-1) / 40)] +=  '#'
    else:
        system['CRT'][int((system['cycle']-1) / 40)] += '.'
    printCRT()

def printCRT():
    t.sleep(0.005)
    os.system('cls')
    for row in system['CRT']:
        print(row)
    print()

def nextCycle():
    system['cycle'] += 1
    updateCRT()
    updateSignalStrength()

def executeCommands():
    for command in commands:
        match command[:-1].split():
            case 'addx', V:
                V = int(V) 
                nextCycle()
                nextCycle()
                system['X'] += V
            case _: 
                nextCycle()

commands = open('ten\input.txt').readlines()

system = {'X': 1, 'cycle': 0, 'CRT': []}
hist = [(0,1)]

populateCRT()
executeCommands()

printSumOfSignalStrengths()