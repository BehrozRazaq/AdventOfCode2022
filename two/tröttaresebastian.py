file = open("input.txt")
input = file.readlines()

def rpsRound(opp, me):
    oppArr = ['A', 'B', 'C']
    if me == 'X':
        return int((oppArr.index(opp) - 1) % 3) + 1
    elif me == 'Y':
        return oppArr.index(opp) + 1 + 3
    else:
        return int((oppArr.index(opp) + 1) % 3) + 1 + 6

totScore = 0
for round in input:
    totScore += rpsRound(round[0], round[-2])
print(totScore)