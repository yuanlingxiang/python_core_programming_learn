#! /usr/bin/evn python
# -*- coding:utf-8 -*-

"""chapter_5_11.py: 取余"""


def func1(num=20):
    """
    返回给定数的奇数，偶数列表
    :param num:
    :return:
    """
    odd_list = [i for i in range(num+1) if i % 2 == 1]
    even_list = [i for i in range(num+1) if i % 2 == 0]

    return odd_list, even_list


def func2(num1, num2):
    try:
        num1, num2 = list(map(float, [num1, num2]))
    except Exception as e:
        return e

    if num1 % num2 == 0 or num2 % num1 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    num1, num2 = input('num1, num2:').split(',')
    print('0~20的奇数列表，偶数列表为：', func1())
    print('num1, num2是整除关系为：', func2(num1, num2))