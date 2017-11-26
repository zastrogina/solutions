#!/usr/bin/env python
# -*- coding: utf-8 -*-

#- Написать класс человек в котором можно хранить имя и фамилию человека,
# возраст, менять и получать их. Возраст должен быть между 0 и 120 годами

class Man:
    def __init__ (self, firstname, secondname, age):
        self.firstname = firstname
        self.secondname = secondname

        if 120 < age or age < 0:
            raise Exception ('Возраст должен быть между 0 и 120 годами')
        else:
            self.age = age

first = Man('Robert', 'Smith', 41)

print(first.age)

#- Написать класс у которого будет отдел и зарплата, которые так же задаются.
# Сделать поля удачных и неудачных поступков сотрудника которые можно через вызовы методов наращивать.
# Реализовать метод считающее итоговую зарплату = зп + 2*(удачные действия) - 3* (неудачные действия)
# - У менеджера зарплата считается как зп + 4*(удачные действия) - 5* (неудачные действия)

class Employee:
    def __init__(self, department, is_manager, salary, ok=0, not_ok=0):
        self.department = department
        self.is_manager = is_manager
        self.salary = salary
        self.ok = ok
        self.not_ok = not_ok

    def IncrOk(self):
        self.ok += 1

    def IncrNotOk(self):
        self.not_ok += 1

    def ItogSalary(self):
        if self.is_manager == False:
            bonus = self.salary + 2 * self.ok - 3 * self.not_ok
        else: 
            bonus = self.salary + 4 * self.ok - 5 * self.not_ok
        return bonus

second = Employee('Dep1', True, 100)

third = Employee('Dep1', False, 20)
second.IncrOk()
second.IncrOk()
second.IncrNotOk()

third.IncrNotOk()
third.IncrNotOk()
third.IncrNotOk()

print(second.ItogSalary())
print(third.ItogSalary())
