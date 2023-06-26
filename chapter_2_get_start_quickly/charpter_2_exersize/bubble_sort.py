#! /usr/bin/env python
# -*- coding:utf-8 -*-


"""通过python实现冒泡排序"""


def bubble_sort(nums):
    """
    从小到大进行排序
    :param nums:传入的列表
    :return:
    """
    for_count = len(nums)
    for_count_1 = for_count

    for i in range(for_count):
        for j in range(for_count_1):
            if j + 1 == for_count_1:
                break
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

        for_count_1 -= 1

    return nums


if __name__ == '__main__':
    nums = [1, 3, 2, 4, 1, 7, 4, 5, 2, 10]
    print(bubble_sort(nums))
