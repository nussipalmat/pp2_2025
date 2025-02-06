#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def even(n):
    for i in range(2, n + 1, 2): 
        yield i

n = int(input())
even_nums = even(n)
print(",".join(str(i) for i in even_nums))
        