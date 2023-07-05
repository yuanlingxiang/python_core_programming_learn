#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_6_6.py:创建一个string.strip的替代函数"""


def func(str):
    str1 = ''
    str2 = ''
    str3 = ''

    for char in str:
        if char.isspace() and len(str1) == 0:
            continue
        else:
            str1 += char

    for char in reversed(str1):
        if char.isspace() and len(str2) == 0:
            continue
        else:
            str2 += char

    for char in reversed(str2):
        str3 += char

    return str3


if __name__ == "__main__":
    str = input('str:')
    print(func(str))
