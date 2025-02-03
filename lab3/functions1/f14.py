import math
def grams_to_ounces(weight):
    return weight*28.3495231

def fahr_to_cent(temp_f):
    return ((5 / 9) * (temp_f-32))

def vol_sph(rad):
    return ((4/3) * math.pi * rad**3)

def histogram(numbers):
    for i in numbers:
        print('*' * i)

a=int(input("""Pick a number between 1 and 4 to run funtions
        1- To turn grams to ounces
        2- To turn F to C
        3- To find the volume of the sphere
        4- To make histogram
        any other input to exit.
        """))
if a==1:
    gr=float(input("input grams: "))
    print(grams_to_ounces(gr))
elif a==2:
    f=float(input("input F: "))
    print(fahr_to_cent(f))
elif a==3:
    r=float(input("input R of a sphere: "))
    print(vol_sph(r))
elif a==4:
    st=input("I need numbers with spaces: ")
    l=st.split(" ")
    for i in range(len(l)):
        l[i]=int(l[i])
    histogram(l)
else:
    print("Goodbye")


