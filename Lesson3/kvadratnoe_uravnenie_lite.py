#!/usr/bin/python3

import cmath
import math

try:
    a = float(input('Введите коэффициент а:'))
except ValueError:
    a = 'e'
    while a == 'e':
        print('Введённое не является числом. Попробуйте ещё раз.')
        a = input('Введите коэффициент a:')
        try:
            a = float(a)
        except ValueError:
            a = 'e'

while a == 0:
    print('Коэффициент a не может быть равен нулю.')
    a = input('Введите коэффициент a:')
    try:
        a = float(a)
    except ValueError:
        a = 'e'
        while a == 'e':
            print('Введённое не является числом. Попробуйте ещё раз.')
            a = input('Введите коэффициент a:')
            try:
                a = float(a)
            except ValueError:
                a = 'e'
try:
    b = float(input('Введите коэффициент b:'))
except ValueError:
    b = 'e'
    while b == 'e':
        print('Введённое не является числом. Попробуйте ещё раз.')
        b = input('Введите коэффициент b:')
        try:
            b = float(b)
        except ValueError:
            b = 'e'

try:
    c = float(input('Введите коэффициент c:'))
except ValueError:
    c = 'e'
    while c == 'e':
        print('Введённое не является числом. Попробуйте ещё раз.')
        c = input('Введите коэффициент c:')
        try:
            c = float(c)
        except ValueError:
            c = 'e'

D = b**2 - 4*a*c

if D < 0:
    x1 = (-b + cmath.sqrt(D)) / (2*a)
    x2 = (-b - cmath.sqrt(D)) / (2*a)
    if x1.imag == 0:
        x1 = x1.real
    if x2.imag == 0:
        x2 = x2.real
    print('Корни Вашего уравнения:')
    print('x1=', x1, sep='')
    print('x2=', x2, sep='')
elif D == 0:
    x = -b / (2*a)
    print(f'Один корень двойной кратности:{x}')
elif D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print('Корни Вашего уравнения:')
    print('x1=', x1, sep='')
    print('x2=', x2, sep='')

