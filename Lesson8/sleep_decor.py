#!/usr/bin/python3

import time


def sleep(func):
    '''Декоратор для функции подсчёт значения заданного элемента
    последовательности Фибоначчи, запрещающий вызов функции чаще
    чем раз в 5 секунд'''

    count = [0]
    last = [time.time()]

    def wrapper(n):
        # Первый вызов функции
        if count[0] == 0:
            count[0] += 1
            return func(n)
        # Последующие вызовы
        else:
            if time.time() - last[0] < 5:
                print(f'Слишком частый вызов функции. Результат будет выведен через {5 - (time.time() - last[0])} секунд')
                # Таймер
                time.sleep(5 - (time.time() - last[0]))
        count[0] += 1
        last[0] = time.time()
        return func(n)
    return wrapper


@sleep
def print_fib(n):
    def fibonacci(n):
        if n in (1, 2):
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    print(
        f'Элемент последовательности Фибоначчи с порядковым номер {n} равен {fibonacci(n)}\n')


n = '0'
while n.isdigit():
    try:
        n = input('Введите порядковый номер элемента последовательности Фибоначчи:\n')
        print_fib(int(n))
    except RecursionError:
        print('Порядковый номер элемента последовательности Фибоначчи должен быть целым положительным числом')
        exit()
    except ValueError:
        print('Порядковый номер элемента последовательности Фибоначчи должен быть целым положительным числом')
        exit()
    except KeyboardInterrupt:
        print('Выполнение программы завершено')
        exit()
