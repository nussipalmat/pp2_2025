import re

st = input()

rep = re.sub('[  . ,]',  ':', st)
if rep:
    print(rep) 
else:
    print('NO')