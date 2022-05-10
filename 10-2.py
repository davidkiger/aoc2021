file = open("10-1.in", "r")

counts = {']': 0, ')': 0, '>': 0, '}': 0}
scores = []
for line in file:
    error = False
    parse = list(line.strip())

    next_close = []
    for token in parse:
        if error:
            break

        if token == '[': next_close.append(']')
        elif token == '(': next_close.append(')')
        elif token == '<': next_close.append('>')
        elif token == '{': next_close.append('}')
        elif token == ']':
            if next_close[-1] != ']':
                counts[token] += 1
                error = True
            else:
                next_close.pop()
        elif token == ')':
            if next_close[-1] != ')':
                counts[token] += 1
                error = True
            else:
                next_close.pop()
        elif token == '>':
            if next_close[-1] != '>':
                counts[token] += 1
                error = True
            else:
                next_close.pop()
        elif token == '}':
            if next_close[-1] != '}':
                counts[token] += 1
                error = True
            else:
                next_close.pop()

    if not error:
        score = 0
        next_close.reverse()
        for x in next_close:
            score *= 5
            if x == ')': score += 1
            elif x == ']': score += 2
            elif x == '}': score += 3
            elif x == '>': score += 4
        scores.append(score)

scores.sort()
print(scores[len(scores)//2])
