import functools

data = open('data.txt', 'r')

# Track coords by seperate row/col dicts
# This should allow for easier manipulation
# when folding coords along x/y axis 
dotCoordsX = {} # {X: [y1,y2,y3], X2:...} 
dotCoordsY = {} # {Y: [x1,x2,x3], Y2:...}
folds = [] # [[x/y, foldPos],[x/y, foldPos]...]
coordData = True

for l in data:
    if coordData:
        if(l == '\n'):
            # end of coordinate data
            coordData = False
        else:
            [x, y] = [int(n) for n in l.strip().split(',')]

            if x in dotCoordsX:
                dotCoordsX[x].append(y)
            else:
                dotCoordsX[x] = [y]

            if y in dotCoordsY:
                dotCoordsY[y].append(x)
            else:
                dotCoordsY[y] = [x]

        continue


    # now collecting fold info 
    fold = l.strip().split('=')
    folds.append([fold[0][-1], int(fold[1])])

# make a fold given a dotCoord dict, foldPos 
def makeFold(dotCoords, foldPos):
    dotCoordsTemp = dict(dotCoords)
    for n in dotCoords:
        # get new n pos from folding up or left
        if n > foldPos:
            newN = foldPos - (n - foldPos)

            if newN in dotCoordsTemp:
                dotCoordsTemp[newN] += dotCoordsTemp[n]
            else:
                dotCoordsTemp[newN] = dotCoordsTemp[n]
            dotCoordsTemp.pop(n, None)

            # remove any duplicates from overlapping points
            dotCoordsTemp[newN] = list(set(dotCoordsTemp[newN]))
    return dotCoordsTemp

# after each fold, it is necessary both dotCoord dicts are updated
# this is used for that
def transposeDotCoords(dotCoords):
    dotCoordsTransposed = {} 
    for x in dotCoords:
        for y in dotCoords[x]:
            if y in dotCoordsTransposed:
                dotCoordsTransposed[y].append(x)
            else:
                dotCoordsTransposed[y] = [x]
    return dotCoordsTransposed


    
def makeFolds(dotCoordsX, dotCoordsY, folds):
    for fold in folds:
        [foldDir, foldPos] = fold
        if(foldDir == 'y'):
            # folding bottom upwards (y-dir)
            dotCoordsY = makeFold(dotCoordsY, foldPos) 
            dotCoordsX = transposeDotCoords(dotCoordsY)

        if(foldDir == 'x'):
            # folding right lefwards (x-dir)
            dotCoordsX = makeFold(dotCoordsX, foldPos)
            dotCoordsY = transposeDotCoords(dotCoordsX)

        # only perform 1st fold for part 1
        break

    # print solution
    t = functools.reduce(lambda total, r: total + len(dotCoordsY[r]), dotCoordsY, 0)
    print(t)

makeFolds(dotCoordsX, dotCoordsY, folds)
