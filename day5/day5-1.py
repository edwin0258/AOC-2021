f = open('data.txt', 'r')

coords = [] # keep track of coords with atleast 1 vent

def storeRange(rg, const, d, coords): # (range, constant num, dir, coords)
    for c in rg:
        coord = (str(c) + ',' + str(const)) if (d == 0) else (str(const) + ',' + str(c))
        coords.append(coord)

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
    #print(int(c1[0]), int(c2[0]))

    if(c1[0] != c2[0] and c1[1] != c2[1]):
        continue # ignore diag for now

    # hor or vert
    elif(c1[0] != c2[0]):
        if(c1[0] < c2[0]):
            storeRange(range(c1[0], c2[0]+1), c1[1], 0, coords)
        else:
            storeRange(range(c2[0], c1[0]+1), c1[1], 0, coords)
        
    elif(c1[1] != c2[1]):
        if(c1[1] < c2[1]):
            storeRange(range(c1[1], c2[1]+1), c1[0], 1, coords)
        else:
            storeRange(range(c2[1], c1[1]+1), c1[0], 1, coords)


calculateSolution(coords)
