#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


#bart = Student('Bart Simpson', 59)
#lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()
#print(bart.name, bart.get_grade())
#print(lisa.name, lisa.get_grade())

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender in ("male", "female"):
            self.__gender = gender
        else:
            raise ValueError('Invalid gender')

# 测试:
#bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#    print('测试失败!')
# else:
#    bart.set_gender('female')
#    if bart.get_gender() != 'female':
#        print('测试失败!')
#    else:
#        print('测试成功!')


class Animal(object):
    def run(self):
        print('Animal is running...')

    def __len__(self):
        return 100


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


def run_twice(animal):
    animal.run()
    print('Length is', len(animal))

#dog = Dog()
# dog.run()

#cat = Cat()
# cat.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())


class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

pass
