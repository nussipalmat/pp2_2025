import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

bin_number = re.search(r'БИН (\d+)', text).group(1)
total = re.search(r'ИТОГО:\n([\d\s]+,\d+)', text).group(1)
date = re.search(r'Время: (.*)', text).group(1)

with open('almat.txt', 'w', encoding='utf-8') as file:
    file.write(f'BIN: {bin_number}\n')
    file.write(f'Total: {total}\n')
    file.write(f'Date: {date}\n')