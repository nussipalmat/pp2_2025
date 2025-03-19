import re

st = input()
match = r'[A-Z]+[a-z]+'
seq = re.findall(match,  st)

if seq:
    print(seq) 
else:
    print('NO')