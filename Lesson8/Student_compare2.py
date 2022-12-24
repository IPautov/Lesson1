#!/usr/bin/python3
from Student import Student

print('Введите данные студентов')
print('Для студента 1')
Student_1 = Student(input('Пол\n'), input('Возраст\n'), 4,  'No', 'No', 'Yes', 'Yes', input('Рост\n'), input('Вес\n'), input('Имя\n'), input('Количество сданных ДЗ\n'))
print('Для студента 2')
Student_2 = Student(input('Пол\n'), input('Возраст\n'), 4,  'No', 'No', 'Yes', 'Yes', input('Рост\n'), input('Вес\n'), input('Имя\n'), input('Количество сданных ДЗ\n'))

if Student_1 == Student_2:
    print('У студентов одинаковое количество выполненых ДЗ')
if Student_1 <= Student_2:
    print(f'У студентов одинаковое количество выполненых ДЗ или {Student_1.name} сделал меньше чем {Student_2.name}')
if Student_1 < Student_2:
    print(f'{Student_1.name} сделал меньше ДЗ чем {Student_2.name}')
if Student_1 != Student_2:
    print(f'У студентов разное количество выполненныз ДЗ')
if Student_1 > Student_2:
    print(f'{Student_1.name} сделал больше ДЗ чем {Student_2.name}')
if Student_1 >= Student_2:
    print(f'У студентов одинаковое количество выполненых ДЗ или {Student_1.name} сделал больше чем {Student_2.name}')
