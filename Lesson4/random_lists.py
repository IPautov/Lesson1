#!/usr/bin/python3

from random import *
print('Даны 2 списка чисел:')
list_1 = [randint(1, 100) for x in range(0, 10)]
list_2 = [randint(1, 100) for x in range(0, 10)]

print(list_1)
print(list_2)
list_of_duplicate = []
list_of_just_in_1 = []
list_of_just_in_2 = []
list_of_both = []

for a in list_1:
    if a in list_of_duplicate:
        continue
    for b in list_2:
        if a == b:
            list_of_duplicate.append(a)
            break

for a in list_1:
    if a in list_2:
        continue
    else:
        list_of_just_in_1.append(a)
        
for b in list_2:
    if b in list_1:
        continue
    else:
        list_of_just_in_2.append(b)
        
for a in list_1:
    if a not in list_2:
        list_of_both.append(a)

for b in list_2:
    if b not in list_1:
        list_of_both.append(b)


print('Повторяющиеся в обоих списках числа:                      ', list_of_duplicate)
print("Числа которые есть только в 1 списке:                     ", list_of_just_in_1)
print("Числа которые есть только во 2 списке:                    ", list_of_just_in_2)
print("Числа которые есть в обоих списках, но не повторяющиеся:  ", list_of_both)
