#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from enum import Enum,unique

Month = Enum('Month',('Jan','Feb')) # 定义一个Month类型的枚举类
print(Month.Jan)    # 引用一个常量
print(Month.Jan.value) # 获取枚举值指向的值
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
 
@unique # 检查没有重复值   
class ErrorCode(Enum):
    Error1 = '001'
    Error2 = '002'
error1 = ErrorCode.Error1
print(error1)
error1 = ErrorCode['Error1']
print(error1)
print(error1.value)
for name,member in ErrorCode.__members__.items(): # 遍历所有成员，包括重复的
    print(name,'=>',member,',',member.value)
for error in ErrorCode: # 如有重复成员，只遍历第一个
    print(error,',',error.name,',',error.value)
    
class Gender(Enum):
    Male = 0
    Female = 1
class Student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

bart = Student('Bart',Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')