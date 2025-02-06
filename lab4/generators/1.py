#Create a generator that generates the squares of numbers up to some number N.

def squar_gen(n):
    for i in range(n): 
        yield i**2
        
n = int(input())

for i in squar_gen(n):
    print(i, end = ' ')
