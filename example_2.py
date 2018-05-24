#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 14:33
# @Author  : JY.Liu
# @Site    : 
# @File    : example_2.py
# @Software: PyCharm

def decorator(func):
    def wrapper():
        print("setp 2")
        print("[Debug]: call function: %s()" % func.__name__)
        return func()
    print wrapper
    print("setp 1")
    return wrapper

def say_hello():
    print("setp 3")
    print("hello...")

def say_goodby():
    print("setp 3")
    print("goodby...")

if __name__ == "__main__":
    say_hello = decorator(say_hello)
    say_goodby = decorator(say_goodby)
    print say_hello
    print say_goodby
    say_hello()
    say_goodby()
