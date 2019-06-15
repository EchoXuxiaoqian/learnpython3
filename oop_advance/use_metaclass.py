#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Hello(object):
    def hello(self,name='world'):
        print('hello,%s.' % name)
        
h = Hello()
h.hello()
print(type(Hello))  # 类的type是type
print(type(h))  # 实例的type是类

def fn(self,name='world'): # 先定义函数
    print('Hi,%s.' % name)
Hi = type('Hi',(object,),dict(hi=fn)) # type创建class，参数为类名，继承的父类，方法与函数绑定
hi = Hi()
hi.hi()
print(type(Hi))
print(type(hi))


