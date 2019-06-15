#! /usr/bin/env python3
# -*- coding:utf-8 -*-

class Student(object):   
    @property
    def score(self):
        return self._score   
    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise TypeError("score must be integer!")
        if score < 0 or score > 100:
            raise ValueError("score must between 0-100!")
        self._score = score
    @property
    def age(self):
        return self._age
        
        
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,width):
        self._width = width
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,height):
        self._height = height  
    @property
    def resolution(self):
        return self._height*self._width
    
if __name__ == '__main__':
    try:
        s = Student()
        s.score = 80
        print(s.score)
        #s.age = 15  # can't set attribute,该属性只有getter方法，为只读属性
        s = Screen()
        s.width = 1024
        s.height = 768
        print('resolution =', s.resolution)
        if s.resolution == 786432:
            print('测试通过!')
        else:
            print('测试失败!')
    except Exception as e:
        print(e)
    