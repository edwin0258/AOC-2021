from copy import copy, deepcopy

data = open('data.txt', 'r')

floor = []
floorWidth = 0
floorHeight = 0

for line in data:
    floor.append(list(line.strip()))


floorWidth = len(floor[0])
floorHeight = len(floor)

moves = 1 # count how many moves in one step

# returns positions of > and V
def getPositions(floor):
    [easts, souths] = [[],[]]
    funcs = {'.': (lambda x, y: False), '>': (lambda x, y: easts.append([x, y])),
            'v': (lambda x, y: souths.append([x , y]))}
    for y, row in enumerate(floor):
        for i, spot in enumerate(row):
            funcs[spot](i, y)

    return [easts, souths]
        

def checkPosition(x, y, floor):
    return floor[y][x] == '.'

def updateEasts(floor, easts, f):
    moves = 0
    for e in easts:
        [x, y] = [e[0],e[1]]

        if(x == floorWidth - 1):
            if(checkPosition(0,y, f) == True):
                floor[y][x] = '.'
                floor[y][0] = '>'
                moves += 1
        else:
            if(checkPosition(x+1, y, f) == True):
                floor[y][x] = '.'
                floor[y][x+1] = '>'
                moves += 1

    return [moves, floor]


def printFloor(floor):
    for r in floor:
        print(''.join(r))
    print('\n')


def updateSouths(floor, souths, f):
    moves = 0
    for e in souths:
        [x, y] = [e[0],e[1]]

        if(y == floorHeight - 1):
            if(checkPosition(x,0, f) == True):
                floor[y][x] = '.'
                floor[0][x] = 'v'
                moves += 1
        else:
            if(checkPosition(x, y+1, f) == True):
                floor[y][x] = '.'
                floor[y+1][x] = 'v'
                moves += 1

    return [moves, floor]

steps = 0
while moves > 0:
    steps += 1
    moves = 0

    [easts, souths] = getPositions(floor)
    [eastMoves, floor] = updateEasts(floor, easts, deepcopy(floor))
    [southMoves, floor] = updateSouths(floor, souths, deepcopy(floor))
    moves += eastMoves
    moves += southMoves

print(steps)
