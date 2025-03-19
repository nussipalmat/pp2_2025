import re

st = input()
match = 'a(b{2,3})'
if re.search(match,  st):
    print('YES') 
else:
    print('NO')