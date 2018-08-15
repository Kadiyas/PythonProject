# !/usr/local/bin/python3
# -*- coding: utf-8 -*-
import math

# 函数
print('-------------------调用函数-------------------')

absName = abs
print(absName(-23.34))
print(244)

# 打印16进制的数据
print(hex(244))

print('-------------------定义函数-------------------')


def my_abs(args):
    if not isinstance(args, (float, int)):
        raise TypeError('bad operand type')
    if args > 0:
        return args
    else:
        return -args


help(isinstance)
help(TypeError)

print(my_abs(23))
print('-----------空函数---------')


def nop():
    print('this is a nop function')
    pass
    print('this is a nop function2')


nop()


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.cos(angle)
    return nx, ny


print(move(0, 0, 23, 40))


#
# 练习
#
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解。


def quadratic(a, b, c):
    if a == 0:
        raise Exception('a can not be 0')
    x1 = -b + math.sqrt(b * b - 4 * a * c) / (2 * a)
    x2 = -b - math.sqrt(b * b - 4 * a * c) / (2 * a)
    return x1, x2


x, y = quadratic(2, 3, 1)
print(x, y)
print('quadratic(2, 3, 1) 的第一个解为 %s ,第二个解为 %s' % (x, y))
print(quadratic(1, 3, -4))


def power(a, b=2):
    s = 1
    while b > 0:
        b = b - 1
        s = s * a
    return s


print(power(2))


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def anything(L=None):
    if L is None:
        L = []
    L.append("END")
    return L


print(anything())


# 可变参数 使用 *


def calculate(*numbers):
    sumValue = 0
    for number in numbers:
        sumValue = sumValue + number * number
    return sumValue


numbers = [1, 2, 4]
# 对于List，传参时可以使用*指向一个list
print(calculate(*numbers))


# 关键值参数


def person(name, age, **kwargs):
    if 'city' in kwargs:
        print('city is', kwargs.get('city'))

    if 'job' in kwargs:
        print('job is', kwargs.get('job'))
    print('name = ', name, ', age = ', age, ', other', kwargs)


extra = {'gender': 'man', 'address': 'cq'}
person('liu', 23, **extra)

person('liu', 23, city='cq', job='engineer', address='yb')


# 命名关键字参数(用于限定传入的关键字参数）


def person(name, age, *, city='chongQing', job='engineer'):
    print(name, age, city, job)


person('liu', 25, city='que')


#
# 参数组合
#
# * 代表可变参数 相当于 tuple，
# ** 代表关键字参数 相当于 dict，
# 使用 * , 隔开代表命名关键字参数 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
#
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：
# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 例如，
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


def f1(a, b, c=None, *args, name, **kwargs):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kwargs)


args1 = (1, 2, 3)
kwargs1 = {'q1': 'A', 'q2': 'B'}

f1(23, 'match', *args1, name='bobo', c1='math', c2='chinese')

# 练习
#
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
# def product(x, y):
#     return x * y
print('---------------------练习---------------------')


def product(*args):
    if len(args) == 0:
        raise Exception('args can not be empty')
    else:
        result = args[0]
        string = None
        for arg in args:
            if string is None:
                string = str(arg)
            else:
                string = string.__add__(' * %s' % arg)
                result = result * arg

    print(string, ' = ', result)


product(*args1)

print('-------------------递归函数--------------------')


def fact(n):
    print('n = ', n)
    if n == 1:
        return 1
    return n * fact(n - 1)


# 尾递归

def fact_iter(num, product):
    print('product = ', product)
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


def fact1(n):
    return fact_iter(n, 1)


print('fact(4)=', fact(4))
print('fact1(4)', fact1(4))

# 练习
#
# 汉诺塔的移动可以用递归函数非常简单地实现。
#
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法


number = 0


def move(n, start, buffer, target):
    global number
    if n == 1:
        number = number + 1
        print(start, '--->', target)
        # print('Move', n, 'from', start, 'target', target)
    else:
        # 将n-1 个盘子从起始区（A)搬到缓冲区(B)
        move(n - 1, start, target, buffer)
        # 将起始区（A）的最后一个盘子也就是第n个盘子搬到目标区（C)
        move(1, start, buffer, target)
        # 将n-1个盘子从缓冲区（B)搬到目标区（C)
        move(n - 1, buffer, start, target)


move(15, 'A', 'B', 'C')
print('总共搬运了', number, '次')
