#! /usr/bin/evn python
# -*- coding:utf-8 -*-

"""chapter_5_10.py: 温度转换"""


def func(F):
    try:
        F = float(F)
    except Exception as e:
        return e

    return (F-32) * (5 / 9)


if __name__ == "__main__":
    F = input('F:')
    print('转换后的温度为：', func(F))