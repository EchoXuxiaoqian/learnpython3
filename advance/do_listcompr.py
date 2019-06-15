# -*- coding:utf-8 -*-
import os

L = [x*x for x in range(1,11)]
print(L)
L = [ x*x for x in range(1,11) if x%2 == 0]
print(L)
L = [ a+b for a in 'ABC' for b in 'abc']
print(L)

d = {'A':'a','B':'b'}
L = [ k+'=>'+v for k,v in d.items()]
print(L)

d = [('A','A1'),('B','B1')]
L = [t+'=>'+t1 for t,t1 in d]
print(L)

dirs = [d for d in os.listdir('.')] # os.listdir列出文件和目录
print(L)

# convert all string to lower
L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s,str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')