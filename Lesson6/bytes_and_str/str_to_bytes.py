#!/usr/bin/python3

def str_to_byte(list):
    list_byte = []
    for s in list:
        for x in s:
            list_byte.append(ord(x))
    return list_byte

n = input('Введите Ваш текст:\n')
l = []
while n:
    l.append(n)
    n = input('Продолжите ввод или оставьте поле пустым что увидеть результат:\n')

print('Введённым Вами символам, соответствуют следующие байты (числа):\n',str_to_byte(l),sep='')
