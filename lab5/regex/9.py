import re

st = input()

splitted = re.findall('[A-Z][^A-Z]*', st)

print(' '.join(splitted))