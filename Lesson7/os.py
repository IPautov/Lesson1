#!/usr/bin/python3

import os

print(f"Имя операционной системы: {os.name}")
print(f"Имя пользователя, вошедшего в терминал: {os.getlogin()}")
print('Список файлов и папок в текущей дирректории:')
dirs = os.listdir(path='.')
for file in dirs:
    print(file)
