#! /usr/bin/evn python
# -*- coding:utf-8 -*-

"""chapter_5_6.py: 计算机程序"""

import operator


operator_dict = {'+': operator.add, '-': operator.sub,
                 '*': operator.mul, '/': operator.truediv,
                 '%': operator.mod, '**': operator.pow}


def func(experss):
    """
    计算表达式的结果
    :param experss:传入的表达式
    :return:
    """
    for i in ['+', '-', '*', '/', '%', '**']:
        if i in express:
            if '**' in experss:
                split_char = '**'
            else:
                split_char = i

            try:
                nums_list = list(map(float, express.split(split_char)))
                return operator_dict.get(split_char)(nums_list[0], nums_list[1])
            except Exception as e:
                return e


if __name__ == '__main__':
    express = input('express=')
    print(func(express))