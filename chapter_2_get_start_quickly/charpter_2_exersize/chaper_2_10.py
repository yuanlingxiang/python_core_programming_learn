#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_2_10.py:用户输入一个1~100的数，正确显示并退出；输入错误，提示用户再次输入，直到正确为止"""


def func1():
    while True:
        num = float(input('num='))
        if 1 <= num <= 100:
            return num
        else:
            print('input num not in 1~100, try again')


if __name__ == "__main__":
    print(func1())