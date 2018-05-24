#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 15:45
# @Author  : JY.Liu
# @Site    : 
# @File    : example_5.py
# @Software: PyCharm

from datetime import datetime

def logging(level='INFO'):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print "[{level}] {time}: enter function {func}()".format(
                level=level,
                time=datetime.now(),
                func=func.__name__)
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper


@logging(level='INFO')
def say(something):
    print "say {}!".format(something)


@logging(level='DEBUG')
def do(something):
    print "do {}...".format(something)


if __name__ == '__main__':
    say('hello')
    do("my work")
    say('goodbye')
