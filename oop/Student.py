#!/usr/bin/env python3
# -*- coding=utf-8 -*-

class Student(object):
      '''
      Student records basic student information
      
      >>> bart = Student('Bart',99)
      >>> bart.name
      'Bart'
      >>> bart.score
      99
      >>> bart.print_score()
      Bart:99
      >>> bart.get_grade()
      'A'
      
      '''
      def __init__(self,name,score):
            self.name = name
            self.score = score
      def print_score(self):
            print('%s:%s' % (self.name,self.score))
      def get_grade(self):
            if self.score >= 90:
                  return 'A'
            elif self.score >= 60:
                  return 'B'
            else:
                  return 'C'
             
if __name__== '__main__':
      bart = Student('Bart',99)
      print(bart.name)
      print(bart.score)
      bart.print_score()
      score = bart.get_grade()
      print(score)
      lisa = Student('Lisa', 99)
      bart = Student('Bart', 59)
      print(lisa.name, lisa.get_grade())
      print(bart.name, bart.get_grade())      
      import doctest
      doctest.testmod()