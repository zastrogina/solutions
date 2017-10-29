#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = {'0':'jan','1':'feb','2':'mar','3':'apr','4':'may','5':'jun','6':'jul','7':'aug','8':'sep','9':'oct','10':'nov','11':'dec'}

# разворачиваем словарь
b = dict([(y,x) for (x,y) in a.items()])

# объединяем a и b в один словарь
a.update(b)

d = input()

print(a[d])