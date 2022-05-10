depths = [int(x.strip()) for x in open('1-1.in').readlines()]

increases = 0
for i in range(3, len(depths)):
	a = depths[i-3] + depths[i-2] + depths[i-1]
	b = depths[i-2] + depths[i-1] + depths[i]
	if b > a:
		increases += 1

print(increases)
