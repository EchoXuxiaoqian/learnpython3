#! /usr/bin/env python3
# -*- coding:utf-8 -*-

class Student(object):
    __slots__ = ('name','age')  #用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
  #  __slots__ = ('gender')  
    pass
    

if __name__ == "__main__":
    s = Student()
    s.name = 'tom'
    #s.gender = 'male'   #绑定未定义的属性得到AttributeError的错误
    s1 = GraduateStudent()
    s1.gender = 'male' #__slots__限制对继承的子类不起作用
    s1.score = '98' #子类中有slots限制的话，允许定义的属性就是父类加子类的