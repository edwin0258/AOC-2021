f = open('data.txt', 'r').readline().strip().split(',')
f = list(map(int, f))
fish = {}
newFish = {} # new fish to be added to fish after they grow up 
adultCycle = 6
babyCycle = 8
days = 256

# count fish in groups to reduce calculation time
for x in range(0, adultCycle+1):
    fish[x] = 0
for x in range(3, babyCycle+1):
    newFish[x] = 0

for fi in f:
    fish[fi] += 1

def rotateLeft(d): # rotate values to left in dict, left most is put on right 
    tempDict = {}
    for k in d:
        nextK = k+1
        if(nextK in d):
            tempDict[k] = d[nextK]
        else:
            tempDict[k] = d[next(iter(d))]
    return tempDict 

def sumKeys(d):
    t = 0
    for k in d:
        t += d[k]
    return t

for d in range(0, days):
    fish = rotateLeft(fish)
    newFish = rotateLeft(newFish)
    fish[2] += newFish[8] # any new fish with an 8 is no longer new (becomes a 2 fish)
    newFish[8] = 0 # remove new fish with 8, no longer new
    newFish[8] = fish[6] # any fish with a 6 creates a new fish
    
print(sumKeys(fish) + sumKeys(newFish))
