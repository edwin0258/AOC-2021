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
    lows = []
    for y, col in enumerate(hts):
        for x, h in enumerate(col):
            # val can't be greater than 9 so this is default
            [up, down, left, right] = [10,10,10,10] 

            # get adjacent heights 
            if(y != 0):
                up = hts[y-1][x]
            if(y != len(hts) - 1):
                down = hts[y+1][x]
            if(x != 0):
                left = hts[y][x-1]
            if(x != len(col) - 1):
                right = hts[y][x+1]

            # low flag
            isLow = True

            # test if height is lower than all directions or not
            for d in [up, down, left, right]:
                if (h >= d):
                   isLow = False 

            if(isLow):
                lows.append(h)
    return lows

heights = formatData(data) 
lows = determineLows(heights)

# print solution
print(sum(list(map(lambda x: x + 1, lows))))
