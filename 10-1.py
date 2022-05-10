file = open("10-1.in", "r")


counts = {']': 0, ')': 0, '>': 0, '}': 0}
for line in file:
    parse = list(line.strip())

    next_close = []
    for token in parse:
        if token == '[': next_close.append(']')
        elif token == '(': next_close.append(')')
        elif token == '<': next_close.append('>')
        elif token == '{': next_close.append('}')
        elif token == ']':
            if next_close[-1] != ']':
                counts[token] += 1
                break
            else:
                next_close.pop()
        elif token == ')':
            if next_close[-1] != ')':
                counts[token] += 1
                break
            else:
                next_close.pop()
        elif token == '>':
            if next_close[-1] != '>':
                counts[token] += 1
                break
            else:
                next_close.pop()
        elif token == '}':
            if next_close[-1] != '}':
                counts[token] += 1
                break
            else:
                next_close.pop()

print(counts[')']*3 + counts[']']*57 + counts['}']*1197 + counts['>']*25137)
