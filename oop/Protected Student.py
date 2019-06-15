#!/usr/bin/env python3
# -*- coding=utf-8 -*-

class Student(object):
    '''
    Student records basic student information

    >>> bart = Student('Bart','male',99)
    >>> bart.name
    Traceback (most recent call last):
      ...
    AttributeError: 'Student' object has no attribute 'name'
    >>> bart.score
    Traceback (most recent call last):
      ...
    AttributeError: 'Student' object has no attribute 'score'
    >>> bart.print_score()
    Bart:99
    >>> bart.get_grade()
    'A'

    '''
    def __init__(self,name,gender,score):
        self.__name = name  # 私有变量，不允许外部直接访问
        self.__score = score
        self.__gender = gender
    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if gender in ('male','female','unknown'):       # 对输入值的合法性做校验
            self.__gender=gender
        else:
            raise ValueError("wrong value,must input 'male','female','unknown'")
    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

if __name__== '__main__':
    bart = Student('Bart','male',99)
   # print(bart.name) 私有变量无法直接从外部访问
   # print(bart.score)
    bart.print_score()
    score = bart.get_grade()
    print(score)
    lisa = Student('Lisa', 'female',99)
    bart = Student('Bart','female', 59)
    print(lisa.get_name(), lisa.get_grade())
    print(bart.get_name(), bart.get_grade())      
    import doctest
    doctest.testmod()
    bart = Student('Bart', 'male','86')
    if bart.get_gender() != 'male':
        print('测试失败!')
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print('测试失败!')
        else:
            print('测试成功!')    
    bart.set_gender('F')