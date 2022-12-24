#!/usr/bin/python3

from Animals import Human


class Student(Human):
    '''Класс студенты имеет все признаки людей
    плюс количество сданных ДЗ
    '''

    def __init__(self, gender, age, limbs, wool, wings, predator, milk,
                 height, weight, name, dz):
        super().__init__(gender, age, limbs, wool, wings, predator, milk,
                         height, weight, name)
        self.dz = dz
    '''Перегружаем операторы сравнения для класса
    студенты для сравнения по количеству сданных ДЗ
    '''

    def __lt__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz < other_dz

    def __le__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz <= other_dz

    def __eq__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz == other_dz

    def __ne__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz != other_dz

    def __gt__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz > other_dz

    def __ge__(self, other):
        self_dz = self.dz
        other_dz = other.dz
        return self_dz >= other_dz
