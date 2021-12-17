f = open('data.txt', 'r')

charPoints = {')': 3, ']': 57, '}': 1197, '>': 25137}
# counts of each illegal char found
illegalChars = {')': 0, ']': 0, '}': 0, '>': 0}
for l in f:
    chars = list(l)
    # push/pop to match opening/closing braces
    charStack = []
    opening = ['(','[','{','<']
    closing = [')',']','}','>']
    mappings = {')': '(', ']': '[', '}': '{', '>': '<'}
    for c in chars:
        if c in opening:
            charStack.append(c)
        if c in closing:
            if(len(charStack) > 0):
                close = charStack.pop()
                if(mappings[c] != close):
                    illegalChars[c] += 1
                    break
            else:
                print('NOT ENOUGH CHARS')
                break

# print solution
total = 0
for c in illegalChars:
   total += (illegalChars[c] * charPoints[c]) 

print(total)

