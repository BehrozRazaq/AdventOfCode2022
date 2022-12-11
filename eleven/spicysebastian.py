class Monkey:
    def __init__(self, items, recipiants):
        self.items = items
        self.recipiants = []
        for recipiant in recipiants:
            self.recipiants.append(recipiant) 
        self.inspectionTimes = 0
    
    def inspectItems(self):
        for item in self.items:
            cItem = self.operation(item) % 9699690
            if cItem < 0 :
                print('BIG OOF') 
            monkeys[self.recipiants[self.test(cItem)]].items.append(cItem)
            self.inspectionTimes += 1
        self.items.clear()
    
    def operation(self, item):
        if monkeys.index(self) == 0:
            return (item * 5)  
        elif monkeys.index(self) == 1:
            return (item + 5) 
        elif monkeys.index(self) == 2:
            return (item * 19) 
        elif monkeys.index(self) == 3:
            return (item + 7) 
        elif monkeys.index(self) == 4:
            return (item + 2)
        elif monkeys.index(self) == 5:
            return (item + 1) 
        elif monkeys.index(self) == 6:
            return (item * item) 
        else:
            return (item + 4) 
        
    def test(self, item):
        if monkeys.index(self) == 0:
            return item % 11 == 0
        elif monkeys.index(self) == 1:
            return item % 19 == 0
        elif monkeys.index(self) == 2:
            return item % 5 == 0
        elif monkeys.index(self) == 3:
            return item % 3 == 0
        elif monkeys.index(self) == 4:
            return item % 13 == 0
        elif monkeys.index(self) == 5:
            return item % 17 == 0
        elif monkeys.index(self) == 6:
            return item % 7 == 0
        else:
            return item % 2 == 0
def parseMonkeys():
    arguments = []
    recipiants = []
    for line in notes:
        if line == '\n':
            arguments.append(recipiants)            
            monkeys.append(Monkey(*arguments))
            recipiants.clear()
            arguments.clear()
            continue
        line = line.split()
        match line[0]:
            case 'Starting':
                items = []
                for word in line[2:-1]:
                    items.append(int(word[:-1]))
                items.append(int(line[-1]))
                arguments.append(items)
            case 'If':
                recipiants.append(int(line[-1]))
                recipiants.reverse()
                
notes = open('eleven\input.txt').readlines()

monkeys = []
parseMonkeys()

for round in range(10000):
    for monkey in monkeys:
        monkey.inspectItems()

monkeBussiness = []
for monkey in monkeys:
    monkeBussiness.append(monkey.inspectionTimes)

monkeBussiness.sort()
print(monkeBussiness)
print(monkeBussiness[-2]*monkeBussiness[-1])