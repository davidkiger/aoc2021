file = open("9-1.in", "r")

hmap = []
for line in file:
    hmap.append(list(map(int, line.strip())))

y_max = len(hmap)
x_max = len(hmap[0])
risk = 0
for y in range(y_max):
    for x in range(x_max):
        if ((y+1 == y_max or hmap[y][x] < hmap[y+1][x]) and
            (y-1 == -1    or hmap[y][x] < hmap[y-1][x]) and
            (x+1 == x_max or hmap[y][x] < hmap[y][x+1]) and
            (x-1 == -1    or hmap[y][x] < hmap[y][x-1])):
            risk += hmap[y][x]+1

print(risk)
