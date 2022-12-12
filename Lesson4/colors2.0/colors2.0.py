#!/usr/bin/python3

with open('dict_of_colors_name.txt', 'r') as dict_of_colors_name_file:
    dict_of_colors_name_str = dict_of_colors_name_file.read()
    
with open('dict_of_colors_hex.txt', 'r') as dict_of_colors_hex_file:
    dict_of_colors_hex_str = dict_of_colors_hex_file.read()
    
with open('dict_hex_to_name.txt', 'r') as dict_hex_to_name_file:
    dict_hex_to_name_str = dict_hex_to_name_file.read()
    
with open('dict_name_to_hex.txt', 'r') as dict_name_to_hex_file:
    dict_name_to_hex_str = dict_name_to_hex_file.read()
    

dict_of_colors_name = eval(dict_of_colors_name_str)
dict_of_colors_hex = eval(dict_of_colors_hex_str)
dict_name_to_hex = eval(dict_name_to_hex_str)
dict_hex_to_name = eval(dict_hex_to_name_str)

color = input('Введите оттенок:')
if color.lower() in dict_of_colors_name.keys():
    print(f'RGB для оттенка {color} ({dict_name_to_hex.get(color)}):', dict_of_colors_name.get(color.lower()))
elif color.lower() in dict_of_colors_hex.keys():
    print(f'RGB для оттенка {color} ({dict_hex_to_name.get(color.lower())}):', dict_of_colors_hex.get(color.lower()))
else:
    print('Такого оттенка нет')
