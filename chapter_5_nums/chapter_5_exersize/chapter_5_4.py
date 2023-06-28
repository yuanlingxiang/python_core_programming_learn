#! /usr/bin/evn python
# -*- coding:utf-8 -*-

"""chapter_5_4.py: 计算是否是闰年"""


def func(year):
    """
    计算是否是闰年
    :param year: 传入的年份
    :return:
    """
    try:
        year = int(year)
    except Exception as e:
        return e

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return '是润年'
    else:
        return '不是闰年'


if __name__ == "__main__":
    year = input('input year:')
    print(func(year))
