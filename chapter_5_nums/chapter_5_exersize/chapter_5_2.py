#! /usr/bin/evn python
# -*- coding:utf-8 -*-

"""chapter_5_2.py:计算两个数的乘积"""


def func(num1, num2):
    """
    返回两个数的乘积
    :param num1:
    :param num2:
    :return:
    """
    return num1 * num2


if __name__ == "__main__":
    nums = list(map(float, input('input nums:').split(',')))
    num1, num2 = nums[0], nums[1]
    print(func(num1, num2))