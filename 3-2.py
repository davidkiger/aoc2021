file = open("3-1.in", "r")

nums = []
for line in file:
    digits = list(line.strip())
    nums.append(digits)

l = len(nums[0])

these_nums = nums.copy()
for i in range(l):
    digits = [x[i] for x in these_nums]
    if digits.count('1') >= digits.count('0'):
        these_nums = [x for x in these_nums if x[i] == '1']
    else:
        these_nums = [x for x in these_nums if x[i] == '0']

    if len(these_nums) == 1:
        oxygen = these_nums[0]
        break

these_nums = nums.copy()
for i in range(l):
    digits = [x[i] for x in these_nums]
    if digits.count('1') >= digits.count('0'):
        these_nums = [x for x in these_nums if x[i] == '0']
    else:
        these_nums = [x for x in these_nums if x[i] == '1']

    if len(these_nums) == 1:
        co2 = these_nums[0]
        break

print(int(''.join(oxygen), 2)*int(''.join(co2), 2))
