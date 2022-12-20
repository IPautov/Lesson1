#!/usr/bin/python3

try:
    crypto_data = input('Введите название файла с шифрованными данными:')
    with open(crypto_data, 'r',encoding='utf-8') as file:
        data = file.read()
        file.close()
except:
    print('Такого файла нет')
    exit()
key = input('Введите ключ:')
text = ''
encrypt = ''

for i in range(len(data)):
    d = data[i]
    k = key[i%len(key)]
    encrypt += chr(ord(d) ^ ord(k))
encrypt_file = open('encrypted.txt', 'w',encoding='utf-8')
encrypt_file.write(encrypt)
encrypt_file.close()
