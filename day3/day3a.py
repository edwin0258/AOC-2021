data = open("data.txt", "r").read().splitlines()

def getMC(n):
    col = ""
    for row in data:
        col += row[n]

    ones = col.count('1')
    zeros = col.count('0')
    return int(ones > zeros) #return 1 or 0 for most common num

mcs = [getMC(n) for n in range(len(data[0]))] # most common in each col
lcs = [1 - n for n in mcs] # least common in each col

# convert to base 10, store in variables
gammaRate = int(''.join(map(str, mcs)), 2)
epsilonRate = int(''.join(map(str, lcs)), 2)

print(gammaRate, epsilonRate)
print(gammaRate * epsilonRate)
