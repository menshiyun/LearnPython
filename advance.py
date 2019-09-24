#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#r = []
#n = 3
# for i in range(n):
#    r.append(L[i])

#r = L[0:3]
#r = L[:3]
#r = L[1:3]
#r = L[-2:]
#r = L[-2:-1]

#L = list(range(100))
#r = L[:10]
#r = L[-10:]
#r = L[10:20]
#r = L[:10:2]
#r = L[::5]
#r = L[:]
#t = (0, 1, 2, 3, 4, 5)[:3]

#d = {'a': 1, 'b': 2, 'c': 3}
# for key, v in d.items():
#    print(key, v)

# for i, value in enumerate(['A', 'B', 'C']):
#    print(i, value)

# for x, y in [(1, 1), (2, 4), (3, 9)]:
#    print(x, y)


def findMinAndMax(L):
    min = None
    max = None
    for x in L:
        if min == None:
            min = x
        elif x < min:
            min = x
        if max == None:
            max = x
        elif x > max:
            max = x
    return (min, max)


# if findMinAndMax([]) != (None, None):
#    print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#    print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#    print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#    print('测试失败!')
# else:
#    print('测试成功!')

#L = [x * x for x in range(1, 11)]
#L = [x * x for x in range(1, 11) if x % 2 == 0]
#L = [m + n for m in 'ABC' for n in 'XYZ']

#import os
#L = [d for d in os.listdir('.')]

#L1 = ['Hello', 'World', 18, 'Apple', None]
#L2 = [S.lower() for S in L1 if isinstance(S, str) == True]

# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#    print('测试通过!')
# else:
#    print('测试失败!')

#g = (x * x for x in range(10))
# for n in g:
#    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# for n in fib(6):
#    print(n)

#g = fib(6)
#while True:
#    try:
#        x = next(g)
#        print('g:', x)
#    except StopIteration as e:
#        print('Generator return value:', e.value)
#        break

def triangles():
    L = [1]
    while 1:
        yield L
        L = [0] + L + [0]
        L = [L[i] + L[i + 1] for i in range(len(L) - 1)]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
#n = 0
#results = []
#for t in triangles():
#    results.append(t)
#    n = n + 1
#    if n == 10:
#        break

#for t in results:
#    print(t)

#if results == [
#    [1],
#    [1, 1],
#    [1, 2, 1],
#    [1, 3, 3, 1],
#    [1, 4, 6, 4, 1],
#    [1, 5, 10, 10, 5, 1],
#    [1, 6, 15, 20, 15, 6, 1],
#    [1, 7, 21, 35, 35, 21, 7, 1],
#    [1, 8, 28, 56, 70, 56, 28, 8, 1],
#    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
#]:
#    print('测试通过!')
#else:
#    print('测试失败!')

print()
