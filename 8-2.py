'''
1 = 2 seg
-
7 = 3 seg
-
4 = 4 seg
-
2 = 5 seg
3 = 5 seg
5 = 5 seg
-
0 = 6 seg
6 = 6 seg
9 = 6 seg
-
8 = 7 seg

 aaaa
b    c
b    c
 dddd
e    f
e    f
 gggg
'''
file = open("8-1.in", "r")

total = 0
all_bars = set('abcdefg')
for line in file:
    pieces = line.strip().split(' | ')
    signals = pieces[0].split(' ')
    signals.sort(key=len)
    output = pieces[1].split(' ')

    seg = {}

    # two bars - maps to c/f
    s = set(signals[0])
    seg['c'] = s
    seg['f'] = s

    # three bars - maps to a/c/f
    s = set(signals[1])
    seg['a'] = s ^ seg['c']
    # A IS SET
    
    # four bars - maps to b/c/d/f
    s = set(signals[2])
    seg['b'] = s ^ seg['c']
    seg['d'] = s ^ seg['c']

    # six bars - maps to a/b/c/d/f/g OR a/b/d/e/f/g OR a/b/c/d/f/g
    s = set(signals[6])
    t = set(signals[7])
    u = set(signals[8])

    for x in seg['c']:
        if x in s and x in t and x in u and x not in seg['a']:
           seg['f'] = set(x)
           # F IS SET
    seg['c'] ^= seg['f']
    # C IS SET

    # five bars - maps to a/c/d/e/g OR a/c/d/f/g OR a/b/d/f/g
    s = set(signals[3])
    t = set(signals[4])
    u = set(signals[5])

    for x in seg['b']:
        if x in s and x in t and x in u:
           seg['d'] = set(x)
           # D IS SET
    seg['b'] ^= seg['d']
    # B IS SET

    # six bars - maps to a/b/c/d/f/g OR a/b/d/e/f/g OR a/b/c/d/f/g
    s = set(signals[6])
    t = set(signals[7])
    u = set(signals[8])

    check_set = all_bars ^ seg['a'] ^ seg['b'] ^ seg['c'] ^ seg['d'] ^ seg['f']
    for x in check_set:
        if x in s and x in t and x in u:
            seg['g'] = set(x)
            # G IS SET
    seg['e'] = check_set ^ seg['g']
    # E IS SET

    two_check = set().union(seg['a'],seg['c'],seg['d'],seg['e'],seg['g'])
    three_check = set().union(seg['a'],seg['c'],seg['d'],seg['f'],seg['g'])
    five_check = set().union(seg['a'],seg['b'],seg['d'],seg['f'],seg['g'])

    zero_check = set().union(seg['a'],seg['b'],seg['c'],seg['e'],seg['f'],seg['g'])
    six_check = set().union(seg['a'],seg['b'],seg['d'],seg['e'],seg['f'],seg['g'])
    nine_check = set().union(seg['a'],seg['b'],seg['c'],seg['d'],seg['f'],seg['g'])

    num = ''
    for o in output:
        s = set(o)
        if len(s) == 2:
            num += '1'
        elif len(s) == 3:
            num += '7'
        elif len(s) == 4:
            num += '4'
        elif len(s) == 7:
            num += '8'
        elif len(s) == 5:
            if len(s ^ two_check) == 0:
                num += '2'
            elif len(s ^ three_check) == 0:
                num += '3'
            elif len(s ^ five_check) == 0:
                num += '5'
        elif len(s) == 6:
            if len(s ^ zero_check) == 0:
                num += '0'
            elif len(s ^ six_check) == 0:
                num += '6'
            elif len(s ^ nine_check) == 0:
                num += '9'

    total += int(num)

print(total)
