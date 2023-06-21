#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_2_9.py:使用while和for循环, 计算列表中元素的和的平均数"""


def func1(num_list):
    """
    使用while实现
    :param num_list:
    :return:
    """
    num_list_length = len(num_list)
    num_list_index = 0
    result = 0

    while num_list_index < num_list_length:
        result += float(num_list[num_list_index])
        num_list_index += 1

    return float(result / num_list_length)


def func2(num_list):
    """
    使用for实现
    :param num_list:
    :return:
    """
    num_list_length = len(num_list)
    result = 0

    for i in range(num_list_length):
        result += float(num_list[i])

    return float(result / num_list_length)


if __name__ == '__main__':
    num_list = input('num_list =').split(',')
    print(func1(num_list))
    print(func2(num_list))