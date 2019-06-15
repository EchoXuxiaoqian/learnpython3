#! /usr/bin/env python3
# -*- coding:utf-8 -*-

class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object(name:%s)' % (self.name)
        
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1 # 初始化两个计数器
    def __iter__(self):
        return self # 返回可迭代对象
    def __next__(self): # 使得该类可用于for...in循环
        self.a,self.b = self.b,self.a+self.b # 计算下一个值
        if self.a > 10: # 退出循环的条件
            raise StopIteration()
        return self.a
    def __getitem__(self,n):    # 使得可以通过下标访问元素
        a,b=1,1
        for i in range(n):
            a,b = b,a+b
        return a

class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path,path))
    def __str__(self):
        return self._path
    __repr__ = __str__
    def __call__(self,param=''): # 可直接调用实例，还可定义参数
        if param != '':
            return Chain('%s/%s' % (self._path,param))
        return Chain(self._path)

if __name__ == '__main__':
    s = Student('Tommy')
    print(s)
    f = Fib()
    for i in f:
        print(i)
    print(f[5])
    print(Chain('http://api/server').user.friends)
    c = Chain('test')
    try:   
        print('callable: %s' % callable(c))
        print(c())   #实例本身是不可调用对象，实例方法只能通过instance.method()来调用
    except Exception as e:
        print(e)
    print(Chain('http://api/server').user('Tommy').friends)