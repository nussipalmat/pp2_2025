import re

st = input()
match = 'a(b*)'
if re.search(match,  st):
    print('YES') 
else:
    print('NO')