#!/usr/bin/python3

print("Ваш персонаж наоходится в точке с координатами (0:0).")
print(" Введите куда Ваш персонаж должен идти")

x = 0
y = 0
break_word = 'ДА'
while break_word == 'ДА':
	x_r = int(input('Вправо на:'))
	x_l = int(input('Влево на:'))
	y_u = int(input('Вверх на:'))
	y_d = int(input('Вниз на:'))
	x += x_r - x_l
	y += y_u - y_d
	print("Новые координаты персонажа:", x,':',y,sep='')
	break_word = input('Продолжаем? (Да/Нет):').upper()
	while break_word != 'ДА' and break_word != 'НЕТ':
		break_word = input('Продолжаем? (Да/Нет):').upper()

