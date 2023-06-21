#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""使用input得到用户的输入"""


def func1(x):
    try:
        x = int(x)
        print(x)
    except ValueError:
        print(x)


if __name__ == "__main__":
    x = input('x=')
    func1(x)