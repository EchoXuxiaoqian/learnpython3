#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
import mydict
#from mydict import Dict

class TestMydict(unittest.TestCase):
    def setUp(self):    # 调用每一个方法之前执行
        print('setUp..')    # 调用每一个方法之后执行
    def tearDown(self):
        print('tearDown..')
    def test_init(self):        # 测试方法必须以test开头
        d = mydict.Dict(a=1,b='test')
        self.assertEqual(d.a,1)     # 断言d.a == 1
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict)) # 断言 isinstance(d,dict) == True
    def test_key(self):
        d = mydict.Dict(a=1,b='test')
        self.assertEqual(d['a'],1)  
    def test_attr(self):
            d = mydict.Dict(a=1,b='test')
            self.assertEqual(d.a,1)      
    def test_attrerror(self):
        d = mydict.Dict()
        with self.assertRaises(AttributeError):   
            value = d.empty       
    def test_keyerror(self):
        d = mydict.Dict()
        with self.assertRaises(KeyError):   # 通过d['empty']访问不存在的key时，断言会抛出KeyError
            value = d['empty']
            
            
if __name__=='__main__':
    unittest.main()   # 单元测试断言不通过的测试方法，会输出Error
        