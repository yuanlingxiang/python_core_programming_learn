#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_2_7.py:使用while和for循环逐个输出字符"""


def func1(str):
    """使用while输出"""
    str_length = len(str)
    i = 0

    while str_length > 0:
        print(str[i])
        i += 1
        str_length -= 1


def func2(str):
    """使用for循环输出"""
    str_length = len(str)

    for i in range(str_length):
        print(str[i])


if __name__ == '__main__':
    str = input('str is:')
    func1(str)
    func2(str)