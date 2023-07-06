#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_6_16.py：矩阵的加法和剩法"""


import numpy as np


def func1():
    """
    矩阵的加法
    :return:
    """
    a = np.mat([[1, 2, 3], [1, 2, 3]])

    return a + a


def func2():
    """
    矩阵的剩法
    :return:
    """
    a = np.mat([[1, 2, 3], [1, 2, 3]])
    b = a.T

    return a * b


if __name__ == "__main__":
    print('矩阵的加法结果：', func1())
    print('矩阵的剩法结果：', func2())