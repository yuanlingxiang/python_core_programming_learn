#! /usr/bin/evn python
# -*- coding:utf-8 -*-

"""chapter_5_5.py: 取余"""


def func(money):
    """
    取余
    :param money:传入的钱
    :return:
    """
    try:
        money = int(float(money) * 100)
    except Exception as e:
        return e

    corn_25_nums, money = divmod(money, 25)
    corn_10_nums, money = divmod(money, 10)
    corn_5_nums, money = divmod(money, 5)

    corn_dict = {'corn_25_nums': corn_25_nums,
                 'corn_10_nums': corn_10_nums,
                 'corn_5_nums': corn_5_nums,
                 'corn_1_nums': money,}

    return corn_dict


if __name__ == "__main__":
    money = input('input money:')
    print(func(money))
