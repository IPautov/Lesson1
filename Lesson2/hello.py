#!/usr/bin/python3
import random

name = input('Как Вас зовут?\n')
greeting = ['Привет', 'Добрый день', 'Здрасвтуй','Ассалам Алейкум','Хай']
print(random.choice(greeting),', ', name, sep = '')
