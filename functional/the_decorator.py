# -*- coding:utf-8 -*-

import datetime,time
import functools

def now():
  time = datetime.datetime.now()
  return time
 
getTime = now
print(getTime.__name__)
print(getTime())
  
f =  lambda x:x*x
print(f.__name__)

# 定义一个能打印日志的decorator
def log(func):
  @functools.wraps(func)  #将原始函数的属性复制过来
  def wrapper(*args,**kw):
    print('call %s():' % func.__name__)
    return func(*args,**kw)
  return wrapper

@log
def now1():
  time = datetime.datetime.now()
  return time

print(now1()) #加上log装饰器之后输出为None?? 因为相当于执行的是log(now1)返回的是wrapper函数
print(now1.__name__)  #返回的是wrapper函数，需要@functools.wraps(func)将原始函数的属性复制过来


# 作用于任何函数上，打印函数执行时间的装饰器
def metric(func):
  @functools.wraps(func)
  def wrapper(*args,**kw):
    start_time = time.time()
    print('begin call %s' % func.__name__)
    r = func(*args,**kw)
    print('end call %s' % func.__name__)
    end_time = time.time()
    print('%s executed in %.4f ms' % (func.__name__, end_time-start_time))
    return r
  return wrapper

# 测试
@metric
def fast(x, y):
  time.sleep(0.0012)
  return x + y;
  
@metric
def slow(x, y, z):
  time.sleep(0.1234)
  return x * y * z;
  
f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
  print('测试失败!')
elif s != 7986:
  print('测试失败!')
else:
  print('测试成功!')
  
#如果装饰器本身需要传入参数，则需要定义一个返回装饰器的高阶函数
def log(text=''):
  def metric(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
      start_time = time.time()
      print('%s begin call %s' % (text,func.__name__))
      r = func(*args,**kw)
      print('%s end call %s' % (text,func.__name__))
      end_time = time.time()
      print('%s %s executed in %.4f ms' % (text,func.__name__, end_time-start_time))
      return r
    return wrapper
  return metric

@log
def slow(x, y, z):
  time.sleep(0.1234)
  return x * y * z;

@log('xxq')
def slow(x, y, z):
  time.sleep(0.1234)
  return x * y * z;    
f = slow(11, 22,33)

def slow(x, y, z):
  time.sleep(0.1234)
  return x * y * z;    
func1 = slow
f = slow(11, 22,33)
