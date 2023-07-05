#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_6_12.py：查找字符串"""


def findchar(str, char):
    for k, v in enumerate(str):
        if v == char:
            return k
    else:
        return -1

def rfindchar(str, char):
    for k in range(1, len(str)+1):
        if str[-k] == char:
            return len(str)-k
    else:
        return -1

def subchar(str, origchar, newchar='a'):
    for i in str:
        if i == origchar:
            str = str.replace(origchar, newchar)
            continue

    return str


if __name__ == "__main__":
    str = input('str:')
    char = input('char:')
    print('index:', findchar(str, char))
    print('index:', rfindchar(str, char))
    print('result:', subchar(str, origchar='l'))


