file = open("8-1.in", "r")

count = 0
for line in file:
    pieces = line.strip().split(' | ')
    signals = pieces[0].split(' ')
    output = pieces[1].split(' ')

    for o in output:
        s = set(o)
        if len(s) == 2 or len(s) == 4 or len(s) == 3 or len(s) == 7:
            count += 1

print(count)
