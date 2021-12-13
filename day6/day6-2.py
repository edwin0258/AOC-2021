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
for x in range(adultCycle-1, babyCycle+1):
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
    fish[adultCycle-2] += newFish[babyCycle] # any new fish that has max num key is not new (becomes adult)
    newFish[babyCycle] = 0 # remove new fish with max key, no longer new
    newFish[babyCycle] = fish[adultCycle] # any fish with a max adult key creates a new fish
    
print(sumKeys(fish) + sumKeys(newFish))
