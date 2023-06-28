#! /usr/bin/env python
# -*-coding:utf-8 -*-


"""第五章学习笔记"""

# FAQ1:PYTHON支持的数字类型
# ANS1:
#     整型:二进制，八进制，十进制，十六进制
#     浮点型：精确存放需要使用decimal模块
#     复数
#     bool型
#
# FAQ2:各进制转换为十进制
# ANS2:
#     int('1001', base=2):二进制转换为十进制
#     int('1001', base=8):八进制转换为十进制
#     int('1001', base=16)：十六进制转换为十进制
#
# FAQ3:十进制转换为各进制
# ANS3:
#     hex(1000):十进制转换为十六进制
#     oct(1000):十进制转换为八进制
#     bin(1000):十进制转换为二进制
#
# FAQ4:ASCII转换
# ANS4:
#     chr(97):十进制转换为ASCII
#     ord('a'): ASCII转换为十进制
#
# FAQ5:random模块
# ANS5:
#     random.randint(a, b):返回两者之间的随机整数
#     random.randrange(a, b, step):以step为步进，随机返回一个值
#     random.uniform(a, b):和random.randint(a, b)一样，但是返回的是浮点数， 且不包含上限
#     random.random():返回浮点数，上限是0.0；下限是1.0
#     random.choce():随机返回给定序列中的一个元素

