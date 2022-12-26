#!/usr/bin/python3

def check_coefficients(a, b, c):
    if a == 'j':
        a = '1j'
    if b == 'j':
        b = '1j'
    if c == 'j':
        c = '1j'
    try:
        if ((type(eval(a)) == int or type(eval(a)) == float or type(eval(a)) == complex) and (eval(a) != 0) and
        (type(eval(b)) == int or type(eval(b)) == float or type(eval(b)) == complex) and
        (type(eval(c)) == int or type(eval(c)) == float or type(eval(c)) == complex)):
            return True
        else:
            return False
    except:
        return False

def discriminant(a, b, c):
    return eval(b) ** 2 - 4 * eval(a) * eval(c)

def root_x_1(a, b, c):
    return (-(eval(b)) - (discriminant(a,b,c)) ** 0.5) / (2 * eval(a))

def root_x_2(a, b, c):
    return (-(eval(b)) + (discriminant(a,b,c)) ** 0.5) / (2 * eval(a))
