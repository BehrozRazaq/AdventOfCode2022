file = open("four\input.txt")
pairs = file.readlines()

def oneContainsSomeOfOther(left, right):
    for section in range(left[0], left[1] + 1):
        if section >= right[0] and section <= right[1]:
            return True

contained = 0
for pair in pairs:
    left = pair.split(',')[0].split('-')
    right = pair.split(',')[1].split('-')

    left = (int(left[0]), int(left[1]))
    right = (int(right[0]), int(right[1]))
    if oneContainsSomeOfOther(left, right):
        contained += 1

print(contained)