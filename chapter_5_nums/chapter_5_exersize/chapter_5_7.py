#! /usr/bin/evn python
# -*- coding:utf-8 -*-

"""chapter_5_7.py: 计算营业税"""


def func(money, radio=0.05):
    try:
        money = float(money)
        result = money * radio
        return result
    except Exception as e:
        return e


if __name__ == "__main__":
    money = input("money:")
    print(func(money))



