file = open("5-1.in", "r")
lines = []
for line in file:
    (start, end) = list(line.strip().split(' -> '))
    lines.append([start, end])

grid = {}
for line in lines:
    start = list(map(int, line[0].split(',')))
    end = list(map(int, line[1].split(',')))

    if start[0] == end[0]:
        rng = (start[1], end[1])
        for i in range(min(rng), max(rng)+1):
            try:
                grid[(start[0],i)] += 1
            except: 
                grid[(start[0],i)] = 1
    elif start[1] == end[1]:
        rng = (start[0], end[0])
        for i in range(min(rng), max(rng)+1):
            try:
                grid[(i,start[1])] += 1
            except: 
                grid[(i,start[1])] = 1
    else:
        if (start[0] < end[0]):
            xd = 1
        else:
            xd = -1
        if (start[1] < end[1]):
            yd = 1
        else:
            yd = -1

        x = start[0]
        y = start[1]
        while x != end[0]:
            try:
                grid[(x,y)] += 1
            except: 
                grid[(x,y)] = 1
            x += xd 
            y += yd
        try:
            grid[(x,y)] += 1
        except: 
            grid[(x,y)] = 1
                    

total = 0
for k in grid.keys():
    if grid[k] > 1:
        total += 1

print(total)
