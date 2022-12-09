# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
В строке могут присутствовать скобки как круглые, так и квадратные скобки. Каждой
открывающей скобке соответствует закрывающая того же типа (круглой – круглая,
квадратной- квадратная). Напишите рекурсивную функцию, проверяющую правильность
расстановки скобок в этом случае.
"""


def check(a, errorb=0, errorc=0):
    if errorb < 0:
        return False
    if errorc < 0:
        return False
    if a:
        if a[0] == '(':
            errorb += 1
        elif a[0] == ')':
            errorb -= 1
        elif a[0] == '[':
            errorc += 1
        elif a[0] == ']':
            errorc -= 1
        return check(a[1:], errorb, errorc)
    return errorb == 0, errorc == 0


if __name__ == '__main__':
    if check(input("Введите строку: ")):
        print("True")
    else:
        print("False")
