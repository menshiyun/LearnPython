#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# n1 = 255
# n2 = 1000

# print(hex(n1))
# print(hex(n2))


import math


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


# print(my_abs(-123))


def nop():
    pass


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# print(my_abs(-123))


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# x, y = move(100, 100, 60, math.pi / 6)
# r = move(100, 100, 60, math.pi / 6)


def quadratic(a, b, c):
    if pow(b, 2) - 4 * a * c < 0:
        print('无解')
    else:
        vsqrt = math.sqrt(pow(b, 2) - 4 * a * c)
        x1 = (-b + vsqrt) / (2 * a)
        x2 = (-b - vsqrt) / (2 * a)
        return x1, x2


# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

# if quadratic(2, 3, 1) != (-0.5, -1.0):
#    print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#    print('测试失败')
# else:
#    print('测试成功')

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#r = power(2,1)


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

# print(calc(*range(0,101)))


# def person(name, age, **kw):
#    print('name:', name, 'age:', age, 'other:', kw)


#person('Michael', 30)
#person('Bob', 35, city='Beijing')
#person('Adam', 45, gender='M', job='Engineer')

#extra = {'city': 'Beijing', 'job': 'Engineer'}
#person('Jack', 24, city=extra['city'], job=extra['job'])

#extra = {'city': 'Beijing', 'job': 'Engineer'}
#person('Jack', 24, **extra)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


#f1(1, 2)
#f1(1, 2, c=3)
#f1(1, 2, 3, 'a', 'b')
#f1(1, 2, 3, 'a', 'b', x=99)
#f2(1, 2, d=99, ext=None)

#args = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}
#f1(*args, **kw)

#args = (1, 2, 3)
# kw = {'d': 88, 'x': '#'}
#f2(*args, **kw)


def product(x, *y):
    sum = x
    for n in y:
        sum *= n
    return sum


#print('product(5) =', product(5))
#print('product(5, 6) =', product(5, 6))
#print('product(5, 6, 7) =', product(5, 6, 7))
#print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#    print('测试失败!')
# elif product(5, 6) != 30:
#    print('测试失败!')
# elif product(5, 6, 7) != 210:
#    print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#    print('测试失败!')
# else:
#    try:
#        product()
#        print('测试失败!')
#    except TypeError:
#        print('测试成功!')

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))

print()
