f = open('sonarSweep.txt', 'r')

[count, prev] = [0, 0]

for line in f:
    if prev < int(line):
        count += 1
    prev = int(line)

print(count - 1) # don't count first increase
