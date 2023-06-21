#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""循环和数字"""


def func1(num1=10, num2=0):
    """
    使用while循环输出0~10所有的整数
    :param num:
    :return:
    """

    while num1 >= 0:
        print(num2)
        num2 += 1
        num1 -= 1


def func2(num):
    """通过range输出0~10所有的整数"""
    for i in range(num+1):
        print(i)


if __name__ == "__main__":
    func1()
    func2(10)