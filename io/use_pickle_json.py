#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pickle
import json

d = dict(name='Tom',age='18',tel='152254878')
print(d)
print(pickle.dumps(d)) # pickle.dumps()方法把任意对象序列化成一个bytes
with open('test_pickle.txt',mode='wb') as f:
    pickle.dump(d,f) # 将对象序列化成bytes之后写入文件 
with open('test_pickle.txt',mode='rb') as f:
    d2 = pickle.load(f) # pickle.load()方法把bytes反序列化出对象
print(d2)

d = dict(name='Tom',age='18',tel='152254878',flag=True,address='浙江杭州')
print(d)
json_str = json.dumps(d)
print(json_str) # json.dumps()返回标准json格式的str
d2 = json.loads(json_str) # json.loads()将json字符串反序列化
print(d2)

class Student(object):
    #__slots__ = ('name','age')
    def __init__(self,name,age):
        self.name = name
        self.age = age
s = Student('Tom','22')
#json_str = json.dumps(s) # 直接转换抛出TypeError: <__main__.Student object at 0x02D22F70> is not JSON serializable异常
def student2dict(s):
    return {
        'name':s.name,
        'age':s.age
    }
json_str = json.dumps(s,default=student2dict) # 使用dumps的可选参数default传入转换函数，将student先转换为dict
print(json_str) 
print(json.dumps(s,default=lambda obj:obj.__dict__)) # 该方法适用于所有对象,除了定义了__slots__的class
s1 = json.loads(json_str)
print(isinstance(s1,dict)) # 反序列化的对象为dict，如果要反序列成对象实例，需要适用可选参数object_hook传入转换函数，将dict转换成实例
def dict2student(d):
    return Student(d['name'],d['age'])
s2 = json.loads(json_str,object_hook=dict2student)
print(isinstance(s2,dict))
print(isinstance(s2,Student))
print(s2)

obj = dict(name='小米',age='12',addr = 'hangzhou')
s1 = json.dumps(obj, ensure_ascii=True)
print(s1)
s11 = json.loads(s1)
print(s11)
s2 = json.dumps(obj, ensure_ascii=False) 
print(s2)
s22 = json.loads(s2)
print(s22)

