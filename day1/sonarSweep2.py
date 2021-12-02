f = open('sonarSweep.txt', 'r')

[count, prev, windowSize] = [0, 0, 3]

dataArr = [int(line) for line in f]

for i, x in enumerate(dataArr):
    curr = sum(dataArr[i:i+windowSize])
    if prev < curr:
        count += 1 
    prev = curr 
    
print(count - 1) # don't count first increase
