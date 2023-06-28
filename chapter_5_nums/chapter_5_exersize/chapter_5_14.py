#! /usr/bin/evn python
# -*- coding:utf-8 -*-

"""chapter_5_14.py: 银行利息"""


def func(money, days, radio=0.0005):
    try:
        money = float(money)
        days = int(days)
    except Exception as e:
        return e

    for i in range(days):
        money = money + money * radio

    return money


if __name__ == "__main__":
    money, days = input('input money, days:').split(',')
    print('结果为：', func(money, days))



