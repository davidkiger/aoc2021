depths = [int(x.strip()) for x in open('1-1.in').readlines()]

increases = 0
for i in range(1, len(depths)):
	if depths[i] > depths[i-1]:
		increases += 1

print(increases)
