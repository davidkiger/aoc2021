file = open("6-1.in", "r")

for line in file:
    fish = list(map(int, line.strip().split(',')))

days = 80
for i in range(days):
    new_fish = []
    for x in range(len(fish)):
        if fish[x] == 0:
            fish[x] = 6
            new_fish.append(8)
        else:
            fish[x] -= 1
    fish.extend(new_fish)

print(len(fish))
