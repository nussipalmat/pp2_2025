import os

lst = ['Test','file']
os.mkdir('task5')
with open('task5\\file.txt', 'w+') as file:
    for i in lst:
        file.write(f'{i}\n') 

file.close()