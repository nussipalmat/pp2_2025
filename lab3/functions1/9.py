import math
def vol_sph(rad):
    return ((4/3) * math.pi * rad**3)
r=float(input())
print(vol_sph(r))