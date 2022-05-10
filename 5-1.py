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
        continue

total = 0
for k in grid.keys():
    if grid[k] > 1:
        total += 1

print(total)
