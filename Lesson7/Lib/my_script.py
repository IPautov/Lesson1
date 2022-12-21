#!/usr/bin/python3

import my_func

try:
    n = int(input('Введите номер элемента последовательности Фибоначчи:\n'))
except:
    print('Нужно ввести целое положительное число')
    exit()
if n < 0:
    print('Нужно ввести целое положительное число')
    exit()
print(f'{n}-ый элемент последовательности Фибоначчи равен {my_func.fibonacci(n)}')

password = input('Введите Ваш пароль:\n')

if my_func.check_password(password):
    print('Хороший пароль')
else:
    print('Плохой пароль')
