file = open("6-1.in", "r")

for line in file:
    fish = list(map(int, line.strip().split(',')))

fish_buckets = {}
for i in range(9):
    fish_buckets[i] = fish.count(i)

days = 256
for i in range(days):
    new_buckets = {}
    for i in range(8):
        new_buckets[i] = fish_buckets[i+1]
    new_buckets[6] += fish_buckets[0]
    new_buckets[8] = fish_buckets[0]

    fish_buckets = new_buckets
    
print(sum(fish_buckets.values()))
