#!/usr/bin/python3

def check_password(password):
    if len(password) < 6 or password.isdigit() or password.upper() == 'PASSWORD':
        return False
    else:
        for sym in password:
            if sym.isalpha():
                continue
            else:
                return True
    return False
