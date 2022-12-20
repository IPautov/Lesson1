#!/usr/bin/python3

def byte_to_str(list):
    list_s = []
    s = ''
    for x in list:
        list_s.append(chr(x))
    s = ''.join(list_s)
    return s

def byte_to_list(list):
    list_s = []
    s = ''
    for x in list:
        list_s.append(chr(x))
    return list_s

def int_plus(x):
    if x.isdigit():
        if 0 < float(x) <= 1114111:
            if float(x) * 10 % 10 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

n = input('Введите целое число в диапазоне от 0 до 1114111 или список [x,y,z] таких чисел. Список может быть только один и введён первым:\n')
l = []

try:
    if isinstance(eval(n), list):
        count = 0
        for x in eval(n):
            if int_plus(str(x)):
                count += 1
        if count == len(eval(n)):
            l = eval(n)
        else:
            print('Список должен содержать только целые, положительные числа')
            exit()
except SyntaxError:
    print('Ввод должен содержать только целые, положительные числа, а не знаки')
    exit()
except NameError:
    print('Ввод должен содержать только целые, положительные числа, а не буквы')
    exit()

while int_plus(n) and n:
    l.append(int(n))
    n = input('Введите целое число в диапазоне от 0 до 1114111:\n')
    if not int_plus(n):
        print('Это не число в диапазоне от 0 до 1114111. Будет выведен результат')

k = byte_to_str(l)
m = byte_to_list(l)
print('Вашим числам соответствуют следующие символы Юникода (строкой):\n',k,sep='')
print('Вашим числам соответствуют следующие символы Юникода (списком):\n',m,sep='')
