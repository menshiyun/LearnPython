#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import functools
from functools import reduce


def add(x, y, f):
    return f(x) + f(y)


#print(add(-5, 6, abs))


def f(x):
    return x * x


#r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#r = list(r)
#r = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


def normalize(name):
    return name.capitalize()


# 测试:
#L1 = ['adam', 'LISA', 'barT']
#L2 = list(map(normalize, L1))
# print(L2)


def prod(L):
    # def fn(x, y):
    #    return x * y
    return reduce(lambda x, y: x * y, L)


#print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#    print('测试成功!')
# else:
#    print('测试失败!')

def str2float(s):
    pass

#print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#    print('测试成功!')
# else:
#    print('测试失败!')


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印1000以内的素数:
# for n in primes():
#    if n < 100:
#        print(n)
#    else:
#        break


def is_palindrome(n):
    return str(n) == str(n)[::-1]


# 测试:
#output = filter(is_palindrome, range(1, 1000))
#print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#    print('测试成功!')
# else:
#    print('测试失败!')

#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
#L2 = sorted(L, key=by_name)
# print(L2)


def by_score(t):
    return -t[1]
#L2 = sorted(L, key=by_score)
# print(L2)


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

#f = lazy_sum(1, 3, 5, 7, 9)
# print(f())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

#f1, f2, f3 = count()
#f1 = f1()
#f2 = f2()
#f3 = f3()


def createCounter():
    s = [0]

    def counter():
        s[0] = s[0] + 1
        return s[0]
    return counter

# 测试:
#counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
#counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#    print('测试通过!')
# else:
#    print('测试失败!')

int2 = functools.partial(int, base=2)

print(sys.path)

print()
