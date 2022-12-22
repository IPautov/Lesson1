#!/usr/bin/python3

spirt = []

n = input('Введите имя файла данных:\n')

try:
    with open(n, 'r') as f:
        for line in f:
            try:
                spirt.append(int(line))
                f.close
            except ValueError:
                print('Не соответствие формата данных. Не целые числа')
                f.close
                exit()
except FileNotFoundError:
    print('Такого файла нет')
    exit()

if spirt[0] < 0 or spirt[1] < 0 or spirt[2] < 0:
    print('Не соответствие формата данных. Отрциательные числа')
    exit()
else:
    w = open('spirt_out.txt', 'w')
    w.write(f'У Вас получится {min(spirt[0] // 2, spirt[1] // 6, spirt[2])} молекул спирта\n')
    w.close()
    print('Результат записан в файл spirt_out.txt')

