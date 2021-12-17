f = open('data.txt', 'r')

charPoints = {')': 1, ']': 2, '}': 3, '>': 4}
autoCompletes = []
# counts of each illegal char found
for l in f:
    chars = list(l)
    # push/pop to match opening/closing braces
    charStack = []
    autoComplete = []
    opening = ['(','[','{','<']
    closing = [')',']','}','>']
    mappings = {')': '(', ']': '[', '}': '{', '>': '<'}
    revMappings = {'(':')', '[':']', '{':'}', '<':'>'}
    for c in chars:
        if c in opening:
            charStack.append(c)
        if c in closing:
            if(len(charStack) > 0):
                close = charStack.pop()
                if(mappings[c] != close):
                    # discard corrupted
                    charStack = []
                    break
            else:
                break

    while(len(charStack) != 0):
        # autocomplete
        opn = charStack.pop() #open
        autoComplete.append(revMappings[opn])

    if(len(autoComplete) != 0):
        autoCompletes.append(autoComplete)

# print solution
vals = [] # total values for each line
for ac in autoCompletes:
    total = 0
    for c in ac:
        total *= 5
        total += charPoints[c]
    vals.append(total)

# print middle value
print(sorted(vals)[int((len(vals) - 1) / 2)])
