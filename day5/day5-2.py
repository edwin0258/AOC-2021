f = open('data.txt', 'r')

coords = [] # keep track of coords with atleast 1 vent

def storeRange(rg, const, d, coords, v=0): # (range, constant num, dir, coords, up/down (diag))
    for c in rg:
        coord = (str(c) + ',' + str(const)) if (d == 0 or d == 2) else (str(const) + ',' + str(c))
        coords.append(coord)

        if(v == 1): # down
            const += 1
        elif(v == 2):
            const -= 1

def calculateSolution(coords):
    coordOcs = {} # count how many times (occurences) a coord appears
    count = 0 # for counting coords with 2 or more ocs

    for c in coords:
        if c in coordOcs:
            coordOcs[c] += 1
        else:
            coordOcs[c] = 1

    for c in coordOcs:
        if coordOcs[c] > 1:
            count += 1
    
    print(count)

for l in f:
    [c1, c2] = l.split('->')
    [c1, c2] = [list(map(int, c1.split(','))), list(map(int, c2.split(',')))]

    if(c1[0] != c2[0] and c1[1] != c2[1]):
        # diag down or up
        if(c1[0] < c2[0]):
            r = range(c1[0], c2[0]+1)
            yStart = c1[1]
            if (c1[1] < c2[1]):# down
                v = 1
            else: # up
                v = 2
        else:
            r = range(c2[0], c1[0]+1)
            yStart = c2[1]
            v = 1 if(c2[1] < c1[1]) else 2

        storeRange(r, yStart, 2, coords, v) # const will change in this case

    # hor or vert
    elif(c1[0] != c2[0]):
        [x1, x2] = sorted([c1[0], c2[0]]) # smallest first
        storeRange(range(x1, x2+1), c1[1], 0, coords)
        
    elif(c1[1] != c2[1]):
        [y1, y2] = sorted([c1[1], c2[1]])
        storeRange(range(y1, y2+1), c1[0], 1, coords)


calculateSolution(coords)
