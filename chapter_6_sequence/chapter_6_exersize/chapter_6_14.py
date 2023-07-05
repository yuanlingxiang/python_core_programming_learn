#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_6_14.py：剪刀石头布游戏"""

import random


def func(arg):
    options_list = ['剪刀', '石头', '布']
    random_option = random.choice(options_list)
    print("对手的选择：", random_option)

    if arg == '布' and random_option == '石头':
        print('赢!')

    if arg == '布' and random_option == '布':
        print('平局!')

    if arg == '布' and random_option == '剪刀':
        print('输!')

    if arg == '剪刀' and random_option == '布':
        print('赢!')

    if arg == '剪刀' and random_option == '剪刀':
        print('平局!')

    if arg == '剪刀' and random_option == '石头':
        print('输!')

    if arg == '石头' and random_option == '剪刀':
        print('赢!')

    if arg == '石头' and random_option == '石头':
        print('平局!')

    if arg == '石头' and random_option == '布':
        print('输!')


if __name__ == "__main__":
    arg = input('你的选择：')
    func(arg)

