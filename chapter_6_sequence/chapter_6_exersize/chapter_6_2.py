#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_6_2.py:标识符检查"""


import string
import keyword

legal_char_list = list(string.ascii_letters + string.digits + '_')


def func(seq):
    for i in seq:
        if i not in legal_char_list:
            return '非法标识符'

    if seq[0] in string.digits:
        return '非法标识符'

    if seq in keyword.kwlist:
        return '非法标识符'
    else:
        return '合法标识符'


if __name__ == "__main__":
    seq = input('arg：')
    print(func(seq))