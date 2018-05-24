#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 14:18
# @Author  : JY.Liu
# @Site    : 
# @File    : example_1.py
# @Software: PyCharm

import inspect

def prepare():
    call_name = inspect.stack()[1][3]
    print("[Debug]: call function: %s()" % call_name)
    # for i in call_name:
    #     print i

def say_hello():
    prepare()
    print("hello...")

def say_goodby():
    prepare()
    print("goodby...")


if __name__ == "__main__":
    say_hello()
    say_goodby()