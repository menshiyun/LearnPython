#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print('HelloWorld!')

# print(1024 * 768)

# name = 'World'  # input()
# print('Hello,', name)

# print(__file__, __name__)

# print absolute value of an integer:
#a = 100
# if a >= 0:
#    print(a)
# else:
#    print(-a)

#a = 'ABC'
#b = a
#a = 'XYZ'
# print(b)

#n = 123
#f = 456.789
#s1 = 'Hello, world'
#s2 = 'Hello, \'Adam\''
#s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''

# print(n)
# print(f)
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# print('包含中文的str')
# print(ord('A'))
# print(ord('中'))
# print(chr(66))
# print(chr(25991))
# print('\u4e2d\u6587')

# list
#classmates = ['Michael', 'Bob', 'Tracy']
# classmates.append('Adam')
#classmates.insert(1, 'Jack')
# classmates.pop()
# classmates.pop(1)
#classmates[1] = 'Sarah'
#L = ['Apple', 123, True]
#s = ['python', 'java', ['asp', 'php'], 'scheme']
#p = ['asp', 'php']
#q = ['python', 'java', p, 'scheme']

# tuple
# classmates = ('Michael', 'Bob', 'Tracy')
# t = (1, 2)
# t = ()
# t = (1)
# t = (1,)
# t = ('a', 'b', ['A', 'B'])

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]

# print(L[0][0])
# print(L[1][1])
# print(L[2][2])

#age = 20
# if age >= 18:
#    print('your age is', age)
#    print('adult')

#age = 3
# if age >= 18:
#    print('your age is', age)
#    print('adult')
# else:
#    print('your age is', age)
#    print('teenager')

#age = 3
# if age >= 18:
#    print('adult')
# elif age >= 6:
#    print('teenager')
# else:
#    print('kid')

#age = 20
# if age >= 6:
#    print('teenager')
# elif age >= 18:
#    print('adult')
# else:
#    print('kid')

# birth = input('birth: ')
# birth = int(birth)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

#height = float(input('height :'))
#weight = float(input('weight :'))

#bmi = weight / (height * height)

# if bmi < 18.5:
#    print("BMI为%.2f" % bmi + '，过轻')
# elif bmi < 25:
#    print("BMI为%.2f" % bmi + '，正常')
# elif bmi <28:
#    print("BMI为%.2f" % bmi + '，过重')
# elif bmi < 32:
#    print("BMI为%.2f" % bmi + '，肥胖')
# else :
#    print("BMI为%.2f" % bmi + '，严重肥胖')

#names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#    print(name)

#sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#    sum = sum + x
# print(sum)

#sum = 0
# for x in range(101):
#    sum = sum + x
# print(sum)

#sum = 0
#n = 1
# while n < 100:
#    sum += n
#    n += 2
# print(sum)

#n = 1
#while n <= 100:
#    if n > 10:  # 当n = 11时，条件满足，执行break语句
#        break  # break语句会结束当前循环
#    print(n)
#    n = n + 1
#print('END')

#n = 0
#while n < 10:
#    n = n + 1
#    if n % 2 == 0: # 如果n是偶数，执行continue语句
#        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#    print(n)

#d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
#d.pop('Bob')

#s = set([1, 2, 3])
#s = set([1, 1, 2, 2, 3, 3])
#s.add(4)
#s.remove(4)

#s1 = set([1, 2, 3])
#s2 = set([2, 3, 4])
#sa = s1 & s2
#sb = s1 | s2

a = 'abc'
a = a.replace('a', 'A')

print()
