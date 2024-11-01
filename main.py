# Apollos Eastman
# Nov 1 2024
# Range function

# 4-3 Counting to Twenty
for i in range(1,21):
    print(i)

# 4-4 One Million
nums = list(range(1,1000001))
for i in nums:
    print(i)

# 4-5 Summing a Million
nums1 = list(range(1,1000001))
sum = sum(nums1)
print(f'Minimum: {min(nums1)}')
print(f'Maximum: {max(nums1)}')
print(f'sum: {sum}')

# 4-6 Odd Numbers
odd_nums = list(range(1,21,2))
for i in odd_nums:
    print(i)

# 4-7 Threes
threes = list(range(3,31,3))
for i in threes:
    print(i)

# 4-8 Cubes
cubes = list(i**3 for i in range(1, 11))
for i in cubes:
    print(i)
