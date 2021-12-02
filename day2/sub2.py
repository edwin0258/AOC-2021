f = open('data.txt', 'r')

[hor, vert, aim] = [0, 0, 0]
for x in f:
    [d, i] = x.split(' ')
    if d == "forward":
        hor += int(i)
        vert += aim * int(i)
    elif d == "down":
        aim += int(i)
    elif d == "up":
        aim -= int(i)

print("HOR", hor)
print("VERT", vert)

print(hor * vert)
