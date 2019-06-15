#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 捕捉和打印错误
import logging
try:
    print('trying...')
    r = 10/int('0')
    print('result:',r)
except BaseException as e:  #所有错误类型的基类，可捕捉所有的异常
    print('exception:',e)   # e.__class__可获取类型
    logging.exception(e)    # logging.exception 打印错误栈
else:
    print('no error')
finally:
    print('finally...')
print('END')
    

# 抛出错误，尽量选择python内置的错误类型
def foo(s):
    n = int(s)
    if n==0:
        raise ZeroDivisionError('invalid value:%s' % s)
    return 10/n
def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError')
        raise
    except ZeroDivisionError as e:
        print('ZeroDivisionError')
     #   raise   # raise不带参数，则将error原样往上抛 
    
bar()
