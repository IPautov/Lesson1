#!/usr/bin/python3

def str_to_byte(list):
    """Перевод строки в байт код

    Принимает:
        строку
    Возвращает:
        список байт кода

    """

    list_byte = []
    for s in list:
        for x in s:
            list_byte.append(ord(x))
    return list_byte

n = input('Введите Ваш текст:\n')
sym = []
while n:
    sym.append(n)
    n = input('Продолжите ввод или оставьте поле пустым чтобы увидеть результат:\n')

print('Введённым символам, соответствуют байты (числа):\n', str_to_byte(sym))


