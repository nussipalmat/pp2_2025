def spy_game(nums):
    count = 0

    for i in nums:
        if i == 0 and count == 0:
            count = 1
        elif i == 0 and count == 1:
            count = 2
        elif i == 7 and count == 2:
            count = 3
            
    return count == 3


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
