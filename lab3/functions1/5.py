from itertools import permutations

def permute(s):
    return [''.join(p) for p in permutations(s)]

str1=input()
print(permute(str1))