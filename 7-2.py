file = open("7-1.in", "r")

for line in file:
    crabs = list(map(int, line.strip().split(',')))

max_ = max(crabs)
min_ = min(crabs)

min_fuel = 100000000000
for i in range(min_, max_):
    fuel = 0
    for crab in crabs:
        fuel += sum(range(0, abs(i - crab)+1))
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)
