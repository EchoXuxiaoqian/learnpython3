#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score > 100 or self.score < 0 :
            raise ValueError('invalid score:%d' % self.score)
        if self.score >= 80:
                    return 'A'        
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'