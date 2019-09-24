#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique
from types import MethodType


class Student(object):
    __slots__ = ('name', 'age', 'set_age')  # 用tuple定义允许绑定的属性名称
    pass


#s = Student()
# s.name = 'Michael'  # 动态给实例绑定一个属性
# print(s.name)


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


# s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
# s.set_age(25)  # 调用实例方法
# print(s.age)  # 测试结果


class GraduateStudent(Student):
    pass


#g = GraduateStudent()
#g.score = 9999
# print(g.score)

class Screen(object):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def resolution(self):
        return self.__width * self.__height
    pass

# 测试:
#s = Screen()
#s.width = 1024
#s.height = 768
#print('resolution =', s.resolution)
# if s.resolution == 786432:
#    print('测试通过!')
# else:
#    print('测试失败!')


class Animal(object):
    pass

# 大类:


class Mammal(Animal):
    pass


class Bird(Animal):
    pass

# 各种动物:


class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class RunnableMixIn(object):
    def run(self):
        print('Running...')


class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


class Dog(Mammal, RunnableMixIn):
    pass


class Bat(Mammal, FlyableMixIn):
    pass


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

pass
