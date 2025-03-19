import re

st = input()
match = r'a(.*)(b$)'
if re.search(match,  st):
    print('YES') 
else:
    print('NO')