#! /usr/bin/evn python
# -*- coding:utf-8 -*-

"""chapter_5_13.py: 小时数转换为分钟数"""


def func(hours, minutes):
    try:
        hours, minutes = list(map(int, [hours, minutes]))
    except Exception as e:
        return e

    minutes = hours * 60 + minutes

    return minutes


if __name__ == "__main__":
    hours, minutes = input('time:').split(':')
    print('转换后的结果：', func(hours, minutes))