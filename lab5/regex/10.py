import re

st = input()

splitted = re.split(' ', st)

for i in range(len(splitted)):
    splitted[i] = splitted[i].lower()

print('_'.join(splitted))