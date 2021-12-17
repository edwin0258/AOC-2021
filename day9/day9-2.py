data = open('data.txt', 'r')

def formatData(data):
    output = []
    for line in data:
        # split into indv nums, convert all to int. Make sure appending a list
        lineHeights = list(line.strip())
        lineHeights = map(int, lineHeights)
        output.append(list(lineHeights))

    return output 


def determineLows(hts): # heights = hts
    lows = [] # 2d list [[low y, low x], etc..]
    for y, col in enumerate(hts):
        for x, h in enumerate(col):
            # val can't be greater than 9 so this is default
            [up, down, left, right] = [10,10,10,10] 
            # used for adjacent checks
            hasUp       = (y != 0)
            hasDown     = (y != len(hts) - 1)
            hasLeft     = (x != 0) 
            hasRight    = (x != len(col) - 1)

            # get adjacent heights 
            if(hasUp):      up      = hts[y-1][x]
            if(hasDown):    down    = hts[y+1][x]
            if(hasLeft):    left    = hts[y][x-1]
            if(hasRight):   right   = hts[y][x+1]

            # low flag
            isLow = True

            # test if height is lower than all directions or not
            for d in [up, down, left, right]:
                if (h >= d):
                   isLow = False 

            if(isLow): # record coords at each low 
                lows.append([y, x])

    return lows


def determineBasins(hts, lows):
    # internal functions to determine Basins
    def notNine(c): return hts[c[0]][c[1]] != 9
    # the coordinate is within grid of heights
    def inBounds(c):
        return ((c[0] >= 0 and c[1] >= 0) and
        (c[0] <= len(hts) - 1 and c[1] <= len(hts[0]) - 1))

    basins = [] # 2d list [[basin nums],[basin nums],etc..]

    #breakpoint()
    for low in lows:
        d = 'hor' 
        inBasin = [low] # current nums in basin
        addToBasin = [] # nums to be added to basin for next iteration
        # alternate between exploring hor and vert of all identified basin nums
        # keep exploring until nothing left to add
        while True:
            inBasin = inBasin + addToBasin # update in basin
            addToBasin = [] # make sure to clear this

            for c in inBasin:
                # -1 signals seach in direction has stopped
                vertSearch = {'up': 1, 'down': 1} # distance up/down from origin
                horSearch = {'left': 1, 'right': 1}
                dirCount = 4 # how many search directions still active

                # helper dirSearch used for each search direction
                def dirSearch(d, coord): 
                    if(inBounds(coord) and 
                       coord not in addToBasin + inBasin and 
                       notNine(coord)):

                        addToBasin.append(coord)
                        return 0 
                    d = -1
                    return -1

                while(dirCount > 0):

                    # vertical search
                    if(vertSearch['up'] != -1):
                        upPos = c[0] - vertSearch['up'] # y + how far up to search
                        upCoord = [upPos, c[1]]
                        dirCount += dirSearch(vertSearch['up'], upCoord)
                    
                    if(vertSearch['down'] != -1):
                        downPos = c[0] + vertSearch['down']
                        downCoord = [downPos, c[1]]
                        dirCount += dirSearch(vertSearch['down'], downCoord)

                    # horizontal search
                    if(horSearch['left'] != -1):
                        leftPos = c[1] - horSearch['left']
                        leftCoord = [c[0], leftPos]
                        dirCount += dirSearch(horSearch['left'], leftCoord)

                    if(horSearch['right'] != -1):
                        rightPos = c[1] + horSearch['right']
                        rightCoord = [c[0], rightPos]
                        dirCount += dirSearch(horSearch['right'], rightCoord)

            # nothing left to add, break
            if(len(addToBasin) == 0):
                break

        basins.append(inBasin)
    return basins


heights = formatData(data) 
lows = determineLows(heights)
basins = determineBasins(heights, lows)

# calculating/printing solution..

# get sorted list of basin sizes
basinSizes = sorted(list(map(lambda x: len(x), basins)))
total = 1;

for size in (basinSizes[-3:]):
    total *= size 

print(total)
