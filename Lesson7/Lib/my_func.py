#!/usr/bin/python3

def fibonacci(n):
    if n == 0:
        return n
    if n > 0:
        if n in (1, 2):
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

def check_password(password):
    if len(password) < 6 or password.isdigit() or password.upper() == 'PASSWORD':
        return False
    else:
        for sym in password:
            if not sym.isdigit():
                continue
            else:
                return True 
