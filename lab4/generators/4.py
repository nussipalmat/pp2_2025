#Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

#Create a generator that generates the squares of numbers up to some number N.

def squar_gen(a,b):
    for i in range(a,b+1): 
        yield i**2
        
a = int(input())
b = int(input())
for i in squar_gen(a,b):
    print(i, end = ' ')