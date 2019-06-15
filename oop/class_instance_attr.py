#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Student(object):
    classname = 'Student'
    def __init__(self,name):
        self.name = name
        
s = Student('Tom')  #创建实例
s.score = '90'  # 实例属性
print(s.name,s.score)

print(s.classname)  # 打印classname属性，因为实例并没有classname属性，所以会继续查找class的classname属性
print(Student.classname)# 打印类属性

s.classname = 's' # 给实例绑定classname属性
print(s.classname)  # 实例属性优先级高于类属性，因此会屏蔽掉类的classname属性
print(Student.classname)

del s.classname
print(s.classname)  

class Student(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count += 1
        
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')