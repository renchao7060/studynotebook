#-*- coding: utf-8-*-
"""
@progect=Practice_9.19
@file=p42
@author=Administrator
@create_time=2017/9/19 0019 下午 5:20
"""

import time

def bulk(self):
    print('%s is bulking...'%self.name)

class Dog(object):
    def __init__(self,name):
        self.name=name
    def eat(self):
        print('%s is eating'%self.name)

d=Dog('xiaobai')
# d.eat()


choice=input('>>:')

'''属性判断，查找，设置，删除'''
# if hasattr(d,choice):
    # print(getattr(d,choice))
# else:
    # setattr(d,choice,10)
    # print(getattr(d,choice))

'''方法判断，查找，设置，删除'''
if hasattr(d,choice):
    func=getattr(d,choice)
    func()
else:
    setattr(d,choice,bulk)
    func=getattr(d,choice)
    func(d)

# time.sleep(5)
# delattr(d,choice)
# print(getattr(d,choice))