#! /usr/bin/evn python
# -*- coding:utf-8 -*-

"""chapter_5_16.py: 家庭财务"""


def func(balance, payment):
    print('%-10s%-10s%-10s' % ('Pyth#', 'Paid', 'balance'))
    print('%-10s%-10s%-10s' % ('-' * 5, '-' * 5, '-' * 5))

    month = 0
    print('%-10s%-10s%-10s' % (month, payment-payment, balance))

    while True:
        month += 1
        if balance < payment:
            payment = balance
            balance = 0
            print('%-10s%-10s%-10s' % (month, round(payment, 2), round(balance, 2)))
            break
        else:
            balance = balance - payment
            print('%-10s%-10s%-10s' % (month, round(payment, 2), round(balance, 2)))


if __name__ == "__main__":
    balance = input('Enter opening balance:')
    payment = input('Enter monthly payment:')
    balance, payment = list(map(float, (balance, payment)))
    func(balance, payment)