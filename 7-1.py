file = open("7-1.in", "r")

for line in file:
    crabs = list(map(int, line.strip().split(',')))

max_ = max(crabs)
min_ = min(crabs)

min_fuel = 100000000000
for i in range(min_, max_):
    fuel = 0
    for crab in crabs:
        fuel += abs(i - crab)
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)
