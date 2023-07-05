#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_6_11.py：整数与IP地址相互转换"""


def func1(ip, bin_num_str=''):
    """
    ip地址转换为整型
    :param ip:
    :param bin_num_str:
    :return:
    """
    num_list = list(map(int, ip.split('.')))

    for i in num_list:
        if i not in range(0, 256):
            print('ip地址非法')
        else:
            # 注意：strip('0b')会删除0和b的字符，并不是以'0b'为整体来进行删除的
            bin_num_str += bin(i).lstrip('0b').zfill(8)

    return int(bin_num_str, base=2)


def func2(num):
    """
    整型转换成ip地址
    :param num:
    :return:
    """
    ip_list = []
    num_bin = bin(num).lstrip('0b').zfill(32)
    num_bin_list = map(str, [num_bin[:8], num_bin[8:16], num_bin[16:24], num_bin[24:]])

    for i in num_bin_list:
        ip_list.append(int(i, base=2))

    ip_list = list(map(str, ip_list))

    return '.'.join(ip_list)


if __name__ == "__main__":
    ip = input('ip:')
    num = func1(ip)
    print(func1(ip))
    print(func2(num))






