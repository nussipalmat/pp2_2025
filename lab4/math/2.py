#Write a Python program to calculate the area of a trapezoid.
import math

print('Height: ', end = '')
height = int(input())
print('Base, first value: ', end = '')
base1 = int(input())
print('Base, second value: ', end = '')
base2 = int(input())

#print('Expected output: ', round(math.fsum([base1,base2]) * height / 2, 1))
print('Expected output: ', round((base1 + base2) * height / 2, 1))
