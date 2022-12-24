#!/usr/bin/python3

class Animals:
    '''
    Класс животные, описывантся следующими признаками:
    пол, возраст, количество конечностей, наличие волосяного покрова,
    наличие крыльев, хищностью
    '''

    def __init__(self, gender, age, limbs, wool, wings, predator):
        self.gender = gender
        self.age = age
        self.limbs = limbs
        self.wool = wool
        self.wings = wings
        self.predator = predator


class Mammals(Animals):
    '''Класс мплекопитающие имеет те же признаки что и животные,
    но добавляется наличие молока
    '''

    def __init__(self, gender, age, limbs, wool, wings, predator, milk):
        super().__init__(gender, age, limbs, wool, wings, predator)
        self.milk = milk


class Human(Mammals):
    '''Класс люди имеет все признаки млекопитающих
    плюс рост, вес, имя
    '''

    def __init__(self, gender, age, limbs, wool, wings, predator, milk,
                 height, weight, name):
        super().__init__(gender, age, limbs, wool, wings, predator, milk)
        self.height = height
        self.weight = weight
        self.name = name

    def say(self, text):
        print(text)

    def say_age(self):
        if self.gender == 'male':
            print(f'My age is {self.age}')

    def _private(self):
        print("It's a private method")


class Dog(Mammals):
    '''Класс собаки имеет все признаки млекопитающих
    плюс имя и порода
    '''

    def __init__(self, gender, age, limbs, wool, wings, predator, milk,
                 name, breed):
        super().__init__(gender, age, limbs, wool, wings, predator, milk)
        self.name = name
        self.breed = breed

    def info(self):
        print(f"I'm dog. My name is {self.name}")

    def make_sound(self):
        print('Bark')


class Cat(Mammals):
    '''Класс кошки имеет все признаки млекопитающих
    плюс имя, порода и наглость
    '''

    def __init__(self, gender, age, limbs, wool, wings, predator, milk, name,
                 breed, impudence):
        super().__init__(gender, age, limbs, wool, wings, predator, milk)
        self.name = name
        self.breed = breed
        self.impudence = impudence

    def info(self):
        print(f"I'm cat. My name is {self.name}")

    def make_sound(self):
        print('Meow')
