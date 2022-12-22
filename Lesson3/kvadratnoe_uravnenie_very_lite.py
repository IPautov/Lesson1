#!/usr/bin/python3

import math

print('Введите коэффициенты a, b, c Вашего квадратного уравнения:')
print('ax\u00B2 + bx + c = 0')

try:
    a = int(input('Введите коэффициент а:'))
except ValueError:
    a = 'e'
    while a == 'e':
        print('Введённое не является целым числом. Попробуйте ещё раз.')
        a = input('Введите коэффициент a:')
        try:
            a = int(a)
        except ValueError:
            a = 'e'

while a == 0:
    print('Коэффициент a не может быть равен нулю.')
    a = input(' Введите коэффициент a:')
    try:
        a = int(a)
    except ValueError:
        a = 'e'
        while a == 'e':
            print('Введённое не является целым числом. Попробуйте ещё раз.')
            a = input('Введите коэффициент a:')
            try:
                a = int(a)
            except ValueError:
                a = 'e'
try:
    b = int(input('Введите коэффициент b:'))
except ValueError:
    b = 'e'
    while b == 'e':
        print('Введённое не является целым числом. Попробуйте ещё раз.')
        b = input('Введите коэффициент b:')
        try:
            b = int(b)
        except ValueError:
            b = 'e'

try:
    c = int(input('Введите коэффициент c:'))
except ValueError:
    c = 'e'
    while c == 'e':
        print('Введённое не является целым числом. Попробуйте ещё раз.')
        c = input('Введите коэффициент c:')
        try:
            c = int(c)
        except ValueError:
            c = 'e'

D = b**2 - 4*a*c

if D < 0:
    print('Корней нет.')
elif D == 0:
    x = -b / (2*a)
    print(f'Один корень двойной кратности:{x}')
elif D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print('Корни Вашего уравнения:')
    print('x1=', x1, sep='')
    print('x2=', x2, sep='')

