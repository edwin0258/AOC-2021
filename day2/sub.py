f = open('data.txt', 'r')

[hor, vert] = [0, 0]
for x in f:
    [d, i] = x.split(' ')
    if d == "forward":
        hor += int(i)
    elif d == "down":
        vert += int(i)
    elif d == "up":
        vert -= int(i)

print("HOR", hor)
print("VERT", vert)

print(hor * vert)
