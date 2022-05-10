file = open("11-1.in", "r")

octo = []
for line in file:
    row = list(map(int, line.strip()))
    octo.append(row)

y_max = len(octo)
x_max = len(octo[0])

step = 1
while True:
    for y in range(y_max):
        for x in range(x_max):
            octo[y][x] += 1

    flash_count = 0
    flashed = True
    while flashed:
        flashed = False
        for y in range(y_max):
            for x in range(x_max):
                if octo[y][x] > 9:
                    flashed = True
                    flash_count += 1
                    octo[y][x] = -10000000
                    if (y+1 < y_max): octo[y+1][x] += 1
                    if (y-1 > -1):    octo[y-1][x] += 1
                    if (x+1 < x_max): octo[y][x+1] += 1
                    if (x-1 > -1):    octo[y][x-1] += 1

                    if (x-1 > -1 and y-1 > -1):       octo[y-1][x-1] += 1
                    if (x-1 > -1 and y+1 < y_max):    octo[y+1][x-1] += 1
                    if (x+1 < x_max and y-1 > -1):    octo[y-1][x+1] += 1
                    if (x+1 < x_max and y+1 < y_max): octo[y+1][x+1] += 1

    for y in range(y_max):
        for x in range(x_max):
            if octo[y][x] < 0:
                octo[y][x] = 0

    if flash_count == 100:
        print(step)
        exit()

    step += 1
