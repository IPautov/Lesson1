#!/usr/bin/python3

password = input('Введите Ваш пароль:')

def check_password(password):
    if len(password) < 6 or password.isdigit() or password.upper() == 'PASSWORD':
        return False
    else:
        for sym in password:
            if not sym.isdigit():
                continue
            else:
                return True
if check_password(password):
    print('Ваш пароль удовлетворяет условиям')
else:
    print('Ваш пароль не удовлетворяет условиям')
