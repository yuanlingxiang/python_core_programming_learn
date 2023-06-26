#! /usr/bin/env python
# -*- coding:utf-8 -*-


"""chapter_2_11.py:带文本菜单程序"""


def func1(nums):
    """
    计算五个数之和, 五个数的平均值
    :param nums: nums为数字列表
    :return:
    """
    # 计算五个数的和
    result_sum = 0
    for i in range(len(nums)):
        result_sum = result_sum + float(nums[i])

    result_avg = result_sum / len(nums)

    return result_sum, result_avg


def main():
    while True:
        nums = input('input nums:').split(',')
        option = input('''input option
        1:取五个数之和
        2:取五个数平均值
        x:退出程序
        ''')
        if option == '1':
            print(func1(nums)[0])
        elif option == '2':
            print(func1(nums)[1])
        elif option == 'x':
            return
        else:
            print('input error, try again')


if __name__ == '__main__':
    main()
