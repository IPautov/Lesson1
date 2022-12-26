#!/usr/bin/python3

from equation import *

def test_check_coefficients_4_5_6():
    assert check_coefficients('4', '5', '6') == True

def test_discriminant_4_5_6():
    assert discriminant('4', '5', '6') == -71

def test_root_x_1_minus_4_5_6():
    assert root_x_1('-4', '5', '6') == 2.0

def test_root_x_2_minus_4_5_6():
    assert root_x_2('-4', '5', '6') == -0.75

def test_check_coefficients():
    assert check_coefficients('sdg', '5', '6') == False

def test_check_coefficients_0_5_6():
    assert check_coefficients('0', '5', '6') == False

def test_check_coefficients_j_j_j():
    assert check_coefficients('j', 'j', 'j') == True
