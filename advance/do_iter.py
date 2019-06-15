# -*- coding:utf-8 -*-
from collections import Iterable

print(isinstance('abc',Iterable)) # 判断对象是否是可迭代对象
print(isinstance(12,Iterable))
print(isinstance(['abc'],Iterable))
print(isinstance(('abc'),Iterable))
print(isinstance({'abc'},Iterable))
print(isinstance({'abc':12},Iterable))

# iter list
L = list(range(5))
for t in L:
    print(t)
# iter list with index
for i,v in enumerate(L):
    print(i,v)
    
# iter dict key
L = {'a':65,'b':66}
for k in L:
    print(k)
# iter dict value
for v in L.values():
    print(v)
# iter dict key and value
for k,v in L.items():
    print('%s=>%s' % (k,v))
    
# iter string
for t in 'swdwe':
    print(t)

for x,y in [(1,2),('a','b')]: # list中元素如果是tuple，可直接通过赋值进行拆分
    print(x,y)
    
def findMinAndMax(L):
    min = None
    max = None
    for t in L:
        if min == None or t < min:
            min = t
        if max == None or t > max:
            max = t
    return min,max
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')