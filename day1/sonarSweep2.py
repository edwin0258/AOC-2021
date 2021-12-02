f = open('sonarSweep.txt', 'r')

[count, prev, windowSize, i, winSum] = [0, 0, 3, 0, 0]

dataArr = []
for line in f:
    dataArr.append(int(line))

windowArr = []
for i, x in enumerate(dataArr):
    curr = sum(dataArr[i:i+windowSize])
    windowArr.append(curr)

    if prev < curr:
        count += 1 
    prev = curr 
    
print(count - 1) # don't count first increase
