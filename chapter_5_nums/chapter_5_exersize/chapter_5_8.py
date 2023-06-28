#! /usr/bin/evn python
# -*- coding:utf-8 -*-

"""chapter_5_8.py: 几何， 计算面积和体积"""

import math


def func1(length, width, high):
    """
    计算正方向面积、立方体体积
    :param length:
    :param width:
    :param high:
    :return:
    """
    try:
        length, width, high = list(map(float, [length, width, high]))
        area = length * width
        volume = length * width * high
    except Exception as e:
        return e

    return area, volume


def func2(r):
    """
    计算圆面积、球体积
    :param r:
    :return:
    """
    try:
        r = float(r)
        area = math.pi * pow(r, 2)
        volume = (4 / 3) * math.pi * pow(r, 3)
    except Exception as e:
        return e

    return area, volume


if __name__ == "__main__":
    length, width, high = input('input length, width, high:').split(',')
    r = input('r:')
    print('正方形的面积和立方体的体积为：', func1(length, width, high))
    print('圆面积和球体积为：', func2(r))



