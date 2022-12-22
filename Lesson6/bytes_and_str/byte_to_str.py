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

def byte_to_str(list):
    """Перевод байт кода в символы

    Принимает:
        Список байт кода
    Возвращает:
        Список символов

    """

    list_s = []
    for x in list:
        list_s.append(chr(x))
    return list_s

n = input('Введите Ваш текст:\n')
string = []
while n:
    string.append(n)
    n = input('Продолжите ввод или оставьте поле пустым что увидеть результат:\n')

print('Введённым символам соответствуют следующий байт код:\n',str_to_byte(string),sep='')
print('Результат выполнения обратной функции:\n',byte_to_str(str_to_byte(string)),sep='')

