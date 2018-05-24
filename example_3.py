#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:07
# @Author  : JY.Liu
# @Site    : 
# @File    : example_3.py
# @Software: PyCharm

def decorator(func):
    def wrapper():
        print("setp 2")
        print("[Debug]: call function: %s()" % func.__name__)
        return func()

    print("setp 1")
    return wrapper

@decorator
def say_hello():
    print("setp 3")
    print("hello...")

@decorator
def say_goodby():
    print("setp 3")
    print("goodby...")

if __name__ == "__main__":
    say_hello()
    say_goodby()
