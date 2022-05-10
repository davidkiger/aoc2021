file = open("3-1.in", "r")

nums = []
for line in file:
    digits = list(line.strip())
    nums.append(digits)

l = len(nums[0])

gamma = []
for i in range(l):
    digits = [x[i] for x in nums]
    if digits.count('1') >= digits.count('0'):
        gamma.append('1')
    else:
        gamma.append('0')

epsilon = []
for i in range(l):
    if gamma[i] == '1':
        epsilon.append('0')
    else:
        epsilon.append('1')

print(int(''.join(gamma), 2)*int(''.join(epsilon), 2))
