file = open("12-1.in", "r")

path = {}
for line in file:
    (a, b) = line.strip().split('-')
    if a in path.keys():
        path[a].append(b)
    else:
        path[a] = [b]

    if b in path.keys():
        path[b].append(a)
    else:
        path[b] = [a]

def step(key, p_str):
    if key == 'end':
        return p_str
    for x in path[key]:
        return p_str + ',' + step(x, p_str)

print(step('start', ''))
