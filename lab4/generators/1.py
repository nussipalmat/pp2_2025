#Create a generator that generates the squares of numbers up to some number N.

def squar_gen(n):
    for i in range(n): 
        return i**2
        
n = int(input())

print(squar_gen(n))
