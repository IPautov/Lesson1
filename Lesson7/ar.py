#!/usr/bin/python3

import numpy as np

array = np.random.randint(1, 100, (3, 3))
array_transpose = np.transpose(array)
print("Массив со случайнами числами: ", array, sep="\n")
print("Транспонированный массив: ", array_transpose, sep="\n")
