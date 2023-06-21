#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""数字和操作符"""

import operator


def func(num1, num2):
    """
    数字运算符使用
    :param num1:
    :param num2:
    :return: 计算结果
    """
    add_result = num1 + num2
    sub_result = num1 - num2
    mul_result = num1 * num2
    div_result = num1 / num2
    divmod_result = num1 % num2
    pow_result = num1 ** num2

    return add_result, sub_result, mul_result, div_result, divmod_result, pow_result


if __name__ == "__main__":
    num1 = float(input('num1 = '))
    num2 = float(input('num2 = '))
    print(func(num1, num2))