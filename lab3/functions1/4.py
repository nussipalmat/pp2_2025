def filter_prime(nums):
    nums = [int(n) for n in nums]  
    for i in range(2, int(max(nums) ** 0.5) + 1):  
        nums = [n for n in nums if n == i or (n % i != 0 and n != 1)]
    return nums

numbers_str = input()
nums = numbers_str.split(" ") 
print(filter_prime(nums))