# !/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os

# 高级特性
print('--------------切片(Slice)---------------')
# list tuple 字符串 都可以切片
L = ['L0', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', 'L11']
print("L == ", L)
print('L 取0~2 = ', L[0:3])
print('L 取倒数第二个~最后一个 = ', L[-2:])
print('L 前10个数，每两个取一个： = ', L[0:10:2])
print('L 所有数，每5个取一个：： = ', L[::5])

# 什么都不写，只写[:]就可以原样复制一个list：L[:]
L1 = L[:]
print('L1 = ', L1)

# tuple也是一种list，所以也可以切片
print('tuple也可以切片', (0, 1, 2, 3, 4, 5, 6, 7)[:3])


# 练习
#
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(string):
    if string == '':
        return ''
    while string[:1] == ' ':
        string = string[1:]
    while string[-1:] == ' ':
        string = string[:-1]
    return string


s = "  hello , weo  "
print(trim(s))
print(s.strip())
print('after trim --%s--' % trim(s))
print(s, 'after trim --' + trim(s) + '--')

print('--------------迭代(Iteration)---------------')
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
dic = {'L0': 0, 'L1': 1, "L2": 2}
for k, v in dic.items():
    print('key=', k, ', value=', v)
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
# from collections import Iterable
# isinstance('abc', Iterable)

# Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print("下标", i, "值", value)
# 练习
#
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
list1 = {1, 23, 2, 23, 55, 2, 5, 15}


def find_max_and_min(*args):
    if len(args) == 0:
        return None, None
    max1 = args[0]
    min1 = args[0]
    for value1 in args:
        if max1 < value1:
            max1 = value1
        if min1 > value1:
            min1 = value1
    return max1, min1


print('max value = %d,and min value = %d' % find_max_and_min(*list1))
print('--------------------列表生成式---------------------')
# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
list2 = list(range(1, 11))
print(list2)
print([x * x for x in list2])
print([m + n for m in 'ABC' for n in 'XYZ'])
print([d for d in os.listdir('.')])
L = ['Hello', 'World', 18, 'Apple', None]
L2 = []
[L2.append(s.lower()) for s in L if isinstance(s, str)]
print([s for s in L if isinstance(s, str)])
print(L2)

print('--------------------生成器-----------------------')
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
g = (s for s in L if isinstance(s, str))
for n in g:
    print(n)


# 著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fibonacci(max):
    n, a, b = (0, 0, 1)
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1

    print('done')


fibonacci(5)


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def fib(max):
    n, a, b = (0, 0, 1)
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

    print('done')


f = fib(20)


def triangles(lines):
    n = 0
    ret = [1]
    while n <= lines:
        yield ret
        for j in range(1, len(ret)):
            ret[j] = pre[j] + pre[j - 1]
        ret.append(1)
        pre = ret[:]
        n = n + 1


#
# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L.append(0)
#         L = [L[i - 1] + L[i] for i in range(len(L))]

def triangle(lines):
    pre = []
    current = [1]
    while lines > 1:
        yield current
        for m in range(1, len(current)):
            current[m] = pre[m] + pre[m - 1]
        current.append(1)
        pre = current[:]


tran = triangle(4)
print(next(tran))
print(next(tran))
print(next(tran))
print(next(tran))
