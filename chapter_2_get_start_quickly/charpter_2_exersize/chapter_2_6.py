#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_2_6.py:判断数字是正数，负数，等于0的情况"""


def func(num):
    try:
        num = float(num)
        if num == 0:
            print('input num equal 0')
        elif num > 0:
            print('input num greater 0')
        else:
            print('input num less 0')
    except ValueError:
        print('input num is not digits')


if __name__ == '__main__':
    num = input('num=')
    func(num)
