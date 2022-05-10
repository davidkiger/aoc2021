file = open("9-1.in", "r")

hmap = []
for line in file:
    hmap.append(list(map(int, line.strip())))

def fill(x,y,hmap):
    count = 0
    if hmap[y][x] == 9:
        return count
    elif hmap[y][x] == -1:
        return count
    else:
        count += 1
        hmap[y][x] = -1
        if (y+1 != y_max):
            count += fill(x,y+1,hmap)
        if (y != 0):
            count += fill(x,y-1,hmap)
        if (x+1 != x_max):
            count += fill(x+1,y,hmap)
        if (x != 0):
            count += fill(x-1,y,hmap)
        return count

y_max = len(hmap)
x_max = len(hmap[0])
counts = []
for y in range(y_max):
    for x in range(x_max):
        counts.append(fill(x,y,hmap))

counts.sort(reverse=True)
print(counts[0] * counts[1] * counts[2])
