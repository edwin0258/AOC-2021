fish = open('data.txt', 'r').readline().strip().split(',')
fish = list(map(int, fish))

days = 80 # how many days to run simulation
newFish = [] # new fish to be added to fish after they grow up 

for d in range(0, days):
    fish = [f - 1 if f > 0 else 6 for f in fish]
    fish = fish + [2] * newFish.count(3)
    newFish = [f - 1 for f in newFish if f != 3]
    newFish = newFish + [8] * fish.count(6)

print(len(fish) + len(newFish))

