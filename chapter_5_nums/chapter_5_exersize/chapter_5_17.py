#! /usr/bin/evn python
# -*- coding:utf-8 -*-

"""chapter_5_17.py: 随机数"""


import random


def func():
    num_list_1 = []
    num_list_2 = []
    for i in range(2, 101):
        num_list_1.append(random.randint(0, pow(2, 31)-1))

    for i in range(1, 101):
        num_list_2.append(random.choice(num_list_1))

    num_list_2.sort()

    return num_list_2


if __name__ == "__main__":
    print(func())