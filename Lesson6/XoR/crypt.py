#!/usr/bin/python3

try:
    data_file = input('Введите название файла с данными:')
    with open(data_file, 'r',encoding='utf-8') as file:
        data = file.read()
        file.close()
except:
    print('Такого файла нет')
    exit()
key = input('Введите ключ:')
text = ''
crypt = ''

for i in range(len(data)):
    d = data[i]
    k = key[i%len(key)]
    crypt += chr(ord(d) ^ ord(k))
crypt_file = open('crypted.txt', 'w',encoding='utf-8')
crypt_file.write(crypt)
crypt_file.close()
