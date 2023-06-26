#! /usr/bin/env python
# -*- coding:utf-8 -*-


"""chapter_3_13.py:"""

import os


def make_text_file(fname):

    while True:
        if os.path.exists(fname):
            print("error: '%s' already exists" % fname)
            return
        else:
            break

    all_text = []
    print("Enter lines ('.' by itself to quit).")

    while True:
        entry = input('input text:')
        if entry == '.':
            break
        else:
            all_text.append(entry)

    with open(fname, 'w') as fobj:
        fobj.writelines(['%s\n' % x for x in all_text])
    print('done')
    

def read_text_file():
    fname = input('enter filename:')

    with open(fname, 'r') as fobj:
        for eachline in fobj:
            print(eachline.strip())


if __name__ == "__main__":
    fname = input('fname:')
    fname = os.path.join(os.getcwd(), fname)
    make_text_file(fname)
    read_text_file()
