#! /usr/bin/env python
# -*- coding:utf-8 -*-


"""chapter_2_15.py: 排序三个数"""


def func1(nums):
    """
    从下到大排序
    :param nums:
    :return:
    """
    for_count = len(nums)

    for i in range(for_count):
        for j in range(for_count):
            if j+1 == for_count:
                break
            if nums[j] >= nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

        for_count -= 1

    return nums


def func2(nums):
    """
    从大到小排序
    :param nums:
    :return:
    """
    for_count = len(nums)

    for i in range(for_count):
        for j in range(for_count):
            if j+1 == for_count:
                break
            if nums[j] <= nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

        for_count -= 1

    return nums


if __name__ == "__main__":
    nums = [5, 1, 3, 2, 8, 4, 1, 2, 3]
    print(func1(nums))
    print(func2(nums))

