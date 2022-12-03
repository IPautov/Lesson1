#!/usr/bin/python3

import cmath
import math

print('Введите коэффициенты a, b, c Вашего квадратного уравнения ax\u00B2 + bx + c = 0')

try:
    a = complex(input('Введите коэффициент а:'))
except ValueError:
    a = 'e'
    while a == 'e':
        a = input('Введённое не является числом. Попробуйте ещё раз. \nВведите коэффициент a:')
        try:
            a = complex(a)
        except ValueError:
            a = 'e'
if a.imag == 0:
    a = a.real
while a == 0:
    a = input('Коэффициент a не может быть равен нулю. Введите коэффициент a:')
    try:
        a = complex(a)
    except ValueError:
        a = 'e'
        while a == 'e':
            a = input('Введённое не является числом. Попробуйте ещё раз. \nВведите коэффициент a:')
            try:
                a = complex(a)
            except ValueError:
                a = 'e'
try:
    b = complex(input('Введите коэффициент b:'))
except ValueError:
    b = 'e'
    while b == 'e':
        b = input('Введённое не является числом. Попробуйте ещё раз. \nВведите коэффициент b:')
        try:
            b = complex(b)
        except ValueError:
            b = 'e'
if b.imag == 0:
    b = b.real
    
try:
    c = complex(input('Введите коэффициент c:'))
except ValueError:
    c = 'e'
    while c == 'e':
        c = input('Введённое не является числом. Попробуйте ещё раз. \nВведите коэффициент c:')
        try:
            c = complex(c)
        except ValueError:
            c = 'e'
if c.imag == 0:
    c = c.real

D = b**2 - 4*a*c

if 'j' in str(D):
    x1 = (-b + cmath.sqrt(D))/(2*a)
    x2 = (-b - cmath.sqrt(D))/(2*a)
    if x1.imag == 0:
        x1 = x1.real
    if x2.imag == 0:
        x2 = x2.real
    print('Корни Вашего уравнения:')
    print('x1=',x1,sep='')
    print('x2=',x2,sep='')
elif D < 0:
    x1 = (-b + cmath.sqrt(D))/(2*a)
    x2 = (-b - cmath.sqrt(D))/(2*a)
    if x1.imag == 0:
        x1 = x1.real
    if x2.imag == 0:
        x2 = x2.real
    print('Корни Вашего уравнения:')
    print('x1=',x1,sep='')
    print('x2=',x2,sep='')
elif D == 0:
    x = -b/(2*a)
    print(f'Один корень двойной кратности:{x}')
elif D > 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print('Корни Вашего уравнения:')
    print('x1=',x1,sep='')
    print('x2=',x2,sep='')
