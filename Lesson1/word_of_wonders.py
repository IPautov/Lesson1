from itertools import *

word = input('Введите буквы:')
# получим объект файла
file1 = open("/home/student/Lesson1/sample.txt", "r")
words = []

while True:
    # считываем строку
    line = file1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    if 3 <= len(line) <= len(word) + 1:
        words.append(line.strip())
# закрываем файл
file1.close

s = ''
words_find = []
for j in range(3, len(word) +1):
    for i in permutations(word, j):
        s = ''.join(i) # abc acb bac bca cab cba
        if s in words:
            words_find.append(s)
        else:
            continue

words_find_final = [el for el, _ in groupby(words_find)]
print(*words_find_final, sep = '\n')
