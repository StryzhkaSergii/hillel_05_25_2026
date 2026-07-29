
import unittest #імпорт з інтерпретатора
import requests #імпорт з venv

import unittest as ut

# from python_practice.lesson4 import string_example #імпорт з кореню проекту
import module_for_import #імпорт з пекеджа

import sys

print(sys.path)
#
sys.path.append(r"C:\Users\Helber\PycharmProjects\hillel_05_25_2026\python_practice\lesson4")
print(sys.path)

import string_example
print(string_example)

# from python_practice.lesson9.del_example import Car
import math
print(math.pi)

from math import pi

print(pi)

from math import *

print(tau)

# from ..lesson4 import split_example
# split_example.element