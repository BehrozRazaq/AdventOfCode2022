file = open("four\input.txt")
pairs = file.readlines()

def oneContainsOther(left, right):
    if (left[0] >= right[0] and left[1] <= right[1]) or (left[0] <= right[0] and left[1] >= right[1]): 
        return True

fullyContained = 0
for pair in pairs:
    left = pair.split(',')[0].split('-')
    right = pair.split(',')[1].split('-')

    left = (int(left[0]), int(left[1]))
    right = (int(right[0]), int(right[1]))
    if oneContainsOther(left, right):
        fullyContained += 1

print(fullyContained)
