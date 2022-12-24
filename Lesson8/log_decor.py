#!/usr/bin/python3

import logging
 
def logs(func):
    def wrapper(*params):
        logging.basicConfig(filename="my_log.log", 
                            level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")
        logging.debug(f'Переданные параметры {params}')
        logging.info(f'Результат {sum(params)}')
        return func(*params)
    return wrapper

@logs
def summ(*params):
    sum_chisel = 0
    for n in params:
        sum_chisel += n
    if sum_chisel.imag == 0:
        print('Сумма введёных Вами чисел:', sum_chisel.real)
    else:
        print('Сумма введёных Вами чисел:', sum_chisel)
a = ' '
x = []
while a:
    try:
        a = complex(input('Введите число:\n'))
        x.append(a)
    except ValueError:
        print("Введённое не является числом\nПродолжаем? (Да/Нет)")
        if input() == 'Да':
            continue
        else:
            a = ''
summ(*x)
