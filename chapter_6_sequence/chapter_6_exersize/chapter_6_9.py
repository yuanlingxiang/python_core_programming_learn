#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_6_9.py：接收分钟数转换成小时和分钟数"""


def func(minutes):
    minutes = int(minutes)
    hours, minutes = list(map(str, divmod(minutes, 60)))

    return ':'.join([hours.zfill(2), minutes.zfill(2)])


if __name__ == "__main__":
    minutes = input('minutes:')
    print(func(minutes))


