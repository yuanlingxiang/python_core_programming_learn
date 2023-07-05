#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_6_10.py：大小写转换"""


def func(str):
    return str.swapcase()


if __name__ == "__main__":
    str = input('str:')
    print(func(str))