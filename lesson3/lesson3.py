#!/usr/bin/env python
# -*- coding: utf-8 -*-

#- Дан файл в каждой строке которого записано число.
# Написать функцию которая на вход принимает путь к файлу и выводит на консоль сумму чисел из файла

def read_all_file(path):

    with open(path, 'r') as f:
        nums = f.read().split("\n")
        sumn = sum([int(numb) for numb in nums if numb])
        return sumn

#print(read_all_file('/home/gene/solutions/lesson3/lesson3.txt'))

#- Написать функцию которая на вход принимает путь к файлу, и 2 целых числа m и n.
# В файл записать m случайно регенерированных текстовых строк длиной n
#'/home/gene/solutions/lesson3/for_input.txt'

from random import choice
from string import ascii_letters

def write_in_file(path, m, n):

    fill = ""
    i = 0
    while i < m:
        fill += ''.join(choice(ascii_letters) for i in range(n)) + '\n'
        i += 1
    with open(path, 'w') as f:
        f.write(fill)
    return True

#write_in_file('/home/gene/solutions/lesson3/randm.txt', 4, 3)

#- Написать функцию is_year_leap, принимающую 1 аргумент год,
# и возвращающую True, если год високосный, и False иначе.

def is_year_leap(y):

    if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
        return False
    else:
        return True

#print(is_year_leap(2001))

#Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
# площадь квадрата и диагональ квадрата.

import math

def square(b):

    perimetr =  str(int(b) * 4)
    sq = str(int(b) * 2)
    diag = str(math.sqrt(2) * int(b))
    return (perimetr, sq, diag)

#square(20)

#- Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.

def is_prime(x):

    if x == 0:
        return False
    elif x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x%i == 0:
                return False
            elif i == x-1:
                return True

#print(is_prime(113))

