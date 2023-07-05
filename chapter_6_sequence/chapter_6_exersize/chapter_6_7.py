#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_6_7.py:调试"""

# 输入
num_str = input("enter a number：")

# 将输入转换为整型
num_num = int(num_str)

# 生成列表
fac_list = list(range(1, num_num+1))
print("before:", fac_list)

# 赋值i=0
i=0
l2 = []

# 循环
while i < len(fac_list):
    # 移除列表中能被最大值求余==0的元素
    if num_num % fac_list[i] != 0:
        l2.append(fac_list[i])

    i = i + 1


print('after:', l2)
