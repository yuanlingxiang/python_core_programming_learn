#! /usr/bin/evn python
# -*- coding:utf-8 -*-

"""chapter_5_3.py:成绩判断程序"""


def func1(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 0 <= score < 60:
        return 'E'
    else:
        return 'input error'


if __name__ == "__main__":
    score = float(input('score:'))
    print(func1(score))