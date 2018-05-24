#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:19
# @Author  : JY.Liu
# @Site    : 
# @File    : example_4.py
# @Software: PyCharm

def decorator(func):
    def wrapper(*args, **kwargs):
        print("setp 2")
        print("[Debug]: call function: %s()" % func.__name__)
        return func(*args, **kwargs)
    print("setp 1")
    return wrapper

@decorator
def say_hello(arg):
    print("setp 3")
    print("hello %s" % arg)
    print('*' * 20)

@decorator
def say_goodby(arg1, arg2):
    print("setp 3")
    print("goodby %s, %s" % (arg1, arg2))
    print('*' * 20)

if __name__ == "__main__":
    say_hello("wo de ge")
    say_goodby("sickness", "poor")
