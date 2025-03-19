import re

st = input()

splitted = re.split('_', st)

for i in range(len(splitted)):
    splitted[i] = splitted[i].capitalize()

print(''.join(splitted))