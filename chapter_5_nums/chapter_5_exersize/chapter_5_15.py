#! /usr/bin/evn python
# -*- coding:utf-8 -*-

"""chapter_5_15.py: 最大公约数， 最小公倍数"""


def func1(num1, num2):
    """
    计算两个数的最大公约数
    :param num1:
    :param num2:
    :return:
    """
    try:
        num1, num2 = list(map(int, [num1, num2]))
    except Exception as e:
        return e

    smaller = num1 if num1 < num2 else num2

    result = 1
    for i in range(1, smaller+1):
        if num1 % i == 0 and num2 % i == 0:
            result = i

    return result


def func2(num1, num2):
    """
    计算两个数的最小公倍数
    :param num1:
    :param num2:
    :return:
    """
    try:
        num1, num2 = list(map(int, [num1, num2]))
    except Exception as e:
        return e

    greater = num1 if num1 > num2 else num2

    while True:
        if greater % num1 == 0 and greater % num2 == 0:
            return greater
        else:
            greater += 1


if __name__ == "__main__":
    num1, num2 = input('num1, num2:').split(',')
    print('两个数的最大公约数：', func1(num1, num2))
    print('两个数的最小公倍数：', func2(num1, num2))

