file = open("input.txt")
input = file.readlines()

def rpsRound(opp, me):
    oppArr = ['A', 'B', 'C']
    meArr = ['X', 'Y', 'Z']
    if oppArr.index(opp) == ((meArr.index(me) + 1) % 3):
        return meArr.index(me) + 1
    elif meArr.index(me) == ((oppArr.index(opp) + 1) % 3):
        return meArr.index(me) + 1 + 6
    else:
        return meArr.index(me) + 1 + 3

totScore = 0
for round in input:
    totScore += rpsRound(round[0], round[-2])
print(totScore)