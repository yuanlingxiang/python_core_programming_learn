#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_6_3.py:排序"""


def func1(seq):
    """输入一串数字，从小到大排列"""
    nums_list = list(map(int, seq))
    nums_list.sort()
    nums_list.reverse()

    return nums_list


def func2(seq):
    """通过字典序排序：从大到小进行排序"""
    nums_list = list(seq)
    nums_list.sort()
    nums_list.reverse()

    return nums_list


if __name__ == "__main__":
    seq = ['1', '2', '3', '4', '11', '12', '13', '14', '21', '22', '23', '24']
    print(func1(seq))
    print(func2(seq))