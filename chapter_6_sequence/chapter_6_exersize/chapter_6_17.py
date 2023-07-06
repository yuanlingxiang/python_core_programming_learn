#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_6_17.py：实现一个功能与pop相同的mypop函数"""


def func(arg):

    a = arg[-1]
    arg = arg[:-1]

    print('移除的元素:', a)
    print('现在的列表为:', arg)


if __name__ == "__main__":
    func(list('1234'))