#!/usr/bin/python3

from equation import *

a = input('Введите коэффициент a:')
b = input('Введите коэффициент b:')
c = input('Введите коэффициент c:')

if a == 'j':
    a = '1j'
if b == 'j':
    b = '1j'
if c == 'j':
    c = '1j'

if check_coefficients(a, b, c):
    x1 = root_x_1(a, b, c)
    x2 = root_x_2(a, b, c)
    if x1 == x2:
        print('Один корень двойной кратности равен:', x1)
    else:
        print('Корни Вашего уравнения:')
        print('x1=',x1,sep='')
        print('x2=',x2,sep='')
else:
    print('Коэффициенты должны быть числами, коэффициент a не может быть равен 0')
