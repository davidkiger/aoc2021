file = open("2-1.in", "r")

inst = []
for line in file:
    (w, d) = line.strip().split(' ')
    d = int(d)
    inst.append((w, d))

depth = 0
pos = 0
aim = 0
for i in inst:
    if i[0] == 'forward':
        pos += i[1]
        depth += aim * i[1]
    elif i[0] == 'down':
        aim += i[1]
    elif i[0] == 'up':
        aim -= i[1]

print(depth * pos)
