#!/usr/bin/python3
def summ(*arg):
    sum_str = 'Вы не передали ни одного аргумента'
    if not arg:
        return sum_str
    sum_list = []
    sum_tuple = ()
    sum_set = {}
    sum_dig = 0
    type0 = type(arg[0])
    count = 0
    count_dig = 0
    for x in arg:
        if type(x) == type(1) or type(x) == type(0.1) or type(x) == type(5j):
            count_dig += 1
    for x in arg:
        if type(x) == type0:
            count += 1
    if count == len(arg) and count != 0:
        if type0 == type([1,2,3]):
            for x in arg:
                sum_list += x
            sum_str = sum_list
        if type0 == type((1,2,3)):
            for x in arg:
                sum_tuple += x
            sum_str = sum_tuple
        if type0 == type('a'):
            sum_str = ''
            for x in arg:
                sum_str += x
        if type0 == type({1,2,3}):
            print('Если имелось ввиду множество, то их складывать нельзя')
            sum_str = ''
            for x in arg:
                sum_str += str(x)
        if type0 == type({'a':1,'b':2}):
            print('Если имелся ввиду словарь, то их складывать нельзя')
            sum_str = ''
            for x in arg:
                sum_str += str(x)
        if type0 == type(True):
            sum_bool = ''
            for x in arg:
                sum_bool += str(x)
            for x in arg:
                sum_dig += int(x)
            sum_str = f'Если вы имеелли ввиду строку результат будет {sum_bool}\nЕсли вы имели ввиду булев тип результат {sum_dig}'
    else:
        sum_str = ''
        for x in arg:
            x = str(x)
            sum_str += x
    if count_dig == len(arg):
        for x in arg:
            sum_dig += x
        if sum_dig.imag == 0:
            if sum_dig * 10 % 10 == 0:
                sum_str = int(sum_dig)
            else:
                sum_str = float(sum_dig)
        else:
            sum_str = sum_dig
    return sum_str

l = []
l_str = []
while True:
    n = input('Введите аргумент который необходимо передать в функцию сложения, пустой ввод покажет результат:\n')
    if n == '':
        break
    l_str.append(n)
    try:
        if complex(n).imag == 0:
            if str(float(n))[-1] == '0':
                l.append(int(n))
            else:
                l.append(float(n))
        else:
            l.append(complex(n))
    except:
        try:
            if isinstance(eval(n), list):
                l.append(eval(n))
            if isinstance(eval(n), tuple):
                l.append(tuple(eval(n)))
            if isinstance(eval(n), dict):
                l.append(dict(eval(n)))
            if isinstance(eval(n), bool):
                l.append(bool(eval(n)))
            if isinstance(eval(n), set):
                l.append(set(eval(n)))
        except:
            l.append(str(n))

if len(l) > 0:
    type1 = type(l[0])
    count_t = 0
    count_d = 0
    for y in l:
        if type(y) == type1:
            count_t += 1
        if type(y) == type(1) or type(y) == type(5j) or type(y) == type(0.1):
            count_d += 1
    if count_t == len(l) or count_d == len(l):
        k = summ(*l)
    else:
        k = summ(*l_str)
    print('Результат:\n',k)
else:
    print('Результат\n',summ(*l))
