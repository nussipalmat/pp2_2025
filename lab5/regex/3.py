import re

st = input()
match = r'[a-z]+_[a-z]+'
seq = re.findall(match,  st)

if seq:
    print(seq) 
else:
    print('NO')