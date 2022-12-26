#!/usr/bin/python

import password_check

def test_p_c_1111111():
    assert password_check.check_password('1111111') == False

def test_p_c_password():
    assert password_check.check_password('password') == False

def test_p_c_abcde1():
    assert password_check.check_password('abcde1') == True

def test_p_c_password2():
    assert password_check.check_password('PaSsWOrd2') == True

def test_p_c_qwerty():
    assert password_check.check_password('qwerty') == False

def test_p_c_symbols():
    assert password_check.check_password('!@#$%^&*') == False

