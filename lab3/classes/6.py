nums = [10, 17, 300, 47]

for i in range(2, int(max(nums)**0.5) + 1):
    nums = list(filter(lambda n: n == i or n % i != 0 and not n == 1, nums))

print(nums)
   