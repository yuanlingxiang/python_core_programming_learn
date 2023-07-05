#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""chapter_6_15.py：转换"""

from datetime import datetime


def func1(date1, date2):
    date1 = datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.strptime(date2, '%Y-%m-%d')

    interval_date = date1 - date2

    print("两个日期间隔为：", interval_date.days)


def func2(brithday):
    now = datetime.now()
    birthday_days = now - datetime.strptime(brithday, '%Y-%m-%d')

    print("出生到现在的天数：", birthday_days.days)


def func3(birthday):
    now = datetime.now()
    birthday_month = datetime.strptime(birthday, '%Y-%m-%d').month
    birthday_day = datetime.strptime(birthday, '%Y-%m-%d').day
    now_year = now.year
    next_birthday = datetime.strptime('%s-%s-%s' % (now_year+1, birthday_month, birthday_day), '%Y-%m-%d')

    print('下个生日日期：', (next_birthday - now).days)


if __name__ == "__main__":
    func1('2023-07-06', '2023-07-04')
    func2('1988-07-04')
    func3('1988-07-04')



