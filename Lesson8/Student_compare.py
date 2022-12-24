#!/usr/bin/python3

from Student import Student

Student_1 = Student('Male', 30, 4, 'No', 'No', 'Yes', 'Yes', 189, 88, 'Ilya', 10)
Student_2 = Student('Feale', 31, 4, 'No', 'No', 'Yes', 'Yes', 170, 55, 'Olga', 12)

print(Student_1 == Student_2)
print(Student_1 <= Student_2)
print(Student_1 < Student_2)
print(Student_1 != Student_2)
print(Student_1 > Student_2)
print(Student_1 >= Student_2)
