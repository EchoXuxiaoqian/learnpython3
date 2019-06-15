#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO) # 配置日志输出的级别
def foo(s):
    n = int(s)
    assert n!=0,'n is zero'
    return 10/n

def foo1(s):
    n = int(s)
    logging.info('n = %d' % n)
    print(10 / n)
    
foo1(0)